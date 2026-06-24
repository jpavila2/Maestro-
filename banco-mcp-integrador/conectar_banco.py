#!/usr/bin/env python3
"""
conectar_banco.py
-----------------
Conecta na API do Banco MCP (ou Open Finance), busca saldo, contas e
transações, e salva o resultado consolidado em `dados_banco.json` com
um timestamp.

Uso:
    python conectar_banco.py

Configuração:
    Edite `config.json` e coloque sua URL e API key reais.
"""

import json
import os
import sys
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    print("ERRO: a biblioteca 'requests' nao esta instalada.")
    print("Instale com:  pip install requests")
    sys.exit(1)


CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados_banco.json")

# Timeout das requisicoes HTTP em segundos.
TIMEOUT = 30


def carregar_config(caminho=CONFIG_PATH):
    """Le e valida o config.json."""
    if not os.path.exists(caminho):
        print(f"ERRO: arquivo de configuracao nao encontrado: {caminho}")
        print("Crie o config.json (veja o README) antes de rodar.")
        sys.exit(1)

    with open(caminho, "r", encoding="utf-8") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERRO: config.json invalido: {e}")
            sys.exit(1)

    url = config.get("banco_mcp_url", "").strip()
    api_key = config.get("api_key", "").strip()

    if not url:
        print("ERRO: 'banco_mcp_url' nao definido no config.json")
        sys.exit(1)

    if not api_key or api_key == "seu_token_aqui":
        print("ERRO: 'api_key' nao configurada no config.json")
        print("Substitua 'seu_token_aqui' pela sua chave real do Banco MCP.")
        sys.exit(1)

    return url, api_key


def _headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def buscar_contas(url, api_key):
    """Busca a lista de contas do usuario."""
    resp = requests.get(
        f"{url.rstrip('/')}/v1/accounts",
        headers=_headers(api_key),
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    data = resp.json()
    # Aceita tanto {"accounts": [...]} quanto uma lista direta.
    return data.get("accounts", data) if isinstance(data, dict) else data


def buscar_transacoes(url, api_key, limite=50):
    """Busca as transacoes mais recentes do usuario."""
    resp = requests.get(
        f"{url.rstrip('/')}/v1/transactions",
        headers=_headers(api_key),
        params={"limit": limite},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("transactions", data) if isinstance(data, dict) else data


def calcular_saldo_total(contas):
    """Soma o saldo de todas as contas."""
    total = 0.0
    for conta in contas:
        try:
            total += float(conta.get("balance", conta.get("saldo", 0)) or 0)
        except (TypeError, ValueError):
            continue
    return round(total, 2)


def normalizar_transacao(tx):
    """Padroniza os campos de uma transacao para o dashboard."""
    return {
        "data": tx.get("date") or tx.get("data") or "",
        "descricao": tx.get("description") or tx.get("descricao") or "",
        "categoria": tx.get("category") or tx.get("categoria") or "Sem categoria",
        "valor": float(tx.get("amount", tx.get("valor", 0)) or 0),
        "conta": tx.get("account") or tx.get("conta") or "",
    }


def coletar_dados():
    """Orquestra a coleta e monta o dicionario final."""
    url, api_key = carregar_config()

    print(f"Conectando em {url} ...")
    try:
        contas = buscar_contas(url, api_key)
        transacoes_raw = buscar_transacoes(url, api_key, limite=50)
    except requests.exceptions.HTTPError as e:
        print(f"ERRO HTTP ao consultar a API: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"ERRO de conexao com a API: {e}")
        sys.exit(1)

    transacoes = [normalizar_transacao(t) for t in transacoes_raw]
    # Ordena por data (mais recente primeiro), quando houver data.
    transacoes.sort(key=lambda t: t.get("data", ""), reverse=True)

    resultado = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "saldo_total": calcular_saldo_total(contas),
        "contas": contas,
        "transacoes": transacoes,
    }
    return resultado


def salvar(resultado, caminho=OUTPUT_PATH):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print(f"OK! Dados salvos em: {caminho}")
    print(f"  Saldo total: R$ {resultado['saldo_total']:.2f}")
    print(f"  Contas: {len(resultado['contas'])}")
    print(f"  Transacoes: {len(resultado['transacoes'])}")


def main():
    resultado = coletar_dados()
    salvar(resultado)


if __name__ == "__main__":
    main()
