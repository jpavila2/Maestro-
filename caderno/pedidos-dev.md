# Pedidos de programação (fila do Dev)

> Dono: **Dev**. Qualquer bot (ou o João) pede aqui; o Dev despacha para o Claude Code e acompanha.
> Um pedido por bloco, mais novo em cima. Status: 🆕 novo · 🚚 com o Claude Code · 👀 PR pronto para o João · ✅ feito · ⏸️ parado

## Modelo
### (título curto) · 🆕 · pedido por (bot/João) em (data)
- **O quê:**
- **Por quê:** (qual meta isso ajuda)
- **Onde:** (sistema / repositório / pasta)
- **Pronto quando:** (como o João vai ver que funcionou)
- **Histórico:** (data — o que aconteceu)

---

### Visão de detalhe da tarefa e prazo clicável no painel de Entregas · 🆕 · pedido pelo João (via Maestro, ligação 23/11 11h30)
- **O quê:** no painel de Entregas do Regency App, (1) o prazo da linha fica clicável e (2) clicar numa tarefa abre uma visão de detalhe completa (modal ou painel lateral), não só um formulário, de onde dá para ver tudo e editar/salvar.
- **Por quê:** hoje a tarefa só aparece na lista e, depois de criada, não dá para abrir nem ver os detalhes. O prazo também só edita pelo botão "Editar" ou "Pôr prazo".
- **Onde:** `regency-ai/plataforma-modular-agencia`, main em `975175f`. Arquivo principal: `components/deliveries-panel.tsx`. A função `row` (L124–147) mostra o prazo só como um span sem `onClick` (L129: `<span className="deliveries-due...">{due.text}</span>`). A edição já existe, mas só pelo botão "Editar" ou "Pôr prazo" (L134), que abre o form na linha com `<input type="date" name="due">` e Salvar (L140–146). O `save()` (L93–97) faz POST em `/api/workspace/console/task-step` (passo) ou `task-save` (avulsa), com a API em `lib/workspace-http.ts` L967–1013 e as RPCs `agency_console_task_step`, `agency_console_task_plan` e `agency_console_task_save`. A tabela é `agency_console_tasks.due_date` (date), com RLS e escrita só por security definer. Quem é `readOnly` (Sócio) está em `workspace-app.tsx` L548. Atalho opcional no `DeliveriesSummary` do Início (L48).
- **Fazer:**
  1. Clicar no prazo da linha, ou em "sem prazo" quando estiver vazio, abre a edição direto (pode ser `setEditing(key)` ou um input date inline), reaproveitando o `save()` atual. Quem é `readOnly` (Sócio) continua só vendo, sem clique para editar o prazo.
  2. Clicar na própria tarefa abre uma **visão de detalhe completa** (modal ou painel lateral), e não só um formulário. Ela mostra tudo da tarefa: título, cliente ou entrega, se é passo ou avulsa, dono, prazo, status ou conclusão, o que foi feito, detalhes e notas, e datas de criação e atualização, se existirem. Dentro dessa visão dá para editar o que foi feito e os outros campos, e salvar.
  3. Opcional: o mesmo atalho de prazo no `DeliveriesSummary` do Início (L48).
  4. Reaproveitar `save()`, `task-step`, `task-save` e as RPCs atuais. Confirmar o suporte dos campos (notas, done, dono etc.) e, se faltar algum no banco, **avisar antes** de criar migração. Sem API, coluna ou RLS novos a princípio.
  5. O Sócio abre e **vê** o detalhe, mas não edita. A lista atualiza sem F5. Os testes passam.
- **Pronto quando:** clicar numa tarefa abre o detalhe com todas as informações; a edição salva e reflete na lista na hora; o Sócio fica só leitura; os testes passam; o prazo da linha continua clicável como no item 1.
- **Merge:** segue a regra de sempre (testes ok, revisão limpa e nenhum conflito com o que já está publicado). Este bloco não pede merge.
- **Histórico:** 23/11 11h30 — pedido do João por ligação, passado pelo Maestro. Não abri issue com `@claude` em `regency-ai/plataforma-modular-agencia`: o repositório não tem a integração do Claude Code no GitHub (não há workflow `claude.yml`, não há checks do app e o bot nunca comentou issues). Em 15/11 o João deixou o uso do Claude Code pelo terminal (ver o bloco "Ligar o Claude Code ao GitHub" abaixo). A tarefa entra nesta fila para o Dev despachar no CLI.

### Finalizar o SDR do WhatsApp do Blanc · 🆕 · pedido pelo João em 13/11
- **O quê:** terminar o agente que responde o WhatsApp do Blanc e colocá-lo no ar.
- **Por quê:** meta de Black Friday (fechar leads em novembro).
- **Onde:** projeto regency-ai (SDR). Ver `RETOMAR.md` técnico do SDR.
- **Pronto quando:** _o Dev confirma com o João na primeira rotina_.
- **Histórico:** 13/11 — registrado pelo Claude a partir do pedido do João.
  15/11 — Conferência no código: o "digitando" está no código, mas falta confirmar se foi publicado no n8n da VPS (perguntado ao Guga na issue #28 do Blanchouse-crm). O robô ainda não entende áudio nem documentos. O n8n manda `lead.message` vazio. 16/11: perguntei ao João (pelo Maestro) se começo pelo PR do lead.message e depois pelo áudio.

### CRM do Blanc — opção 2 do Hoje (lead novo e orçamento online com "sem resposta há X h") · 👀 PR pronto, aguarda o João · aprovado pelo João em 17/11 11h20
- **Aprovação registrada:** mensagem do Maestro ao Dev em 17/11 11h20: "João aprovou (17/11 11h20): ... implementar a opção 2 da auditoria ... Só em branch e PR, sem merge, sem deploy e sem SQL em produção". O escopo aprovado foi só branch + PR; merge e deploy não foram aprovados.
- **Com o Claude Code:** feito em 17/11 (Sonnet). Branch `claude/hoje-alerta-sem-resposta`, commit f31d168, PR https://github.com/jpavila2/Blanchouse-crm/pull/43 (aberto, sem conflito). Testes 525/528; as 3 falhas já vinham do main. Sem migration. Resumo: /workspace/crm-hoje-alerta-sessao/RESUMO.md.
- **Detalhes:** só entram leads de 17/11 em diante (constante `FOLLOWUP_TOPO_DESDE`), para não jogar ~200 cadências antigas no Hoje. O "sem resposta" conta desde a última ação da equipe, porque o CRM não guarda a mensagem recebida.
- **O que travou:** nada técnico. Falta o OK do João para merge e deploy (deploy só pela pasta do Mac, porque os deploys do GitHub na Vercel saem BLOCKED). O João disse que ia repensar a aba Hoje depois. Não há registro de OK para merge.

### CRM do Blanc — bug do "Fechado" (arrastar com data em conflito deixa o lead inconsistente) · 👀 PR pronto, aguarda o João · aprovado pelo João em 17/11 11h20
- **Aprovação registrada:** a mesma mensagem de 17/11 11h20 ("Junto, corrigir o bug: arrastar para 'Fechado' com a data em conflito ...").
- **Com o Claude Code:** feito em 17/11, no mesmo PR #43 (branch `claude/hoje-alerta-sem-resposta`, f31d168). O conflito é checado antes de qualquer mudança; no conflito nada muda e o usuário recebe aviso. Teste novo: `tests/drop-fechado-conflito.test.mjs`.
- **O que travou:** o mesmo do bloco acima: falta o OK do João para merge e deploy. Se ele quiser o bug sem a mudança do Hoje, o Claude separa num PR próprio.

### CRM do Blanc — diagnóstico da janela de 24h · ✅ diagnóstico entregue · aprovado pelo João em 17/11 11h27
- **Aprovação registrada:** mensagem do Maestro ao Dev em 17/11 11h27: "Mais um item aprovado pelo João (17/11 11h27) ... Só diagnóstico mais branch e PR, sem merge, sem deploy e sem cadastrar template na Meta sem o meu OK".
- **Com o Claude Code:** feito em 17/11. Diagnóstico: o CRM não fala direto com a Meta; põe a mensagem numa fila e a ponte n8n do Guga envia. Quem trava depois de 24h é o próprio CRM (tela, banco e ponte), e não existe envio de template. Arquivos: /workspace/crm-conversas-template-sessao/DIAGNOSTICO.md e PLANO.md. Reenviado ao Maestro em 18/11.
- **O que travou:** nada; o diagnóstico está pronto. O próximo passo é o bloco do template.

### CRM do Blanc — template de retomada · ⏸️ aguarda o João (texto do modelo + OK para a #28) · aprovado pelo João em 17/11 11h27 (só PR)
- **Aprovação registrada:** a mesma de 17/11 11h27, que cobre só diagnóstico, branch e PR. Cadastrar o modelo na Meta precisa de OK separado.
- **Com o Claude Code:** feito em 17/11. Branch `claude/conversas-template-retomada`, commit fa9b9fc, PR https://github.com/jpavila2/Blanchouse-crm/pull/44 (aberto, sem conflito). Botão "Enviar template de retomada" com a janela fechada, desligado até o modelo existir (`TEMPLATE_RETOMADA.nome = null`). Testes 532/535; as 3 falhas já vinham do main. Resumo: /workspace/crm-conversas-template-sessao/RESUMO.md.
- **O que travou:** três coisas, nesta ordem:
  1. João escolher o texto (dois propostos em 17/11: lead sem contrato, categoria marketing, com opção SAIR; cliente com evento contratado, categoria utility) e cadastrar o modelo no WhatsApp Manager (pt_BR). Ninguém cadastrou nem mandou para a Meta.
  2. OK do João para registrar na #28 o pedido ao Guga: a ponte n8n passar a enviar template. Perguntado em 17/11 e de novo em 18/11; sem resposta registrada.
  3. Depois disso, um PR novo no CRM (SQL com o tipo `template` e `handler.mjs` aceitando `template`) e ligar o nome do modelo. Merge e deploy do #44 também precisam do OK do João.

### Melhorias no sistema do Blanc (CRM) · ✅ cardápio escolhido (17/11 11h20); itens abaixo · pedido pelo João em 13/11
- **O quê:** melhorias de sistema, otimização de fluxos, novas possibilidades e correção de bugs (palavras do João, 13/11).
- **Por quê:** apoiar o fechamento de leads e tirar trabalho manual da equipe.
- **Onde:** CRM do Blanc.
- **Primeiro passo:** issue de auditoria com `@claude` (sem alterar código) → o Dev junta com o que o Blanc House viu nos processos → cardápio de até 3 itens para o João escolher.
- **Pronto quando:** cada item escolhido vira issue própria, com PR aprovado pelo João.
- **Histórico:** 13/11 — registrado pelo Claude.
  17/11 — Auditoria feita pelo Claude Code (Haiku, só leitura, sem alterar código): /workspace/blanc-crm-audit/auditoria-17-11.md. Cardápio enviado ao Maestro; aguardando o João escolher.
  17/11 11h20 — João escolheu a opção 2 + o bug do Fechado (via Maestro). 20/11 — virou os blocos "CRM do Blanc — …" abaixo.

### Ligar o Claude Code ao GitHub (CRM e SDR) · ⏸️ · pedido pelo Claude em 13/11
- **O quê:** instalar a integração do Claude Code com o GitHub nos repositórios do CRM e do SDR, usando a assinatura do Claude do João.
- **Por quê:** é por ela que o Dev passa tarefas ao Claude Code sem o João colar nada.
- **Onde:** no Mac do João, com o Claude Code, dentro de cada repositório (`/install-github-app`).
- **Pronto quando:** uma issue de teste com `@claude` recebe resposta do Claude no GitHub.
- **Histórico:** 13/11 — passo do roteiro de domingo.
  16/11 — ⏸️ parado: em 15/11 o João decidiu que o Dev usa o Claude Code pelo terminal (ver SOUL).
