# 🏦 banco-mcp-integrador

Painel pessoal de finanças que conecta nas suas contas via **Pluggy**
(Open Finance), puxa saldo e transações **já categorizados**, e mostra tudo
num dashboard local — pra você ver, num lugar só, pra onde vai o seu dinheiro.

```
banco-mcp-integrador/
├── config.json            # suas chaves Pluggy — NÃO versionado
├── config.example.json    # modelo de configuração
├── conectar_banco.py       # autentica na Pluggy e gera dados_banco.json
├── dashboard_simples.html  # painel: saldo, transações e gráfico
├── dados_banco.json        # gerado pelo script — NÃO versionado
├── .gitignore
└── README.md
```

> **Por que Pluggy?** Ela conversa com os bancos e devolve as transações
> **já categorizadas** — acabando com o trabalho manual de classificar gasto
> por gasto. Ela só **lê** os dados (não move dinheiro).

---

## 1. Pegar suas chaves na Pluggy

1. Crie uma conta gratuita em [pluggy.ai](https://pluggy.ai) (painel em
   `dashboard.pluggy.ai`).
2. No painel, vá até **API Keys / Credentials**.
3. Copie o **Client ID** e o **Client Secret**.

> 🔒 O **Client Secret** é uma senha. Nunca compartilhe nem suba pro Git.

## 2. Configurar

Copie o modelo e preencha com suas chaves:

```bash
cp config.example.json config.json
```

```json
{
  "pluggy_client_id": "SEU_CLIENT_ID",
  "pluggy_client_secret": "SEU_CLIENT_SECRET",
  "modo": "sandbox"
}
```

- **`modo: "sandbox"`** → usa um **banco de teste** (dados fictícios, já
  categorizados). O programa cria essa conexão sozinho. Ideal para validar tudo
  sem tocar em conta real.
- **`modo: "real"`** → usa os bancos que você conectou de verdade no painel da
  Pluggy.

> ⚠️ O `config.json` está no `.gitignore` justamente para suas chaves
> **nunca** irem pro Git.

## 3. Rodar o integrador

Pré-requisitos: **Python 3.8+** e a biblioteca `requests`.

```bash
pip install requests
python conectar_banco.py
```

O script vai:

1. Ler o `config.json` e autenticar na Pluggy.
2. No modo `sandbox`, criar e sincronizar o banco de teste automaticamente.
3. Buscar contas e transações de todas as contas.
4. Salvar tudo em **`dados_banco.json`** com `timestamp`.

Saída esperada:

```
Autenticando na Pluggy...
Criando conexao com o banco de teste (sandbox)...
  ...sincronizando (status: UPDATING)
OK! Dados salvos em: dados_banco.json
  Modo: sandbox
  Saldo total: R$ 12345.67
  Contas: 2
  Transacoes: 38
```

## 4. Abrir o dashboard

O dashboard lê o `dados_banco.json` via `fetch`, então precisa de um servidor
local (abrir com `file://` é bloqueado pelo navegador):

```bash
python -m http.server 8000
```

Abra no navegador: **http://localhost:8000/dashboard_simples.html**

Mostra:

- 💵 **Saldo consolidado** em destaque.
- 📋 **Tabela** com as últimas 10 transações.
- 🥧 **Gráfico de pizza** dos gastos por categoria.

> Rodou `conectar_banco.py` de novo? Só atualizar a página.

---

## Do teste para o real

1. Comece com `"modo": "sandbox"` e confirme que o painel aparece certinho.
2. No painel da Pluggy, conecte seu banco de verdade (Open Finance).
3. Troque para `"modo": "real"` no `config.json` e rode de novo.

Nenhum dado financeiro sai do seu computador: tudo fica em arquivos locais.
