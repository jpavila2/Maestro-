# 🔄 RETOMAR — Maestro Financeiro

Ponto de entrada pra continuar este subsistema. Faz parte do monorepo **Maestro** (ver `../RETOMAR.md`).
> Num agente novo: **"Leia o RETOMAR.md e continue de onde parei."** — e explique tudo de forma didática (o João está aprendendo, não é dev).

## 1. O que é
Painel pessoal de finanças. Caminho principal (GRÁTIS, sem terminal): o João arrasta o
extrato do Nubank (CSV/OFX) no `dashboard_simples.html` e ele categoriza automático no
navegador, mostrando saldo, transações e gráficos.

## 2. Onde está cada coisa
- `dashboard_simples.html` — **o caminho principal** (HTML+JS+Chart.js, lê CSV/OFX no navegador).
- `importar_extrato.py` / `painel.py` — alternativa por linha de comando.
- `conectar_banco.py` — caminho via Pluggy (sandbox grátis; banco real é pago).
- `extratos/` — extratos de exemplo/importados.
- `CLAUDE.md` — contexto + regra de explicar didaticamente.

## 3. Estado atual (ATUALIZAR ao concluir etapas)
- ✅ Dashboard lendo e categorizando extrato no navegador — funcionando.
- ⚙️ Histórico: Pluggy (real é pago) e pynubank (morto desde 2023) descartados → por isso o caminho é importar extrato exportado.
- 🔜 Próximo: conectar banco real / painel mais rico (evolução mensal, filtros, metas) / interface WhatsApp.

## 4. Regras de ouro
- Explicar cada passo didaticamente, com analogia, sem jargão solto.
- Não fazer escrita em massa em dados sem mostrar antes.

## 5. Como retomar (cole num agente novo)
```
Estou continuando o Maestro Financeiro. Leia RETOMAR.md e CLAUDE.md na raiz desta pasta.
Continue do "Próximo" da seção Estado atual. Explique cada passo de forma didática — não sou dev.
```
