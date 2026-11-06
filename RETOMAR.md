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

## 3. Estado atual (ATUALIZAR ao concluir etapas) — última atualização 05/11/2026 — áudio validado no WhatsApp

### 3.1 O que está RODANDO agora (Maestro = agente pessoal no WhatsApp)
- **Motor:** Hermes Agent v0.22.7 em `~/.hermes` (comando `~/.local/bin/hermes`). Cérebro: **GPT‑6.1 Sol (`gpt-6.1-sol`) pelo ChatGPT Plus**, provedor Hermes `openai-codex`, autenticação OAuth própria do Hermes (label `chatgpt-plus-joao`). Usa a franquia da assinatura; não é API OpenAI paga por chave. Sem fallback automático para Claude/API paga.
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
- **Ferramentas desligadas:** computer_use, browser, image_gen, code_execution, delegation. STT habilitado no WhatsApp: Whisper local `small`, português, sem API paga de áudio.

### 3.2 Decisões (com o porquê) — detalhes em `descoberta/2026-11-03-04-descoberta-maestro.md`
- Hermes Agent como motor; memória fora do motor (caderno em git/Obsidian). Por quê: multi-IA e legível pelo João.
- WhatsApp com **número próprio** (eSIM), não self-chat. Por quê: self-chat não apita no iPhone.
- **Atualizado 05/11:** ChatGPT Plus via OAuth `openai-codex` é o cérebro principal. Haiku via API foi substituído. A ideia anterior de Haiku de reserva foi retirada do caminho automático para evitar cobrança; credencial antiga preservada apenas para eventual rollback manual. Auxiliares em `auto` seguem o provedor explícito; `fallback_providers: []`, sem `fallback_model` legado.
- **E-mail só leitura e FORA da abertura do dia** (João não usa e-mail no dia a dia): só avisa vencimento, corte, cobrança, segurança, alguém esperando.
- **Agendas do Blanc só leitura**; agenda pessoal é do Maestro, mas cria evento só com pedido/aprovação (escada de autonomia). Blocos de rotina antigos serão refeitos.
- Abertura em dois caminhos (1ª mensagem do dia ou reserva 9h30) porque o João acorda em horários diferentes.
- Segredos: o João cola chave/token direto no terminal; a IA não digita credenciais.
- Fora do escopo: dinheiro/banco (v1), mensagens a terceiros, terapia, namoro, família.

### 3.3 Alterações de 05/11
- **10h55 — troca do cérebro:** login por código de dispositivo ativado pelo João; Hermes autenticado no ChatGPT. Catálogo consultado ao vivo e `gpt-6.1-sol` escolhido. Testes locais de resposta e leitura do caderno concluídos; serviço reiniciado, log confirma modelo novo e WhatsApp conectado. Ainda falta o João validar uma conversa real pelo WhatsApp. Backup privado da configuração/autenticação: `~/.hermes/backups/maestro-codex-20261105-105256/` (não versionar segredos).
- Gmail pessoal + Blanc + jpavilabtc ligados (só leitura); scripts `emails.sh`, `conectar-gmail-extra.sh`, `google-somente-leitura.sh`.
- Gateway virou serviço launchd; cron de abertura e cobranças criados e testados (abertura chegou 09:42).
- API do Calendar ativada, conta pessoal reautorizada com agenda; `agenda.sh` criado; SOUL ensinado (e-mail, agenda, estado.md, abertura).
- Achados viraram fios: água Rio+ (R$ 1.018,78, aviso de corte), 7Link, iCloud, boleto Nubank, PUCPR, ar-condicionado do Office (vence 06/11), PRs #43/#44 do SDR com correções pedidas pelo Guga, avaliações do Blanc no Google, Maisa sem resposta.

### 3.4 Pendências
- [x] **Áudio (STT), configuração e teste local:** extra `stt-whisper` instalado, modelo `small` baixado, português, ferramenta habilitada no WhatsApp e gateway reiniciado. Teste real de OGG/Opus retornou exatamente a frase em português (provedor `local`).
- [x] **Áudio real recebido e processado em 05/11 às 13h13:** mensagem de voz do João (3,9 s) recebida pelo WhatsApp, transcrita localmente em português; log registra resposta gerada às 13h14 (19,5 s no total). João confirmou neste chat que recebeu a resposta no WhatsApp: teste ponta a ponta concluído. Primeiro processamento local pode demorar para carregar o modelo.
- [ ] Rodar 24h (Mac dormindo pula cobranças): VPS barata, Oracle grátis ou PC do Blanc. Nada na AWS da Regency. **05/11: João adiou** (o Mac é MacBook e sai com ele; servidor fica pra depois). Recomendação registrada: Oracle grátis; PC do Blanc descartado por privacidade.
- [ ] Conferir a 1ª cobrança automática (hoje 14h) e ajustar tom/frequência com o João.
- [ ] Apagar a chave secreta zs9P no Google Cloud.
- [x] Trocar o cérebro pro ChatGPT Plus: OAuth conectado, `gpt-6.1-sol`/`openai-codex` configurado; gateway reiniciado e WhatsApp reconectado. Sem fallback automático ao Haiku.
- [ ] **Maestro lançar compras da festa no CRM do Blanc (modelo C). João vai fazer pelo GPT (Codex).** Desenho proposto em 05/11 (não aprovado ainda, nada mexido no CRM):
  - Notas de 05/11 já lidas: `caderno/notas-festa-07-11.md` (5 notas, R$ 1.864,55, pendências ⚠️ de itens pessoais e do recibo T&M). SOUL já manda o Maestro registrar toda nota por festa.
  - CRM (`projetos/blanc-house/crm`): compras ficam em `contract_purchases` (chave `contract_id`; tela "Compras avulsas" mostra `category='Mercado'`). Insert do front: `js/producao.js:2295` → `savePurchase` `js/core.js:659`. Fluxo completo com nota = Financeiro › Lançar destino Festa (`confirmarDespesa`, `js/comprovantes.js:678`): grava `status='comprado'`, `purchase_date`, `comprovante_id` (tabela `comprovantes` + bucket privado `comprovantes`, caminho `<sha256>.jpg`). Contrato: `contracts` (`client_name`, `event_date`, `status<>'cancelado'`).
  - Risco: RLS `authenticated_contract_purchases` é FOR ALL pra qualquer logado; por isso NÃO dar login do CRM ao Maestro.
  - Proposta: rota Vercel no CRM (ex.: `api/maestro-compra.js`) com service role só no env da Vercel (João cola), protegida por `MAESTRO_TOKEN` próprio; só INSERE compra + comprovante (sem editar/apagar/ler clientes), deduplica por hash da foto. Maestro só chama depois do "pode lançar" do João.
- [ ] Fios em tabela na nuvem (Supabase) quando sair do Mac.
- [ ] Refazer a rotina da agenda pessoal (apagar blocos antigos) junto com o João.
- [ ] Recarga do eSIM antes de ~04/12.
- [ ] Documento de design (PDF pro João) e plano da v1.
- Ideias futuras: ler conversas do WhatsApp (sessão self-chat guardada em `~/.hermes/whatsapp/session-selfchat-8602-bak`), mandar mensagens que o João pedir, Siri/Atalhos, módulo financeiro seguro (só leitura → lote pra aprovar no app do banco).

### 3.5 Próximo passo
1. Garantir funcionamento com o João fora (Mac acordado; depois decidir hospedagem 24h). Áudio real do WhatsApp já recebido/transcrito e resposta gerada.
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
