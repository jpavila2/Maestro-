# 🏦 banco-mcp-integrador

Painel pessoal de finanças: junta saldo e transações do seu banco num
dashboard local, com os gastos **categorizados automaticamente** — pra você
ver, num lugar só, pra onde vai o seu dinheiro.

```
banco-mcp-integrador/
├── importar_extrato.py     # CAMINHO GRÁTIS: lê extratos (CSV/OFX) e categoriza
├── conectar_banco.py       # caminho via Pluggy (API; sandbox grátis, real pago)
├── dashboard_simples.html  # o painel: saldo, transações e gráfico
├── extratos/               # coloque aqui os extratos exportados do banco
├── dados_banco.json        # gerado pelos scripts — NÃO versionado
├── config.json             # chaves da Pluggy — NÃO versionado
├── config.example.json     # modelo de configuração
├── .gitignore
└── README.md
```

Há **dois jeitos** de trazer seus dados. Os dois geram o mesmo
`dados_banco.json`, que alimenta o mesmo dashboard.

---

## ✅ Caminho A — Arrastar o extrato no painel (grátis, sem terminal)

O jeito mais simples. Tudo acontece **dentro do navegador** — não precisa de
Python, terminal nem servidor.

1. **Exporte o extrato no Nubank** (a única parte manual — exige seu login):
   - **Conta:** app ou site do Nubank → área da conta/NuConta → exportar
     extrato em **CSV** ou **OFX**.
   - **Cartão:** abra a fatura → exportar em **CSV**.
2. **Abra o painel:** dê dois cliques em `dashboard_simples.html`
   (abre no seu navegador).
3. **Arraste o arquivo** exportado pra dentro da área de upload (ou clique
   para escolher). Pode soltar vários (conta + cartão).

Pronto: ele lê, **categoriza automaticamente** e mostra saldo, transações e
o gráfico — na hora. Seus dados nunca saem do navegador.

> **Categorização:** as regras ("iFood → Alimentação" etc.) ficam no topo do
> `<script>` em `dashboard_simples.html` (variável `REGRAS`). É só editar.

### Alternativa por linha de comando (opcional)

Se preferir gerar um `dados_banco.json` (por exemplo para automatizar):
```bash
python3 painel.py          # pega extrato da Downloads, lê e abre o painel
# ou, por partes:
python3 importar_extrato.py # lê os arquivos da pasta extratos/
```

> **Categorização:** as regras ("iFood → Alimentação" etc.) ficam no topo do
> `importar_extrato.py`, na variável `REGRAS_CATEGORIA`. É só editar a lista
> de palavras-chave para deixar do seu jeito.

---

## 💳 Caminho B — Pluggy (API)

A Pluggy é uma "ponte" com os bancos via Open Finance (só leitura). O
**sandbox** (banco de teste fictício) é grátis e ótimo para experimentar;
conectar **banco real** exige plano de produção (pago, voltado a empresas).

### 1. Pegar as chaves
Crie conta em [pluggy.ai](https://pluggy.ai), vá em **API Keys** e copie o
**Client ID** e o **Client Secret**.

### 2. Configurar
```bash
cp config.example.json config.json
```
```json
{
  "pluggy_client_id": "SEU_CLIENT_ID",
  "pluggy_client_secret": "SEU_CLIENT_SECRET",
  "modo": "sandbox",
  "item_ids": []
}
```
- `modo: "sandbox"` → cria um banco de teste automaticamente.
- `modo: "real"` → conecte seu banco no painel da Pluggy, copie o `itemId`
  da conexão e coloque em `item_ids` (a Pluggy não permite listar conexões
  pela API, por segurança).

### 3. Rodar e abrir o dashboard
```bash
pip install requests
python3 conectar_banco.py
python3 -m http.server 8000
```

---

## Privacidade
Nenhum dado financeiro sai do seu computador: tudo fica em arquivos locais
(`dados_banco.json`, `extratos/`, `config.json`), todos no `.gitignore`.
