#!/usr/bin/env python3
"""
importar_extrato.py
-------------------
Le os extratos que voce exportou do banco (arquivos CSV ou OFX), categoriza
cada transacao AUTOMATICAMENTE por palavras-chave, e salva tudo em
`dados_banco.json` — o mesmo formato que o dashboard ja usa.

Como usar:
    1. Exporte seu extrato no app/site do Nubank (CSV ou OFX).
    2. Coloque o(s) arquivo(s) na pasta `extratos/`.
    3. Rode:  python importar_extrato.py
    4. Abra o dashboard (python -m http.server 8000).

Gratuito, sem API, sem mensalidade. Os arquivos de extrato ficam so no seu
computador (a pasta extratos/ esta no .gitignore).
"""

import csv
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXTRATOS_DIR = os.path.join(BASE_DIR, "extratos")
OUTPUT_PATH = os.path.join(BASE_DIR, "dados_banco.json")


# --------------------------------------------------------------------------- #
# Categorizacao automatica (o coracao do projeto)
# --------------------------------------------------------------------------- #
# Cada categoria tem uma lista de palavras-chave. Se a descricao da transacao
# contiver qualquer uma delas, ela recebe essa categoria. Edite a vontade!
REGRAS_CATEGORIA = {
    "Alimentacao": ["ifood", "rappi", "restaurante", "lanchonete", "padaria",
                    "pao", "mercado", "supermerc", "hortifruti", "acougue",
                    "bar ", "burger", "pizza", "cafe", "starbucks", "mcdonald"],
    "Transporte": ["uber", "99app", "99 ", "cabify", "posto", "shell", "ipiranga",
                   "petrobras", "combustivel", "estacionamento", "metro", "onibus",
                   "passagem", "gasolina"],
    "Assinaturas": ["netflix", "spotify", "amazon prime", "prime video", "hbo",
                    "disney", "youtube premium", "apple.com", "icloud", "google",
                    "playstation", "xbox", "deezer"],
    "Saude": ["farmacia", "drogaria", "droga", "hospital", "clinica", "laboratorio",
              "psicolog", "dentista", "academia", "smart fit", "gym"],
    "Moradia": ["aluguel", "condominio", "luz", "energia", "eletrop", "enel",
                "cemig", "agua", "sabesp", "gas ", "internet", "vivo", "claro",
                "tim", "oi ", "iptu"],
    "Compras": ["amazon", "mercado livre", "mercadolivre", "magalu", "magazine",
                "americanas", "shopee", "aliexpress", "loja", "shopping", "renner",
                "riachuelo", "zara"],
    # Renda vem ANTES de Transferencias: um "salario recebido" deve cair em
    # Renda, nao em Transferencias (que tambem casaria com "recebido").
    "Renda": ["salario", "salário", "pagamento recebido", "deposito", "rendimento",
              "proventos", "pro-labore"],
    "Transferencias": ["pix", "ted", "doc ", "transferencia", "transferência",
                       "enviado", "recebido"],
    "Lazer": ["cinema", "ingresso", "show", "viagem", "hotel", "airbnb", "booking",
              "decolar", "latam", "gol ", "azul "],
}

CATEGORIA_PADRAO = "Outros"


def categorizar(descricao):
    """Descobre a categoria de uma transacao a partir da descricao."""
    texto = (descricao or "").lower()
    for categoria, palavras in REGRAS_CATEGORIA.items():
        for palavra in palavras:
            if palavra in texto:
                return categoria
    return CATEGORIA_PADRAO


# --------------------------------------------------------------------------- #
# Leitura/parse dos valores e datas (formatos variados)
# --------------------------------------------------------------------------- #
def parse_valor(bruto):
    """Converte texto de valor em numero. Aceita '1.234,56' e '1234.56'."""
    if bruto is None:
        return 0.0
    s = str(bruto).strip().replace("R$", "").replace(" ", "")
    if not s:
        return 0.0
    # Formato brasileiro: ponto de milhar e virgula decimal -> 1.234,56
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return round(float(s), 2)
    except ValueError:
        return 0.0


def parse_data(bruto):
    """Converte texto de data para o formato YYYY-MM-DD."""
    s = (bruto or "").strip()[:10]
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return s  # devolve como veio se nao reconhecer


# --------------------------------------------------------------------------- #
# Leitura de CSV (descobre as colunas pelo nome do cabecalho)
# --------------------------------------------------------------------------- #
COLUNAS_DATA = ("data", "date")
COLUNAS_DESC = ("descricao", "descrição", "title", "titulo", "título",
                "estabelecimento", "memo", "lancamento", "histórico", "historico")
COLUNAS_VALOR = ("valor", "amount", "value")


def _achar_coluna(cabecalho, candidatas):
    for col in cabecalho:
        if col and col.strip().lower() in candidatas:
            return col
    return None


def ler_csv(caminho):
    transacoes = []
    with open(caminho, "r", encoding="utf-8-sig", newline="") as f:
        amostra = f.read(2048)
        f.seek(0)
        # Descobre se o separador e virgula ou ponto-e-virgula.
        delimitador = ";" if amostra.count(";") > amostra.count(",") else ","
        leitor = csv.DictReader(f, delimiter=delimitador)
        cabecalho = leitor.fieldnames or []

        col_data = _achar_coluna(cabecalho, COLUNAS_DATA)
        col_desc = _achar_coluna(cabecalho, COLUNAS_DESC)
        col_valor = _achar_coluna(cabecalho, COLUNAS_VALOR)

        if not (col_data and col_valor):
            print(f"  AVISO: nao reconheci as colunas de {os.path.basename(caminho)}")
            print(f"         cabecalho encontrado: {cabecalho}")
            return []

        # Fatura de cartao (Nubank) usa cabecalho em ingles ('amount') e lista
        # os gastos como numeros POSITIVOS. Ja o extrato da conta usa 'valor'
        # com sinal (gasto = negativo). Para deixar tudo no mesmo padrao
        # (gasto = negativo), invertemos o sinal quando for fatura de cartao.
        eh_fatura_cartao = col_valor.strip().lower() in ("amount", "value")

        for linha in leitor:
            descricao = (linha.get(col_desc) or "").strip() if col_desc else ""
            valor = parse_valor(linha.get(col_valor))
            if eh_fatura_cartao:
                valor = -valor
            transacoes.append({
                "data": parse_data(linha.get(col_data)),
                "descricao": descricao,
                "valor": valor,
            })
    return transacoes


# --------------------------------------------------------------------------- #
# Leitura de OFX (formato padrao de extrato bancario)
# --------------------------------------------------------------------------- #
def ler_ofx(caminho):
    with open(caminho, "r", encoding="latin-1", errors="ignore") as f:
        conteudo = f.read()

    transacoes = []
    for bloco in re.findall(r"<STMTTRN>(.*?)</STMTTRN>", conteudo, re.DOTALL | re.IGNORECASE):
        def pega(tag):
            m = re.search(rf"<{tag}>([^<\r\n]*)", bloco, re.IGNORECASE)
            return m.group(1).strip() if m else ""

        data_bruta = pega("DTPOSTED")[:8]  # AAAAMMDD
        data = data_bruta
        if len(data_bruta) == 8:
            data = f"{data_bruta[:4]}-{data_bruta[4:6]}-{data_bruta[6:8]}"

        descricao = pega("MEMO") or pega("NAME")
        transacoes.append({
            "data": data,
            "descricao": descricao,
            "valor": parse_valor(pega("TRNAMT")),
        })
    return transacoes


# --------------------------------------------------------------------------- #
# Orquestracao
# --------------------------------------------------------------------------- #
def coletar():
    if not os.path.isdir(EXTRATOS_DIR):
        os.makedirs(EXTRATOS_DIR, exist_ok=True)

    arquivos = sorted(glob.glob(os.path.join(EXTRATOS_DIR, "*.csv")) +
                      glob.glob(os.path.join(EXTRATOS_DIR, "*.ofx")))

    if not arquivos:
        print("Nenhum extrato encontrado na pasta 'extratos/'.")
        print("Exporte seu extrato do Nubank (CSV ou OFX) e coloque-o la dentro.")
        sys.exit(1)

    todas = []
    for caminho in arquivos:
        nome = os.path.basename(caminho)
        print(f"Lendo {nome} ...")
        brutas = ler_ofx(caminho) if caminho.lower().endswith(".ofx") else ler_csv(caminho)
        for t in brutas:
            t["categoria"] = categorizar(t["descricao"])
            t["conta"] = nome
        todas.extend(brutas)
        print(f"  {len(brutas)} transacoes")

    # Mais recentes primeiro.
    todas.sort(key=lambda t: t.get("data", ""), reverse=True)

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fonte": "extrato",
        "saldo_total": round(sum(t["valor"] for t in todas), 2),
        "contas": [],
        "transacoes": todas,
    }


def salvar(resultado):
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print(f"\nOK! Dados salvos em: {OUTPUT_PATH}")
    print(f"  Transacoes: {len(resultado['transacoes'])}")
    print(f"  Soma do periodo: R$ {resultado['saldo_total']:.2f}")
    # Mostra um resumo por categoria, pra conferir se ficou bom.
    por_cat = {}
    for t in resultado["transacoes"]:
        if t["valor"] < 0:
            por_cat[t["categoria"]] = por_cat.get(t["categoria"], 0) + abs(t["valor"])
    if por_cat:
        print("  Gastos por categoria:")
        for cat, total in sorted(por_cat.items(), key=lambda x: -x[1]):
            print(f"    - {cat}: R$ {total:.2f}")


def main():
    salvar(coletar())


if __name__ == "__main__":
    main()
