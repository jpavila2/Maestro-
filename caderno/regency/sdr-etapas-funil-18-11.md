# Etapas do funil do SDR — diagnóstico 18/11/2026

Somente leitura. Repos: CRM `3fe7f38`, implantação Blanc `93e1efa`, plataforma `a5d4b57`. Dados dos 37 leads: `caderno/blanc/crm-leads-10-18-11.md`.

Termos: **SDR** é o robô que conversa no WhatsApp. **Ponte** é a peça que liga o WhatsApp ao CRM. **Etapa** é a coluna do kanban onde o lead está. **Referral** é a informação que a Meta manda quando alguém clica num anúncio para abrir o WhatsApp.

## Por que a etapa não anda

- O robô conversa, mas não muda a etapa. Nenhuma parte do caminho WhatsApp → ponte → CRM mexe na etapa. (`blanc-impl/integracoes/n8n/fluxos/ponte/50-ponte-entrada-para-crm.json:33`)
- Todo lead novo entra como "Novo". (`blanc-impl/implantacoes/blanc-house/kit/lead-blanc-house.sql:137`)
- A etapa só muda quando uma pessoa salva a ficha ou clica em "Recalcular estágios". (`crm/js/comercial.js:1550`, `crm/js/comercial.js:911`)
- A etapa automática olha datas e tipo de orçamento. A conversa não grava essas informações. (`crm/js/core.js:1302-1330`)
- Por isso 26 dos 37 leads continuam em "Novo". Os que saíram foram mexidos por uma pessoa.

**Caso ***3453:** o cliente confirmou degustação para sábado, 21/11, às 17:00. O CRM ficou em "Novo". Para a etapa mudar, alguém precisa colocar a data e o tipo "degustação" na ficha. A ponte não coloca. Além disso, o lead está marcado como "Outro" e "Freelancer", então talvez nem seja festa. (`caderno/blanc/crm-leads-10-18-11.md`, caso ***3453)

## O que existe hoje

- **A IA tem ferramenta para mudar a etapa?** Não. As 9 ferramentas do SDR não mexem em etapa. (`blanc-impl/agentes/sdr/sdr/ferramentas.py:24-58`)
- **Onde mora a mudança?** No CRM, feita por pessoa, no navegador. A ponte não tem como chamar isso. (`crm/js/core.js:737-739`)
- **O que a ponte consegue fazer no CRM?** Só enviar a mensagem recebida. Ler a etapa, mudar a etapa, criar oportunidade e mudar o estado da conversa são "lacunas" do contrato. (`blanc-impl/agentes/sdr/sdr/crm.py:132`, `:163-184`)
- **Existe rota de etapa no CRM?** No CRM Blanc, não. A plataforma genérica tem uma, mas exige login de pessoa, então o robô não usa. (`plataforma/lib/workspace-http.ts:597-606`)
- **Etapas que o CRM tem hoje** (lista fixa no código):
  1. Novo / Qualificação
  2. Qualificado
  3. Orçamento online enviado
  4. Visita agendada
  5. Visita realizada
  6. **Degustação agendada**
  7. **Degustação realizada**
  8. Em negociação
  9. Fechado
  10. Perdido

  Há etapa de degustação (duas). (`crm/js/core.js:496-506`)

## Regras propostas (produto Regency, todos os clientes)

A ideia: etapas e gatilhos viram configuração de cada cliente. Não ficam presos no código do Blanc.

- **Cada cliente tem as suas etapas.** Blanc tem degustação. Uma loja de roupas pode ter "Prova" ou "Reserva". Outro cliente pode não ter visita.
- **Exemplos de gatilhos** (adaptáveis):
  - Orçamento enviado
  - Visita agendada (data e hora confirmadas)
  - Degustação marcada
  - Fechado (sinal pago: a equipe confirma, o robô não fecha sozinho)
  - Perdido (recusa clara do cliente)
- **Regra de ouro:** o robô sugere a mudança com o trecho da conversa que prova. Quem grava é o CRM, com registro de quem mudou, quando, de onde para onde e por quê.

## O que é do Dev e o que é do Guga

**Dev (CRM):**
- Criar uma ação "mudar etapa" que a IA possa chamar, com regra de só avançar (ou voltar só com pessoa).
- Guardar quem mudou, quando, de qual etapa para qual, por qual canal e o motivo. A tabela de histórico já existe: `client_stage_events`.
- Tirar a lista de etapas do código. Guardar por cliente, no banco.
- Mostrar a etapa na ficha do lead.
- Aceitar a origem do lead (ver abaixo).

**Guga (ponte e agente):**
- Detectar o evento na conversa: "cliente confirmou data", "orçamento foi enviado", "recusou".
- Chamar a ação do CRM com o trecho da conversa e o número da mensagem (para não duplicar).
- Não gravar direto no banco. A regra fica no CRM.

## Origem do lead / referral da Meta

- **A ponte já recebe o referral?** Não. Nenhum fluxo do n8n lê esse campo. (`blanc-impl/integracoes/n8n/fluxos/ponte/53-ponte-webhook-whatsapp.json:8`)
- **A ponte repassa algo de origem?** Não. Manda sempre `origin: 'WhatsApp'` e `message: null`. (`.../50-ponte-entrada-para-crm.json:33`)
- **O CRM guarda origem?** Sim, mas grava `origem = 'kit'` fixo ao criar o lead. O valor que a ponte manda é jogado fora. (`blanc-impl/implantacoes/blanc-house/kit/lead-blanc-house.sql:137`)
- **Por que "Meta" aparece zero vezes?** Porque nada grava "Meta" automaticamente. "Meta" é só uma opção de um seletor que a pessoa usa na ficha. (`crm/js/core.js:596`)

**O que o Guga precisa mudar (depois que o Dev aceitar o campo):**
1. No webhook (fluxo 53): ler `referral` da **primeira** mensagem de cada contato.
2. No envio ao CRM (fluxo 50): mandar `referral` junto do lead, só na primeira vez. Campos enxutos:
   - `sourceType`: `ad` (anúncio)
   - `sourceId` e `adId`: número do anúncio
   - `headline`: título do anúncio (até 200 caracteres)
   - `sourceUrl` e `ctwaClid`: opcionais
3. Não enviar o texto da conversa. A decisão de minimização já está tomada.

**Ordem:** primeiro o Dev aceitar o campo. Se o Guga mandar antes, o CRM rejeita.

## Certeza e o que não deu para confirmar

- **Certeza alta:** o robô não muda etapa; a etapa só muda por pessoa ou por recálculo na tela; a origem é fixa `kit`; a ponte não lê referral.
- **Certeza média:** por que cada um dos 26 leads ficou em "Novo" (mecanismo confirmado; não reconsultei o banco).
- **Não confirmado:**
  - Estado exato do registro ***3453 no banco.
  - Se o SQL de implantação é o que está aplicado em produção.
  - Se a migração de reativação de perdido foi aplicada.
  - Como a conversa chega às tabelas do WhatsApp (rota exata dos fluxos 52 e 53).

## Regras aprovadas pelo João em 18/11

Valem para o produto Regency em geral, não só para o Blanc. O diagnóstico acima continua válido: hoje o robô ainda não muda a etapa. O que segue é o combinado e o que já está no CRM, à espera de merge, migration e da ponte.

**Qualificado.** Quando o robô coletar os dados de um lead qualificado (data do evento e os demais campos obrigatórios, configuráveis por cliente), o lead em etapa anterior passa sozinho para "Qualificado".

**Orçamento online enviado.** Quando o orçamento for enviado, pelo robô ou por alguém da equipe (pela aba Conversas/WhatsApp, ou pelo botão de enviar orçamento), o sistema identifica o envio e move o lead para "Orçamento online enviado".

A etapa só avança, nunca volta. Voltar continua sendo só uma pessoa, na tela. Lead perdido ou fechado não anda.

### O que fica no CRM (Dev)

Feito no [PR #46](https://github.com/jpavila2/Blanchouse-crm/pull/46), sem merge e sem deploy. Migration ainda não aplicada (`docs/migration-etapas-avanco.sql`, rollback em `docs/migration-etapas-avanco-volta.sql`).

- Ação `lead.evento.v1` que a ponte chama, com a mesma autenticação do kit. O robô informa o fato (`qualificado` ou `orcamento_enviado`); o CRM decide a etapa.
- No `lead.upsert.v1`, o robô pode mandar `tipoEvento`, `dataEvento` e `convidados`. O CRM preenche só o que estiver vazio (não sobrescreve o que a equipe digitou) e, com todos os obrigatórios preenchidos, qualifica sozinho.
- Config por cliente dos campos obrigatórios de Qualificado (`integracao_config`).
- Botão "Marcar orçamento enviado" na ficha, para a equipe. A regra é a mesma do robô.
- Auditoria em `client_stage_events` (ator robo/equipe/sistema, motivo e trecho opcional).
- O robô não grava direto no banco.

Ordem de merge: primeiro o [PR #45](https://github.com/jpavila2/Blanchouse-crm/pull/45) (origem do lead), depois o #46 rebaseado, depois a reativação de perdido. O merge do #45 e a migration ainda esperam o OK do João.

### O que fica na ponte (Guga)

- Detectar na conversa (1) lead qualificado (campos obrigatórios do cliente coletados) e (2) orçamento online enviado pelo robô.
- Chamar a ação do CRM no formato do PR #46 (`lead.evento.v1`), sem gravar direto no banco. A ponte nunca regride etapa.
- Para a qualificação, também pode mandar os campos no `lead.upsert.v1`; o CRM avança quando eles fecham.
- Os campos são configuráveis por cliente.

O pedido ao Guga, junto com o referral da Meta do PR #45, está na issue [#28](https://github.com/jpavila2/Blanchouse-crm/issues/28).

### Proposta de campos obrigatórios de Qualificado do Blanc (a confirmar com o João)

Base: `campos_qualificacao` do `sdr/blanc-house.json` da implantação.

- **tipo_evento** (tipo de evento)
- **data_evento** (data do evento)
- **convidados** (número de convidados)

O nome do contato não entra: já é coletado na criação do lead, mas não está na lista do SDR. Nesta proposta, a data só conta com o dia completo (`AAAA-MM-DD`); só o mês ainda não qualifica (o robô às vezes pergunta "data ou mês"). Mudar a lista depois é uma linha na config, sem deploy.
