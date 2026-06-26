#!/usr/bin/env python3
"""
conectar_banco.py
-----------------
Conecta na API da Pluggy (Open Finance), busca saldo, contas e transacoes
de todas as contas conectadas, e salva o resultado consolidado em
`dados_banco.json` com um timestamp.

Modos (definidos no config.json):
  - "sandbox": cria sozinho um banco de TESTE (dados ficticios, ja
               categorizados). Otimo para validar tudo sem mexer em conta real.
  - "real":    usa os bancos que voce conectou de verdade no painel da Pluggy.

Uso:
    python conectar_banco.py
"""

import json
import os
import sys
import time
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    print("ERRO: a biblioteca 'requests' nao esta instalada.")
    print("Instale com:  pip install requests")
    sys.exit(1)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "dados_banco.json")

API_URL = "https://api.pluggy.ai"
TIMEOUT = 30  # segundos por requisicao

# Connector e credenciais do "banco de mentira" da Pluggy (sandbox).
SANDBOX_CONNECTOR_ID = 2
SANDBOX_USUARIO = "user-ok"
SANDBOX_SENHA = "password-ok"


# --------------------------------------------------------------------------- #
# Configuracao
# --------------------------------------------------------------------------- #
def carregar_config(caminho=CONFIG_PATH):
    """Le e valida o config.json."""
    if not os.path.exists(caminho):
        print(f"ERRO: arquivo de configuracao nao encontrado: {caminho}")
        print("Crie o config.json a partir do config.example.json (veja o README).")
        sys.exit(1)

    with open(caminho, "r", encoding="utf-8") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERRO: config.json invalido: {e}")
            sys.exit(1)

    client_id = config.get("pluggy_client_id", "").strip()
    client_secret = config.get("pluggy_client_secret", "").strip()
    modo = config.get("modo", "sandbox").strip().lower()

    if not client_id or client_id == "seu_client_id_aqui":
        print("ERRO: 'pluggy_client_id' nao configurado no config.json")
        sys.exit(1)
    if not client_secret or client_secret == "seu_client_secret_aqui":
        print("ERRO: 'pluggy_client_secret' nao configurado no config.json")
        sys.exit(1)

    return client_id, client_secret, modo


# --------------------------------------------------------------------------- #
# Chamadas a API da Pluggy
# --------------------------------------------------------------------------- #
def autenticar(client_id, client_secret):
    """Troca client_id + client_secret por um apiKey temporario (~2h)."""
    resp = requests.post(
        f"{API_URL}/auth",
        json={"clientId": client_id, "clientSecret": client_secret},
        timeout=TIMEOUT,
    )
    if resp.status_code == 403:
        print("ERRO: client_id ou client_secret invalidos (403). Confira o config.json.")
        sys.exit(1)
    resp.raise_for_status()
    return resp.json()["apiKey"]


def _headers(api_key):
    return {"X-API-KEY": api_key, "Content-Type": "application/json"}


def criar_item_sandbox(api_key):
    """Cria uma conexao com o banco de TESTE da Pluggy e retorna o item id."""
    print("Criando conexao com o banco de teste (sandbox)...")
    resp = requests.post(
        f"{API_URL}/items",
        headers=_headers(api_key),
        json={
            "connectorId": SANDBOX_CONNECTOR_ID,
            "parameters": {"user": SANDBOX_USUARIO, "password": SANDBOX_SENHA},
        },
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()["id"]


def esperar_item_pronto(api_key, item_id, tentativas=30, intervalo=3):
    """Aguarda o item terminar de sincronizar (status UPDATED)."""
    for _ in range(tentativas):
        resp = requests.get(
            f"{API_URL}/items/{item_id}",
            headers=_headers(api_key),
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
        status = resp.json().get("status")
        if status == "UPDATED":
            return True
        if status in ("LOGIN_ERROR", "OUTDATED", "ERROR"):
            print(f"ERRO: a conexao falhou (status: {status}).")
            return False
        print(f"  ...sincronizando (status: {status})")
        time.sleep(intervalo)
    print("ERRO: tempo esgotado esperando a sincronizacao.")
    return False


def listar_items(api_key):
    """Lista todos os items (bancos conectados) da conta."""
    resp = requests.get(f"{API_URL}/items", headers=_headers(api_key), timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    return data.get("results", data) if isinstance(data, dict) else data


def listar_contas(api_key, item_id):
    """Lista as contas de um item."""
    resp = requests.get(
        f"{API_URL}/accounts",
        headers=_headers(api_key),
        params={"itemId": item_id},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json().get("results", [])


def listar_transacoes(api_key, account_id, max_paginas=20):
    """Lista as transacoes de uma conta usando o endpoint novo (/v2, cursor).

    O endpoint antigo (/transactions com page/pageSize) foi descontinuado pela
    Pluggy e responde 410. O novo (/v2/transactions) NAO aceita 'pageSize':
    pagina por 'cursor', devolvendo 'results' e um campo 'next' com a URL da
    proxima pagina. Seguimos o 'next' ate acabar.
    """
    transacoes = []
    url = f"{API_URL}/v2/transactions"
    params = {"accountId": account_id}

    for _ in range(max_paginas):
        resp = requests.get(url, headers=_headers(api_key), params=params, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        transacoes.extend(data.get("results", []))

        proximo = data.get("next")
        if not proximo:
            break
        # O 'next' ja vem como URL completa com os parametros embutidos.
        url, params = proximo, None

    return transacoes


# --------------------------------------------------------------------------- #
# Normalizacao para o dashboard
# --------------------------------------------------------------------------- #
def normalizar_conta(conta):
    return {
        "id": conta.get("id"),
        "nome": conta.get("name") or conta.get("marketingName") or "Conta",
        "tipo": conta.get("type", ""),
        "saldo": float(conta.get("balance", 0) or 0),
        "moeda": conta.get("currencyCode", "BRL"),
    }


def normalizar_transacao(tx, nome_conta=""):
    """Padroniza os campos e garante o sinal certo (gasto = negativo)."""
    valor = float(tx.get("amount", 0) or 0)
    tipo = (tx.get("type") or "").upper()
    if tipo == "DEBIT":
        valor = -abs(valor)
    elif tipo == "CREDIT":
        valor = abs(valor)

    categoria = tx.get("category") or "Sem categoria"
    data = tx.get("date") or ""
    if isinstance(data, str) and len(data) >= 10:
        data = data[:10]  # mantem só YYYY-MM-DD

    return {
        "data": data,
        "descricao": tx.get("description") or "",
        "categoria": categoria,
        "valor": round(valor, 2),
        "conta": nome_conta,
    }


# --------------------------------------------------------------------------- #
# Orquestracao
# --------------------------------------------------------------------------- #
def coletar_dados():
    client_id, client_secret, modo = carregar_config()

    print("Autenticando na Pluggy...")
    api_key = autenticar(client_id, client_secret)

    if modo == "sandbox":
        item_id = criar_item_sandbox(api_key)
        if not esperar_item_pronto(api_key, item_id):
            sys.exit(1)
        item_ids = [item_id]
    else:
        print("Buscando bancos conectados...")
        items = listar_items(api_key)
        item_ids = [it.get("id") for it in items if it.get("id")]
        if not item_ids:
            print("Nenhum banco conectado encontrado. Conecte uma conta no painel da Pluggy")
            print("ou use o modo 'sandbox' no config.json para testar.")
            sys.exit(1)

    contas_norm = []
    transacoes_norm = []

    for item_id in item_ids:
        for conta in listar_contas(api_key, item_id):
            c = normalizar_conta(conta)
            contas_norm.append(c)
            for tx in listar_transacoes(api_key, conta["id"]):
                transacoes_norm.append(normalizar_transacao(tx, c["nome"]))

    # Mais recentes primeiro.
    transacoes_norm.sort(key=lambda t: t.get("data", ""), reverse=True)
    saldo_total = round(sum(c["saldo"] for c in contas_norm), 2)

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "modo": modo,
        "saldo_total": saldo_total,
        "contas": contas_norm,
        "transacoes": transacoes_norm,
    }


def salvar(resultado, caminho=OUTPUT_PATH):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print(f"\nOK! Dados salvos em: {caminho}")
    print(f"  Modo: {resultado['modo']}")
    print(f"  Saldo total: R$ {resultado['saldo_total']:.2f}")
    print(f"  Contas: {len(resultado['contas'])}")
    print(f"  Transacoes: {len(resultado['transacoes'])}")


def main():
    try:
        resultado = coletar_dados()
    except requests.exceptions.HTTPError as e:
        print(f"ERRO HTTP na API da Pluggy: {e}")
        # Mostra a explicacao que a propria Pluggy mandou junto com o erro.
        if e.response is not None:
            print("--- Detalhe da Pluggy ---")
            print(e.response.text)
            print("-------------------------")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"ERRO de conexao com a Pluggy: {e}")
        sys.exit(1)
    salvar(resultado)


if __name__ == "__main__":
    main()
