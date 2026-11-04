# 🔄 RETOMAR — Maestro (centro de comando / "Jarvis")

Ponto de entrada pra continuar de onde parou — conta nova do Claude, Codex ou outra máquina.
> Num agente novo: **"Leia o RETOMAR.md e continue de onde parei."**

## 1. O que é
**Maestro** = monorepo pessoal do João, o "Jarvis" que vai orquestrar todas as automações.
Cada subsistema = uma pasta na raiz. Índice completo no `README.md`.
- **GitHub:** jpavila2/maestro- (branch `claude/banco-mcp-integrador-9qnk1x`)
- **Importante sobre o João:** NÃO é dev — está aprendendo. Sempre explicar didaticamente o quê/por quê/qual ferramenta, com analogias. (Ver `maestro-financeiro/CLAUDE.md`.)

## 2. Subsistemas
| Pasta | O que é | Status | Retomar |
|---|---|---|---|
| `maestro-financeiro/` | Painel que lê extrato do banco (CSV/OFX), categoriza e mostra saldo/gráficos | ✅ funcionando | `maestro-financeiro/RETOMAR.md` |
| `banco-mcp-integrador/` | Integração de banco via MCP | 🔜 inicial | (sem RETOMAR ainda) |

## 3. Estado atual (ATUALIZAR ao concluir etapas)
- 🔜 **EM ANDAMENTO (desde 03/11/2026): descoberta do Maestro como AGENTE PESSOAL** (abertura do dia + cobrança de fios no WhatsApp, memória única multi-IA).
  Tudo decidido até aqui, com o porquê: `descoberta/2026-11-03-04-descoberta-maestro.md` (seção 11 = próximos passos).
  Comparação feita (`descoberta/motor-do-maestro.html`): recomendação Hermes Agent.
- 🧪 **TESTE DE 1 DIA NO MAC (aprovado pelo João em 04/11, é descartável):**
  - [x] Hermes Agent v0.22.7 instalado em `~/.hermes` (comando `~/.local/bin/hermes`), sem navegador e sem computer-use. ~2 GB.
  - [x] Cérebro do teste: **Claude Haiku 5.5 via API** (chave `maestro-haiku`, colada pelo João em 04/11). Provider `anthropic`, backup da config em `~/.hermes/config.yaml.bak-antes-maestro`.
    Removida a credencial `claude_code` que o Hermes importou sozinho (usar a assinatura do Claude em ferramenta de terceiros é bloqueado pela Anthropic).
    1º teste: ~18 mil tokens de contexto por mensagem, **US$ 0,0023** a 1ª (sem cache) → estimativa ~US$ 0,10–0,25/dia com 100 msgs.
  - [ ] Depois (quando o ChatGPT Plus renovar): `hermes auth add openai-codex --no-browser --label chatgpt-plus-joao` + código em https://auth.openai.com/codex/device (vale 15 min). Medir quanto come da cota do Plus; Haiku fica de reserva automática.
  - [x] Ferramentas desligadas no CLI e no WhatsApp: computer_use, browser, image_gen, code_execution, delegation. Terminal e arquivos seguem ligados (com aprovação de comando perigoso) — isolamento de verdade só na VPS.
  - [ ] Ligar `stt` (transcrição de áudio, faster-whisper local, grátis) quando o WhatsApp estiver conectado.
  - [ ] Número novo do Maestro (eSIM pré-pago) como 2ª conta no WhatsApp do iPhone → `hermes whatsapp` (modo bot, QR) com `WHATSAPP_ALLOWED_USERS` = só o número do João e `unauthorized_dm_behavior: ignore`.
  - [ ] Restringir ferramentas (`hermes tools`): sem imessage/findmy/computer-use; pasta de trabalho própria.
  - [ ] Primeira abertura do dia (agenda Blanc + pessoal, pagamentos fixos, prazos Regency, RETOMARs). Gatilho: o João acorda em horários diferentes → abrir quando ele mandar a 1ª mensagem do dia ("bom dia") + lembrete de reserva; despertador/atalho do iPhone a estudar.
  - Depois do teste: medir consumo e escolher onde roda 24/7 (VPS barata, Oracle grátis ou PC do Blanc). Nada na AWS da Regency (não misturar dados).
- ⏸️ Pilar financeiro (parado desde 30/06): sistema financeiro é o primeiro pilar. Caminho grátis: arrastar extrato do Nubank no `dashboard_simples.html`.
- Próximas ideias: conectar banco real (sair do sandbox), painel mais rico (evolução mensal/metas), interface por WhatsApp.

## 4. Regras de ouro
- Explicar didaticamente cada passo (o João está aprendendo).
- Audite antes de alterar dados; nada de escrita em massa sem mostrar os números.
- Ao terminar uma etapa: marque `[x]` no plano do subsistema e atualize esta seção.

## 5. Como retomar (cole num agente novo)
```
Estou continuando o Maestro. Leia RETOMAR.md na raiz e o README (índice de subsistemas).
Entre no subsistema em andamento (ver "Estado atual"), leia o RETOMAR.md dele e continue
do primeiro passo não marcado. Explique cada passo de forma didática — não sou dev.
```
