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

### Finalizar o SDR do WhatsApp do Blanc · 🆕 · pedido pelo João em 13/11
- **O quê:** terminar o agente que responde o WhatsApp do Blanc e colocá-lo no ar.
- **Por quê:** meta de Black Friday (fechar leads em novembro).
- **Onde:** projeto regency-ai (SDR). Ver `RETOMAR.md` técnico do SDR.
- **Pronto quando:** _o Dev confirma com o João na primeira rotina_.
- **Histórico:** 13/11 — registrado pelo Claude a partir do pedido do João.
  15/11 — Conferência no código: o "digitando" está no código, mas falta confirmar se foi publicado no n8n da VPS (perguntado ao Guga na issue #28 do Blanchouse-crm). O robô ainda não entende áudio nem documentos. O n8n manda `lead.message` vazio. 16/11: perguntei ao João (pelo Maestro) se começo pelo PR do lead.message e depois pelo áudio.

### Melhorias no sistema do Blanc (CRM) · ⏸️ (aguarda escolha do João) · pedido pelo João em 13/11
- **O quê:** melhorias de sistema, otimização de fluxos, novas possibilidades e correção de bugs (palavras do João, 13/11).
- **Por quê:** apoiar o fechamento de leads e tirar trabalho manual da equipe.
- **Onde:** CRM do Blanc.
- **Primeiro passo:** issue de auditoria com `@claude` (sem alterar código) → o Dev junta com o que o Blanc House viu nos processos → cardápio de até 3 itens para o João escolher.
- **Pronto quando:** cada item escolhido vira issue própria, com PR aprovado pelo João.
- **Histórico:** 13/11 — registrado pelo Claude.
  17/11 — Auditoria feita pelo Claude Code (Haiku, só leitura, sem alterar código): /workspace/blanc-crm-audit/auditoria-17-11.md. Cardápio enviado ao Maestro; aguardando o João escolher.

### Ligar o Claude Code ao GitHub (CRM e SDR) · ⏸️ · pedido pelo Claude em 13/11
- **O quê:** instalar a integração do Claude Code com o GitHub nos repositórios do CRM e do SDR, usando a assinatura do Claude do João.
- **Por quê:** é por ela que o Dev passa tarefas ao Claude Code sem o João colar nada.
- **Onde:** no Mac do João, com o Claude Code, dentro de cada repositório (`/install-github-app`).
- **Pronto quando:** uma issue de teste com `@claude` recebe resposta do Claude no GitHub.
- **Histórico:** 13/11 — passo do roteiro de domingo.
  16/11 — ⏸️ parado: em 15/11 o João decidiu que o Dev usa o Claude Code pelo terminal (ver SOUL).
