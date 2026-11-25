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
| 23/11/2026 15h04–15h07 | ajuste mobile da central (modo claro + rolagem em iframe) com Opus 5.5 high, liberado pelo João acima de 90% | 92%→100% (reinicia 23/11 16h20) | 0%→0% (semana nova, reinicia 30/11 15h) | ~US$ 1,06, 8 turnos; INTERROMPIDO pelo limite de 5h (429 usage_limit_reached) ainda no diagnóstico; central.tsx não foi alterado; sem compra de créditos; pasta /workspace/central-joao-sessao |

| 24/11/2026 10h35–10h45 | atualizar PR #113, origem da caixinha, regras da visita e proposta de deploy automático (Sonnet, esforço medium) | 35%→48% (reinicia 24/11 13h29) | 27%→28% (reinicia 30/11 14h59) | ~US$ 1,17, 41 turnos; testes sdr-base 865 ok (merge) e 869 ok (ritmo); #113 e #42 atualizados; deploy local sem push (token sem escopo workflow); pasta /workspace/pr113-24-11-sessao |

| 24/11/2026 11h21–11h45 | correção da queda de login do painel da Matriz (Sonnet, esforço medium, PR #80) | 52%→57% (reinicia 24/11 13h30) | 28%→29% (reinicia 30/11 15h) | ~US$ 0,46, 18 turnos; testes 1081 ok, 0 falhas; squash merge `fa728b7`; deploy Cloudflare não publicado (publicação é por tag + wrangler, sem credencial no box, não é Vercel); pasta /workspace/matriz-login-24-11-sessao |

| 24/11/2026 11h52–12h09 | contrato automático no CRM Blanc (Sonnet, esforço medium, PR rascunho #49) | 57%→71% (reinicia 24/11 13h29) | 29%→29% (reinicia 30/11 14h59) | ~US$ 1,36, 6 turnos; suíte 553 testes, 548 ok na rodada completa (2 falhas novas corrigidas e revalidadas à parte; restam as 3 pré-existentes); #48 mesclado `1a26929`; migration só arquivo, não aplicada; pasta /workspace/blanc-contrato-crm-24-11-sessao |

| 24/11/2026 12h28–12h39 | ajustes do contrato automático no CRM Blanc (Sonnet, esforço medium, PR rascunho #49) | 71%→81% (reinicia 24/11 13h30) | 29%→30% (reinicia 30/11 15h) | ~US$ 2,04 em 3 chamadas da mesma conversa (correções 12h28 e 12h30); suíte 562 testes, 559 ok, 3 falhas pré-existentes; migration só arquivo, não aplicada; pasta /workspace/blanc-contrato-crm-24-11-ajustes-sessao |

| 25/11/2026 14h11–14h12 | diagnóstico da etapa do lead e origem Meta + exportação do público qualificado no CRM Blanc (Sonnet, esforço medium, só leitura) | 10%→16% (reinicia 25/11 17h30) | 42%→43% (reinicia 30/11 15h) | ~US$ 0,24, 8 turnos; sem alteração de código, banco, commit ou PR; CSV só no box em /workspace/blanc-publico-meta/; pasta /workspace/blanc-publico-meta-sessao |

## Notas
- Leituras do `/usage` em 19/11: às 15h42, 66% / 18%; às 15h55, 82% / 19%. Reinícios anunciados pelo CLI: janela de 5h às 18h20 de 19/11; semana às 15h de 23/11 (America/Sao_Paulo).
- O `pgrep -af 'bin/claude'` não pega sessões iniciadas só como `claude -p`. Nesses casos, olhar também `pgrep -af 'claude -p'`.
- 23/11: o processo do CLI aparece como `.../bin/claude.exe -p ...`, e `pgrep -af 'claude -p'` não o pega. Conferir também `pgrep -af 'claude.exe'`.

- 23/11 16h25–16h43 · central mobile (modo claro + rolagem) · Opus 5.5 high · janela 5h 0%→13%, semana 0%→2% · sessão encerrada por mim (só faltava um teste de toque). João: ajuste pequeno = Sonnet normal.
- 23/11 16h43–16h50 · central mobile, continuação (o disparo único retomou a sessão sem saber que ela tinha sido encerrada) · Opus 5.5 high · janela 5h 13%→34%, semana 2%→4% · ~US$ 4,53, 20 turnos · só teste: o timeout do Fechar era bug do teste (toque escalado 2x no iframe); central.tsx não mudou desde 16h29; todos os testes OK.
