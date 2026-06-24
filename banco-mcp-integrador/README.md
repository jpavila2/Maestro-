# 🏦 banco-mcp-integrador

Integrador simples que conecta na API do **Banco MCP** (ou Open Finance),
baixa saldo, contas e transações, e exibe tudo num dashboard HTML local.

```
banco-mcp-integrador/
├── config.json            # sua configuração (API key) — NÃO versionado
├── config.example.json    # modelo de configuração
├── conectar_banco.py      # baixa os dados e gera dados_banco.json
├── dashboard_simples.html # visualização (saldo, transações, gráfico)
├── dados_banco.json       # gerado pelo script — NÃO versionado
├── .gitignore
└── README.md
```

---

## 1. Configurar a API key

Copie o modelo e edite com seus dados reais:

```bash
cp config.example.json config.json
```

Abra `config.json` e substitua o placeholder:

```json
{
  "banco_mcp_url": "https://banco.mcp.ai",
  "api_key": "SEU_TOKEN_REAL_AQUI"
}
```

- **`banco_mcp_url`** — URL base da API do Banco MCP (ou do seu provedor Open Finance).
- **`api_key`** — token de acesso fornecido pelo Banco MCP.

> ⚠️ O `config.json` está no `.gitignore` justamente para a sua API key
> **nunca** ir parar no Git. Não remova essa proteção.

---

## 2. Rodar o integrador

Pré-requisitos: **Python 3.8+** e a biblioteca `requests`.

```bash
pip install requests
python conectar_banco.py
```

O script vai:

1. Ler o `config.json`.
2. Consultar a API (`/v1/accounts` e `/v1/transactions`).
3. Calcular o saldo total somando todas as contas.
4. Salvar tudo em **`dados_banco.json`** com um `timestamp`.

Saída esperada:

```
Conectando em https://banco.mcp.ai ...
OK! Dados salvos em: dados_banco.json
  Saldo total: R$ 12345.67
  Contas: 2
  Transacoes: 42
```

### Formato do `dados_banco.json`

```json
{
  "timestamp": "2026-06-24T12:00:00+00:00",
  "saldo_total": 12345.67,
  "contas": [ { "name": "Conta Corrente", "balance": 8000.00 } ],
  "transacoes": [
    {
      "data": "2026-06-23",
      "descricao": "Mercado",
      "categoria": "Alimentação",
      "valor": -150.00,
      "conta": "Conta Corrente"
    }
  ]
}
```

---

## 3. Abrir o dashboard

O dashboard lê o `dados_banco.json` via `fetch`, então precisa ser servido
por um servidor HTTP local (abrir o arquivo direto com `file://` é bloqueado
pelo navegador).

```bash
python -m http.server 8000
```

Depois abra no navegador:

```
http://localhost:8000/dashboard_simples.html
```

O dashboard mostra:

- 💵 **Saldo consolidado** em destaque.
- 📋 **Tabela** com as últimas 10 transações.
- 🥧 **Gráfico de pizza** dos gastos por categoria (usa as transações
  negativas; se não houver categoria, exibe um aviso).

> Sempre que rodar `python conectar_banco.py` de novo, basta atualizar a
> página para ver os dados mais recentes.

---

## Observações

- O script tolera tanto respostas no formato `{"accounts": [...]}` quanto
  listas diretas, e aceita nomes de campos em inglês (`balance`, `amount`,
  `date`, `category`) ou português (`saldo`, `valor`, `data`, `categoria`).
- Nenhum dado financeiro é enviado para fora: tudo fica em arquivos locais.
