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
  - [x] WhatsApp pareado em 04/11 no **modo self-chat** (WhatsApp pessoal do João, chat "Você"). Sessão em `~/.hermes/whatsapp/session` (chmod 700). Prefixo "🎼 *Maestro:*", sem confirmação de leitura, ignora estranhos.
  - [x] **Resultado do teste-chave: a mensagem proativa NÃO apitou no iPhone** (self-chat não notifica). → comprar eSIM pré-pago e trocar pra modo bot (`hermes whatsapp`, opção 1, `WHATSAPP_ALLOWED_USERS` = número pessoal do João). Enquanto isso, as cobranças que precisam apitar vão como **eventos na agenda pessoal com alarme**.
  - [x] Persona do Maestro em `~/.hermes/SOUL.md` (backup do original em `SOUL.md.bak-original`): lê `caderno/fios.md`, cobra até "feito/adia/desisti", português de WhatsApp, limites da fase de teste.
  - [x] Lista de fios criada: `caderno/fios.md` (1º fio real: dentista/plano odontológico). Teste: o Maestro leu e priorizou certo (US$ 0,0024).
  - Gateway: `hermes -p default gateway restart`; log em `~/.hermes/logs/gateway.log`. Só roda com o Mac ligado.
  - [x] **04/11 21h: eSIM Claro do Maestro ativo (21 97560-7150)**, 2ª conta no WhatsApp do iPhone. Hermes em **modo bot** (`WHATSAPP_MODE=bot`), pareado como 5521975607150, responde só ao 8602 do João. Sessão antiga do self-chat guardada em `~/.hermes/whatsapp/session-selfchat-8602-bak` (chmod 700) pra fase "ler conversas". Backup do .env em `.env.bak-selfchat`.
  - [x] Mensagem do número próprio apita (Maestro responde em ~6 s).
  - [ ] **Gmail pessoal só leitura** (05/11, em andamento): projeto Google Cloud `maestro-513800`, Gmail API ligada, público externo em teste (usuário de teste = e-mail pessoal do João), cliente desktop "Maestro Mac". Conectar com `scripts/google-somente-leitura.sh` (o João cola ID e chave secreta no terminal; a IA nunca vê a chave; escopo forçado `gmail.readonly`). Token fica em `~/.hermes/google_token.json` (chmod 600). 1ª chave colada deu `invalid_client`; criada chave nova (final zs9P). Depois: apagar a chave velha (final izwB) e pôr bloco "e-mails esperando resposta" na abertura do dia.
  - Recarga do eSIM: R$ 30 em 04/11 (30 dias). Antes de ~04/12, ver recarga mínima da Claro pra linha não cair (fio do Maestro).
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
