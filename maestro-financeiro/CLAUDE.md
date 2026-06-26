# Notas do projeto: maestro-financeiro

## Sobre o usuário (João Pedro)
- NÃO é desenvolvedor. Está aqui para APRENDER, não só copiar comandos.
- Regra permanente: SEMPRE explicar didaticamente, mesmo que rapidamente,
  o QUE estamos fazendo, POR QUE, e QUAL ferramenta está envolvida —
  a cada passo. O objetivo é gerar conhecimento real, não só resolver.
- Usar analogias do dia a dia. Evitar jargão sem traduzir.

## O que é o projeto
"Maestro Financeiro": painel pessoal de finanças. Caminho principal hoje é
GRÁTIS: o usuário arrasta o extrato (CSV/OFX do Nubank) no dashboard e ele
categoriza automaticamente, no navegador. Visão de longo prazo: WhatsApp.

Histórico de decisões: tentamos Pluggy (real é pago) e pynubank (morto desde
2023). Por isso o caminho atual é importar extrato exportado do banco.

## Stack / ferramentas
- dashboard_simples.html (HTML + JS + Chart.js) — lê/categoriza CSV/OFX no
  navegador (FileReader). É o caminho principal, sem terminal.
- importar_extrato.py / painel.py — alternativa por linha de comando.
- conectar_banco.py — caminho via Pluggy (sandbox grátis; real pago).
- Git/GitHub — repo jpavila2/maestro-, branch claude/banco-mcp-integrador-9qnk1x
