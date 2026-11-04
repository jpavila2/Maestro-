# Descoberta do Maestro (agente pessoal) — sessões de 03 e 04/11/2026

> Conversa de consultoria João + Claude para definir o agente pessoal "Maestro".
> Fase: **descoberta** (nada construído ainda). Próximo: comparação de ferramentas → documento de design → plano.
> Regra: toda decisão com o porquê e a alternativa descartada.

## 1. Para que serve (nas palavras do João)
Organizar a cabeça de um empresário de vários negócios com TDAH. O fio não se perde enquanto ele faz as coisas: se perde **entre** elas
(sai pra almoço, abre 3–5 chats, chegam demandas novas e a importância das antigas apaga). Exemplo real: reestruturação do CRM
(P1–P8 GPT↔Claude) parou no P3.

**Régua de sucesso (João, 04/11):** "abrir o Maestro e me direcionar pra viver o meu dia através dele, ver ele fazendo as coisas por mim,
economizando tempo e dinheiro, fazendo análises que às vezes eu nem sabia que eram necessárias, me cobrando as demandas e ajudando
do início ao fim."

## 2. Escopo
- **Dentro:** Blanc House, Turma Animada, Os Animados, Regency AI, finanças pessoais, casa (reformas, mudança, projetos).
- **Fora:** terapia, namoro ("mozão"), família — João pediu pra não mexer.
- João = **cliente zero da Regency**: o que o Maestro aprende vira playbook vendável.

## 3. Comportamentos decididos
| Decisão | Por quê | Descartado |
|---|---|---|
| **Abertura do dia**: tipo de dia (Blanc presencial / casa seg-qua / rua de compras), pendências de ontem, o que vem (festas, pagamentos, compras, prazos), em ordem de prioridade | É o momento em que o João precisa de direção | Só listar sem ordenar |
| **Cobrar, não só lembrar**: fio fica aberto até "feito / adia pra X / desisti". Sem resposta → cobra de novo. Pergunta "que horas você resolve?" e volta na hora | Lembrete é ignorável; o que funcionou na vida dele foi alguém que lembrava **e cobrava** | Notificação simples |
| Chega com o **primeiro passo pronto** e executa com aprovação (inclusive código pelo chat) | Tirar trabalho da frente, não só apontar | — |
| **Autonomia em escada**: fora da 1ª versão (dinheiro, banco; pode *preparar* ex. lista dos extras de terça) → pede aprovação (padrão) → faz e avisa (após várias aprovações sem alteração) | João: "não deixaria pagamentos nem entrar no banco *a princípio*; o resto, o que eu aprovar" | Autonomia total desde o início |
| **Dinheiro NÃO é "nunca" (João, 04/11)**: desenvolver no futuro um módulo financeiro **seguro** que economize o tempo dele (ex.: pagamentos de terça). Direção sugerida pelo Claude: 1º só leitura (extrato/conciliação) → 2º Maestro prepara o lote (nome, valor, PIX) e João autoriza no app do banco com a senha/2FA dele → só depois discutir limites pré-aprovados | Pagamentos de terça + dia 30 levam horas; segurança vem da estrutura (o banco pede a confirmação do João), não da promessa do agente | "Nunca mexe em dinheiro" (versão anterior desta decisão) |
| **Olho de processo**: detecta o que se repete e propõe assumir | Pedido explícito do João | — |
| Incômodo se ajusta conversando com ele | Pior resultado é o João parar de usar | — |

## 4. Canais
| Decisão | Por quê | Descartado |
|---|---|---|
| Rua: **WhatsApp com chip próprio do Maestro** (contato fixado) — a confirmar na escolha da ferramenta | João não usa Telegram ("canal que não abre é canal morto"); chip próprio isola risco de ban do número dele/do Blanc | Telegram (1ª sugestão do Claude, revista); app próprio (mais um projeto pra terminar) |
| **Número do Maestro**: comprar um número só pra ele (chip/eSIM pré-pago), sem mensalidade. Rodar no app WhatsApp Business no próprio celular do João (2º número) e conectar ao Hermes como "aparelho conectado". O Maestro lembra a recarga mínima que a operadora exige pra não desativar a linha | João quer "só o número, que não caia, sem pagar por mês". Nenhum número é 100% à prova de bloqueio no WhatsApp não oficial; o à prova de bloqueio é a API oficial da Meta (plano B) | Reaproveitar chip que outras pessoas ainda usam (o Maestro veria essas mensagens) |
| Assinaturas do João: **Claude Pro (US$20) + ChatGPT Plus (US$20)** → IA do Hermes pelo login do ChatGPT Plus (custo extra ~0, segundo a doc do Hermes); Claude Pro segue pro trabalho no computador | Claude Pro não pode alimentar Hermes/OpenClaw | API paga do Claude (fica como alternativa) |
| Escritório: computador (Claude Code / Codex) | Ele já trabalha ali | — |
| "Me ligar": entendido como mensagem insistente; ligação real possível mas custa mais | Palpite, a confirmar | — |

## 5. Memória única (recomendação, a fechar com a pesquisa)
- **Caderno** (quem é, como cada negócio funciona, pessoas, decisões + porquê): pasta markdown em git, **legível pelo João no Obsidian** (ele quer poder acessar). Qualquer IA lê.
- **Fios** (o que, quando, status): tabela na nuvem (provável Supabase), porque a cobrança das 8h roda com o Mac fechado.
- **Agenda Google** = o "quando".
- Requisito do João: **global, multi-agente, multi-LLM** (Claude Code, Codex, DeepSeek...). Memória só do Claude não basta.

## 6. Agendas
- Agendas do Blanc (blanchousecasadefesta "VISITA", blancofficeeventos): **Maestro só lê**. Vendedoras alimentam.
- Agenda pessoal do João: **passa a ser do Maestro** (marca/remarca). A rotina antiga em blocos (Leads, Dev, Financeiro…) será **zerada na fase de construção**.
- Turma Animada, Animados e Regency entram conversando ("festa da Turma sábado 15h") → evento + fios (confirmar monitores etc.).

## 7. Custo
Decidir a solução primeiro, preço depois — mas com teto realista: **US$ 100/mês é caro**.

## 8. O que já existe (levantamento 04/11)
- **Nenhum agente rodando.** OpenClaw: só código clonado em `lab/openclaw`, nunca instalado. Hermes: não instalado. `maestro/` parado desde 30/06 (só painel de extrato).
- **Aproveitável:** `~/.agents/AGENTS.md` + `~/.claude/memory/` (embrião da memória); rotina agendada `lembrete-whatsapp-blanc-crm` (seg/qua/sex 9h) = embrião da cobrança;
  CRM Blanc (Supabase `scaxbbeygirfzlpskirj`): `contracts` (39 festas futuras), regras de pagamento em `js/fin-calc.js` (`proximaTerca`, `folhaDoMes`), orçamentos parados;
  proposta "Maestro pra TDAH" de 22/09 em `~/.claude/memory/financas_pessoais_joao.md` (1 número/dia, alerta D-3 de vencimento, ritual de domingo).
- **Os RETOMAR.md espalhados pelos projetos já são o caderno de fios** — o Maestro pode lê-los toda manhã.
- **Lacunas:** Turma Animada sem sistema (festas/monitores) — talvez vire produto pra locadores; prazos da Regency em prosa em 3 lugares;
  sistema dos Animados existe e roda (João) — localizar (`os-animados/sistema`, Supabase `jlmoplffuicjnlkrbada`, ou Matriz do Gustavo).
- **Obsidian:** não salva nada automaticamente; parado desde 09/10.
- **Maestri** (app de canvas pra agentes): complemento de mesa, não é o Maestro; exige macOS 26.2 (Mac do João está no 15).
- Segurança: chave Pluggy em `banco-mcp-integrador/config.json` protegida por `.gitignore` na raiz (04/11; nunca tinha sido commitada).

## 9. Fios abertos encontrados (viram a lista de demandas; João vai triando)
- Finanças pessoais: fatura Sicoob (05/10) e IPVA (19/10) sem registro de pagamento — **João conferir**.
- CRM Blanc: reestruturação P1–P8 parada; P3 respondido pelo GPT em 16/10, espera decisões do João (`crm/docs/auditoria/respostas/P3-gpt.md`).
- Pixel Meta do Blanc (regra duplicada): **não aplicado** (João confirmou).
- Regency: atualizar posicionamento como "aprovado na reunião de 03/11" + registrar na central do Guga (PR #12).
- ~~Proposta Clube Novo Rio~~ — **enviada** (João, 04/11).
- Demais: ver `RETOMAR.md` de cada projeto (vja, turma-animada, os-animados, campanha-kelaine, moura-experience, financas-joao, estrategia-ugc…).

## 10. Recomendação de consultor
Maior risco = repetir o P3 de 8. **Primeira versão pequena, rodando em poucos dias: só abertura do dia + cobrança de fios no WhatsApp.**
O resto entra em fatias, cada uma só depois da anterior funcionar.

## 11. Próximos passos
- [x] Descoberta: rotina, cobrança, canais, autonomia, memória, escopo, régua de sucesso
- [x] Levantamento do que já existe
- [x] Pesquisa de ferramentas prontas → `descoberta/motor-do-maestro.html` (artifact: https://claude.ai/artifact/Jq3kCzq86QRRj6z9za5Wfx). Recomendação: Hermes Agent em VPS + WhatsApp chip próprio + memória fora do motor (git/Obsidian + Supabase). Proposto teste de 1 dia.
- [ ] Escolher ferramenta + onde roda 24/7 + teto de custo
- [ ] Documento de design (PDF pro João) + revisão
- [ ] Plano da 1ª versão e construção

## 12. Decisões e ideias de 04/11 (tarde)
| Decisão | Por quê | Descartado |
|---|---|---|
| **Teste no modo "comigo mesmo"** (Hermes ligado ao WhatsApp **pessoal** do João como aparelho vinculado; conversa no chat "Você"). Nunca no WhatsApp do Blanc | Grátis e imediato, sem chip. Risco de ban baixo (só fala com ele mesmo) | Comprar eSIM já (vira plano B se as mensagens não apitarem); número virtual BRDID (mensalidade, verificação por ligação; guardar pra Regency/clientes na API oficial) |
| Teste do teste: **as mensagens do Maestro apitam no iPhone?** Se chegarem caladas → eSIM pré-pago próprio | Cobrança que não chama atenção vira lembrete ignorável | — |
| João **aceita** que o Maestro tenha a chave do WhatsApp dele | Quer que, aos poucos, ele mande mensagens que o João pedir, aponte o que precisa ser respondido e anote festas a partir das conversas | — |

**Ideias pro futuro (subir aos poucos, sempre com aprovação):**
- Mandar mensagens no WhatsApp que o João pedir (escada de autonomia).
- Triagem: "estas conversas estão esperando resposta sua".
- Anotar festas/compromissos a partir das conversas (cuidado LGPD com dados de clientes).
- Integração com a Siri / Atalhos do iPhone (ex.: despertador dispara a abertura do dia).
