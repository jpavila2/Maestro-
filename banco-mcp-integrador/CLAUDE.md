# Notas do projeto: banco-mcp-integrador

## Sobre o usuário (João Pedro)
- NÃO é desenvolvedor. Está aqui para APRENDER, não só copiar comandos.
- Regra permanente: SEMPRE explicar didaticamente, mesmo que rapidamente,
  o QUE estamos fazendo, POR QUE, e QUAL ferramenta está envolvida —
  a cada passo. O objetivo é gerar conhecimento real, não só resolver.
- Usar analogias do dia a dia. Evitar jargão sem traduzir.

## O que é o projeto
Painel pessoal de finanças que puxa saldo + transações dos bancos (via
Pluggy / Open Finance), já categorizados, e mostra num dashboard local.
Visão de longo prazo: depois, consultar/registrar pelo WhatsApp.

## Stack / ferramentas
- Python (script conectar_banco.py) — busca os dados na Pluggy
- Pluggy API — a "ponte" com os bancos (só leitura)
- HTML + Chart.js (dashboard_simples.html) — a tela
- Git/GitHub — guarda o código (repo jpavila2/maestro-, branch
  claude/banco-mcp-integrador-9qnk1x)
