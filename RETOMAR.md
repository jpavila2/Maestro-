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

## 3. Estado atual (ATUALIZAR ao concluir etapas) — última atualização 05/11/2026 — modelo C implementado, ativação pendente

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
- [x] **Modelo C implementado localmente em 05/11:** CRM `api/maestro-compra.js`, RPC transacional em `docs/migration-maestro-compras.sql`, recibo acessível nas compras avulsas e inclusão na lista de despesas. Cliente `scripts/maestro-compra.py` prepara rascunho privado e envia somente com hash conferido, confirmação explícita e ID da aprovação. Regras versionadas em `caderno/compras-modelo-c.md`; SOUL aponta para elas.
- [ ] **Ativar modelo C em produção:** aplicar migration no Supabase; configurar `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` e `MAESTRO_TOKEN` na Vercel; configurar `~/.hermes/maestro-compras.json` (endpoint/token, chmod 600); publicar CRM; cadastrar UUID/data conferidos da festa; validar uma nota aprovada. MCP Supabase recusou consulta por permissão nesta sessão. `vercel env ls production` mostrou somente ANTHROPIC_API_KEY; nenhuma credencial nova foi criada/exposta. Sem acesso SQL não foi possível executar/verificar a migration.
  - Testes: 18 casos Node da rota com HTTP simulado, testes existentes match-comprovante/producao-areas e teste local do cliente (preparar sem rede, modo 600, bloquear rascunho alterado) passaram. Isso não substitui teste SQL/de produção.
  - Foto deduplicada por bytes SHA-256; outra foto/compressão da mesma nota exige conferência humana. Não há editar/apagar/listar clientes nesta API. Service role fica só no servidor. Aprovação é declaração do cliente Maestro, regida pelo fluxo no caderno/SOUL.
  - **As cinco notas reais continuam pendentes** em `caderno/notas-festa-07-11.md`: R$ 1.864,55 bruto, itens pessoais e recibo T&M com dúvidas. Construir a integração não autoriza lançar essas notas.
- [ ] Fios em tabela na nuvem (Supabase) quando sair do Mac.
- [ ] Refazer a rotina da agenda pessoal (apagar blocos antigos) junto com o João.
- [ ] Recarga do eSIM antes de ~04/12.
- [ ] Documento de design (PDF pro João) e plano da v1.
- Ideias futuras: ler conversas do WhatsApp (sessão self-chat guardada em `~/.hermes/whatsapp/session-selfchat-8602-bak`), mandar mensagens que o João pedir, Siri/Atalhos, módulo financeiro seguro (só leitura → lote pra aprovar no app do banco).

### 3.5 Próximo passo
0. Ativar compras modelo C (migration + envs + deploy + UUID da festa), então testar nota especificamente aprovada. Ver `caderno/compras-modelo-c.md`.
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


### Ativação modelo C — atualização de acesso em 05/11
- João autorizou ativação e concessão dos acessos necessários.
- Configurados na Vercel/produção: `MAESTRO_TOKEN` (sensível, gerado aleatoriamente) e `SUPABASE_URL` do CRM. Config privada do cliente salva em `~/.hermes/maestro-compras.json`, modo 600. Token não exibido nem versionado.
- Continua pendente: liberar projeto `scaxbbeygirfzlpskirj` na conexão Supabase (list_projects só retorna Os Animados), validar/aplicar SQL, configurar `SUPABASE_SERVICE_ROLE_KEY` somente na Vercel, publicar e testar. Nenhuma compra real lançada.

### Workshop Faturando com IA — ligação ao Maestro (05/11/2026)
- [x] Fio SDR Blanc atualizado em `caderno/fios.md` com relato atual do João: instalação quase concluída e previsão 06/11, sem ativação confirmada.
- [x] Próximos passos das aulas 04 e 05/11 consolidados em `caderno/workshop-faturando-ia-2026-11.md`: ativação → revisão/resultado → playbook → comercial; backlog com gatilhos.
- O Hermes já lê os fios nas aberturas/cobranças existentes; não foi criado cron/evento nem registrado envio em `estado.md`. Memória global aponta ao caderno. Não confundir memória registrada com lembrete já entregue; execução automática depende do Mac acordado.


### Modelo C — Supabase liberado e migration aplicada (05/11 à noite)
- Conexão correta: Supabase `blanc crm` (link_id `link_6aed305022c08191883df10b2b93c3e2`), projeto `scaxbbeygirfzlpskirj`. As outras conexões podem mostrar só Os Animados.
- Migration `maestro_compras_modelo_c` aplicada. Estrutura real confirmada. RPC security invoker, service_role EXECUTE=true, anon/authenticated=false. Sem triggers nas duas tabelas.
- Teste SQL real em transação: insert, retry com mesmo ID e rejeição de valor diferente passaram; ROLLBACK executado, sem compra persistida. Testes locais 18/18 continuam passando.
- Contrato conferido: Carlos Henrique / Rosa, 07/11/2026, 150 pessoas, UUID `9946f67d-1b53-476f-ac85-d89797fc5a99`.
- Agora falta somente credencial `SUPABASE_SERVICE_ROLE_KEY` na Vercel (ferramenta oferece apenas chaves públicas), deploy e teste autenticado da rota/WhatsApp. Token dedicado e URL já configurados. Usuário deve colar a chave direto no terminal, nunca no chat. Ainda NÃO publicado.
- Auditoria Supabase não apontou a nova função; alertas preexistentes de funções antigas e proteção de senha constam no retorno, fora do escopo desta mudança.

### Sessão Claude 06/11 (madrugada): conta nova e organização
- João abriu 3ª conta Claude Pro (jpavilabtc@gmail.com, teste de 7 dias; vira US$ 20/mês se não cancelar). Na conta nova é preciso religar os conectores do claude.ai: Supabase (organização do "blanc crm"), Vercel, Gmail (conta do Blanc), Google Agenda e Drive (pessoal), Meta Ads.
- Skills e plugins agora moram no Mac (valem pra qualquer conta): `subir-campanha-meta` e `custo-viagem-toro` foram copiadas para `~/.claude/skills`, e o plugin IT Reelsmaker foi instalado localmente (`it-reelsmaker@itparty`). Os plugins Marketing, Productivity, Design e Adspirer quase não eram usados e não serão levados.
- Apagada a máquina virtual do Cowork (`~/Library/Application Support/Claude/vm_bundles`, 11 GB). João não usa o Cowork. O espaço livre subiu de 25 para 36 GB.
- Regency: 6 pastas extras do SDR foram removidas do Mac. Sobraram `plataforma` (main) e `plataforma-sdr-beta` (ver `projetos/regency-ai/RETOMAR.md`).
- Modelo C continua aguardando a `SUPABASE_SERVICE_ROLE_KEY` na Vercel (João cola), o deploy e o teste com uma nota aprovada. As 5 notas da festa de 07/11 foram **lançadas em 06/11** direto no CRM (valor total por nota, R$ 1.864,55; ver `caderno/notas-festa-07-11.md`), então o teste do modelo C vai usar uma nota futura.
- Ideia nova do João (06/11): conversar com o Maestro por voz, de forma fluida (tipo modo voz do ChatGPT), inclusive no carro, passando demandas e ouvindo o andamento. Pontos levantados: Mac na mochila dorme (exige servidor 24h ou Mac em casa), permissões por voz com cerca (branch claude/, nada de push/merge/deploy sem ele), custo de voz ao vivo por minuto. Próximo: pesquisar projetos prontos antes de construir; começo sugerido = resposta em áudio no WhatsApp.
