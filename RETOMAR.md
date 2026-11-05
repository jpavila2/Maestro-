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

## 3. Estado atual (ATUALIZAR ao concluir etapas) — última atualização 05/11/2026 ~10h

### 3.1 O que está RODANDO agora (Maestro = agente pessoal no WhatsApp)
- **Motor:** Hermes Agent v0.22.7 em `~/.hermes` (comando `~/.local/bin/hermes`). Cérebro: **Claude Haiku 5.5 via API** (chave `maestro-haiku`), ~US$ 0,002/msg.
- **Serviço do Mac:** launchd `ai.hermes.gateway` (liga sozinho com o Mac). Reiniciar: `launchctl kickstart -k gui/$(id -u)/ai.hermes.gateway`. Log: `~/.hermes/logs/gateway.log`. **Só roda com o Mac acordado.**
- **WhatsApp:** número próprio do Maestro (eSIM Claro **21 97560-7150**, modo bot), responde só ao João (5521990218602). Prefixo "🎼 *Maestro:*". Mensagens apitam no iPhone.
- **Persona/regras:** `~/.hermes/SOUL.md` (backup do original em `SOUL.md.bak-original`). Lê `caderno/fios.md`, `caderno/estado.md` e, em saúde, `caderno/saude.md`.
- **Caderno (memória, legível no Obsidian):** `caderno/fios.md` (fios abertos), `caderno/saude.md`, `caderno/estado.md` (o que o Maestro mandou sozinho + data da última abertura).
- **Horários automáticos (`hermes cron list`):**
  - `abertura-reserva` 9h30: só manda se o João ainda não falou no dia (fios + saúde + agenda de hoje/amanhã, até 6 linhas).
  - `cobranca` 14h e 19h: um fio por vez, sem repetir em 5 h; às 14h também olha e-mails e só cita se for importante. `[SILENT]` quando não há nada.
  - Na 1ª mensagem do João no dia, o próprio chat faz a abertura (regra no SOUL).
- **E-mail (só leitura):** 3 contas — pessoal (`~/.hermes/google_token.json`), `blanc` e `jpavilabtc` (`~/.hermes/gmail-contas/<apelido>/`). Script `scripts/emails.sh` (`CONTA=todas`, busca, `ler <id>`).
- **Agenda:** conta pessoal com `calendar.readonly` + `calendar.events`; ela já enxerga VISITA e blancofficeeventos. Script `scripts/agenda.sh [dias]`; `agenda.sh marcar` cria **só** na pessoal.
- **Google Cloud:** projeto `maestro-513800`, app em modo teste (usuários de teste: as 3 contas), cliente desktop "Maestro Mac", APIs Gmail + Calendar ligadas. Chaves secretas: Fkff (em uso) e zs9P (ativa, sem cópia; pode apagar). Conectar/reautorizar conta: `scripts/conectar-gmail-extra.sh <apelido|pessoal> [leitura|escrita]` (mostra no fim qual e-mail ficou ligado).
- **Ferramentas desligadas:** computer_use, browser, image_gen, code_execution, delegation, stt (temporário).

### 3.2 Decisões (com o porquê) — detalhes em `descoberta/2026-11-03-04-descoberta-maestro.md`
- Hermes Agent como motor; memória fora do motor (caderno em git/Obsidian). Por quê: multi-IA e legível pelo João.
- WhatsApp com **número próprio** (eSIM), não self-chat. Por quê: self-chat não apita no iPhone.
- Haiku via API (não usar assinatura Claude Pro em ferramenta de terceiros). ChatGPT Plus fica pra depois, com Haiku de reserva.
- **E-mail só leitura e FORA da abertura do dia** (João não usa e-mail no dia a dia): só avisa vencimento, corte, cobrança, segurança, alguém esperando.
- **Agendas do Blanc só leitura**; agenda pessoal é do Maestro, mas cria evento só com pedido/aprovação (escada de autonomia). Blocos de rotina antigos serão refeitos.
- Abertura em dois caminhos (1ª mensagem do dia ou reserva 9h30) porque o João acorda em horários diferentes.
- Segredos: o João cola chave/token direto no terminal; a IA não digita credenciais.
- Fora do escopo: dinheiro/banco (v1), mensagens a terceiros, terapia, namoro, família.

### 3.3 Alterações de 05/11
- Gmail pessoal + Blanc + jpavilabtc ligados (só leitura); scripts `emails.sh`, `conectar-gmail-extra.sh`, `google-somente-leitura.sh`.
- Gateway virou serviço launchd; cron de abertura e cobranças criados e testados (abertura chegou 09:42).
- API do Calendar ativada, conta pessoal reautorizada com agenda; `agenda.sh` criado; SOUL ensinado (e-mail, agenda, estado.md, abertura).
- Achados viraram fios: água Rio+ (R$ 1.018,78, aviso de corte), 7Link, iCloud, boleto Nubank, PUCPR, ar-condicionado do Office (vence 06/11), PRs #43/#44 do SDR com correções pedidas pelo Guga, avaliações do Blanc no Google, Maisa sem resposta.

### 3.4 Pendências
- [ ] **Áudio (STT):** config pronta (local, modelo small, pt). `hermes pm install --extra stt-whisper` falhou por DNS do roteador (files.pythonhosted.org SERVFAIL). Repetir; se der certo, `hermes tools enable stt --platform whatsapp` + reiniciar serviço.
- [ ] Rodar 24h (Mac dormindo pula cobranças): VPS barata, Oracle grátis ou PC do Blanc. Nada na AWS da Regency.
- [ ] Conferir a 1ª cobrança automática (hoje 14h) e ajustar tom/frequência com o João.
- [ ] Apagar a chave secreta zs9P no Google Cloud.
- [ ] Trocar o cérebro pro ChatGPT Plus quando renovar (`hermes auth add openai-codex --no-browser --label chatgpt-plus-joao`), Haiku de reserva.
- [ ] Fios em tabela na nuvem (Supabase) quando sair do Mac.
- [ ] Refazer a rotina da agenda pessoal (apagar blocos antigos) junto com o João.
- [ ] Recarga do eSIM antes de ~04/12.
- [ ] Documento de design (PDF pro João) e plano da v1.
- Ideias futuras: ler conversas do WhatsApp (sessão self-chat guardada em `~/.hermes/whatsapp/session-selfchat-8602-bak`), mandar mensagens que o João pedir, Siri/Atalhos, módulo financeiro seguro (só leitura → lote pra aprovar no app do banco).

### 3.5 Próximo passo
1. Tentar de novo o áudio (STT) quando a rede estabilizar.
2. Ver com o João como foi a cobrança das 14h e ajustar.
3. Decidir onde o Maestro roda 24h.

### 3.6 Outros subsistemas
- ⏸️ Pilar financeiro (parado desde 30/06): `maestro-financeiro/` (painel de extrato). Caminho grátis: arrastar extrato do Nubank no `dashboard_simples.html`.

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
