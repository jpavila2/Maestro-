# Uso do Claude Code (conta principal)

> Medição pelo `/usage` do Claude CLI: percentual da janela de 5 horas e da semana, com o horário de reinício em America/Sao_Paulo.
> A conta é a principal (`CLAUDE_CONFIG_DIR=/home/box/.claude-meta`). A conta secundária não entra aqui.
> Regra do João (19/11 às 15h39): o teto de 400 respostas não vale mais. Só parar se a janela de 5h ou a semana chegarem perto de 90%.
> Blocos feitos antes dessa regra entram na tabela como "antes do /usage", com a quantidade de respostas só como referência histórica.

| Data (America/Sao_Paulo) | Tipo de demanda | Janela de 5h (antes→depois) | Semana (antes→depois) | Observação |
| --- | --- | --- | --- | --- |
| 19/11/2026 manhã | script de importação Animados | — | — | antes do /usage; 57 respostas |
| 19/11/2026 | estimativa SDR | — | — | antes do /usage; 64 respostas |
| 19/11/2026 13h42– | renovação Turma | — | — | antes do /usage; 74 respostas |
| 19/11/2026 14h57–15h16 | correção IA Blanc | — | — | antes do /usage; 132 respostas |
| 19/11/2026 15h42–15h52 | ajuste de preço IA Blanc | 66%→82% (reinicia 19/11 18h20) | 18%→19% (reinicia 23/11 15h) | primeiro bloco medido pelo /usage; 63 respostas (referência) |
| 19/11/2026 15h55 | pacote/especificação Turma para o Guga | 82%→não iniciado (reinicia 19/11 18h20) | 19%→não iniciado (reinicia 23/11 15h) | adiado: a janela de 5h estava em 82%, perto de 90%. O bloco anterior tinha subido 16 pontos. O pacote fica para depois do reinício das 18h20. |
| 19/11/2026 18h40–18h53 | pacote/especificação Turma para o Guga (Sonnet, zip + mensagem) | 0%→9% (janela nova, reinicia 19/11 23h40) | 19%→19% (reinicia 23/11 15h) | cerca de US$ 1,06 de custo de API reportado pelo CLI; 13 arquivos no zip; sem PR, banco ou contato com o Guga |
| 20/11/2026 10h30–10h35 | estimativa SDR "cliente novo sem código" + custo por conversa, para o Reg (Haiku, só leitura) | 0%→1% (reinicia 20/11 15h29) | 19%→20% (reinicia 23/11 15h) | 16 turnos, ~2,3 min; arquivo /workspace/sdr-sem-codigo-estimativa-20-11.md |
| 22/11/2026 09h59–10h11 | checagem pré-merge PR #43 CRM Blanc (Sonnet, testes + revisão de risco + conflito) | 0%→4% (reinicia 22/11 14h50) | 21%→21% (reinicia 23/11 15h) | ~US$ 0,61, 8 turnos; 3 pontos PASSOU; sem merge/deploy pelo Claude |
| 22/11/2026 09h59–10h11 | checagem pré-merge PR #43 Blanchouse-crm (Sonnet: testes, revisão de risco, conflito) | 0%→4% (reinicia 22/11 14h50) | 21%→21% (reinicia 23/11 15h) | 8 turnos, ~US$ 0,61 reportado pelo CLI; 3 pontos PASSOU; merge 35a71f2 e deploy READY |
| 23/11/2026 11h37–11h51 | visão de detalhe e prazo clicável no painel de Entregas (Sonnet, PR #116) | 3%→10% (reinicia 23/11 16h20) | 21%→22% (reinicia 23/11 15h) | ~US$ 0,67, 20 turnos; testes 768→769, 0 falhas; sem migração; pasta /workspace/regency-entregas-detalhe-23-11-sessao |
| 23/11/2026 11h55–12h13 | Central de tarefas do João, fase 1 (Sonnet, PR rascunho #117) | 10%→29% (reinicia 23/11 16h19) | 22%→23% (reinicia 23/11 14h59) | ~US$ 1,28, 32 turnos; testes 768/769→780, 0 falhas; sem migração; pasta /workspace/regency-central-tarefas-23-11-sessao |
| 23/11/2026 12h58–13h05 | artefato da central do João (Sonnet, TSX local, sem repo/PR) + 1 ajuste de contraste | 46%→51% (reinicia 23/11 16h20) | 24%→25% (reinicia 23/11 15h) | ~US$ 0,89 somando as 2 chamadas, 7 turnos; arquivo local no box, sem push do TSX; pasta /workspace/central-joao-sessao |
| 23/11/2026 13h08–13h35 | troca SDR → agente comercial / Iris (Sonnet, retomada; PRs #119/#77/#111/#44) | 51%→62% (reinicia 23/11 16h20) | 25%→25% (reinicia 23/11 15h) | ~US$ 2,65, 35 turnos nesta retomada; tentativas 12h19–12h41 tinham sido interrompidas; testes sem falhas novas; pasta /workspace/renomear-sdr-iris-23-11-sessao |
| 23/11/2026 13h39–13h41 | ajuste do artefato da central (Sonnet: contraste AA, Kanban acima, cores Regency; TSX local, sem repo/PR) | 62%→70% (reinicia 23/11 16h19) | 25%→26% (reinicia 23/11 14h59) | ~US$ 0,46, 10 turnos; contraste 0 falhas (menor 6,01:1); sem push do TSX; pasta /workspace/central-joao-sessao |
| 23/11/2026 13h55–13h56 | extração de regras de contrato da Blanc (Sonnet, esforço medium, só leitura, sem repo/PR) | 70%→73% (reinicia 23/11 16h19) | 26%→26% (reinicia 23/11 14h59) | ~US$ 0,25, 6 turnos; saída só no box; contratos não commitados |
| 23/11/2026 13h59–14h07 | redesign da central com Opus 5.5 high (claude-opus-5-5, effort high, sem fallback; TSX local, sem repo/PR) | 73%→92% (reinicia 23/11 16h20) | 26%→27% (reinicia 23/11 15h) | ~US$ 2,41, 31 turnos; JANELA DE 5H EM 92%: pausar novas sessões até 16h20; contraste 0 falhas; pasta /workspace/central-joao-sessao |

## Notas
- Leituras do `/usage` em 19/11: às 15h42, 66% / 18%; às 15h55, 82% / 19%. Reinícios anunciados pelo CLI: janela de 5h às 18h20 de 19/11; semana às 15h de 23/11 (America/Sao_Paulo).
- O `pgrep -af 'bin/claude'` não pega sessões iniciadas só como `claude -p`. Nesses casos, olhar também `pgrep -af 'claude -p'`.
- 23/11: o processo do CLI aparece como `.../bin/claude.exe -p ...`, e `pgrep -af 'claude -p'` não o pega. Conferir também `pgrep -af 'claude.exe'`.
