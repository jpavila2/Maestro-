# WhatsApp administrativo da Blanc e histórico de 6 meses

Levantamento de 18/11/2026 (America/Sao_Paulo). Só leitura: caderno, contexto, GitHub e documentação oficial da Meta. Nada foi alterado, comentado ou enviado.

## 1. Telefone administrativo — o que falta

### O que já está pronto

Método escolhido: **Cloud API da Meta em coexistência com o app WhatsApp Business**, pelo **Cadastro Incorporado (Embedded Signup)**. Não é QR de Evolution/Baileys. O celular continua com o app; as conversas individuais também chegam ao CRM.

O comercial da Blanc (**(21) 98363-1155**, `phone_number_id` `638089982714946`, WABA `664850029332649`) já roda nessa coexistência (entrou originalmente pelo Kommo; a ponte da Regency se inscreveu depois). O administrativo é **outro número**, que ainda não foi conectado. O dígito desse número **não apareceu** nas fontes consultadas.

Passos 1 a 3 da ordem de produção já saíram:

1. Migration `whatsapp-canais` aplicada no Supabase (11/11).
2. CRM [PR #36](https://github.com/jpavila2/Blanchouse-crm/pull/36) no ar: aba Conversas com Comercial | Administrativo e a página `/cadastro-whatsapp.html`.
3. Fluxos 50 a 53 publicados no n8n (12/11 à noite, confirmado no andamento da Matriz em 16/11: travas no ar desde 13/11). Nada do administrativo vai ao robô.

Fontes: [issue #66](https://github.com/regency-ai/regency-ai-info/issues/66) e [CANAL-ADMINISTRATIVO-OPERACAO.md](https://github.com/regency-ai/blanc-house-implantacao/blob/main/docs/CANAL-ADMINISTRATIVO-OPERACAO.md).

A [issue #28](https://github.com/jpavila2/Blanchouse-crm/issues/28) do CRM (pendências de VPS, origem do lead e etapas) **não** trata da conexão do número administrativo.

No caderno local (`/workspace/maestro/caderno`) não havia nota atualizada sobre este fio. O andamento de outubro (`WHATSAPP-ANDAMENTO.md`, 26/10) está atrasado em relação à #66.

### Pendência registrada

- Último comentário da #66 (12/11/2026, 17h53 America/Sao_Paulo, Cypher/Gustavo): falta a **prova do Gustavo** — mandar uma mensagem de teste ao 1155 e ver o robô responder como antes. Só depois o João faria a fase 0. Não achei comentário posterior confirmando essa prova.
- Andamento da Matriz, commit de 16/11/2026 às 10h07 America/Sao_Paulo: *"fluxos e travas no ar desde 13/11; falta o João conectar o número na Meta"*. O comercial seguiu em uso depois disso. Não dá para afirmar, só pela #66, que a prova foi formalizada.

### Passos que faltam do João (fase 0 em diante)

Documento de operação, passo 4. App a usar: **Blanc House CRM**, id `1787928619110544`, portfólio **Blanc house 3**.

**Primeiro passo (concreto):** no celular do número administrativo, conferir que o app é o **WhatsApp Business** (não o WhatsApp comum), versão **2.24.17 ou mais nova**, conta ativa e sem bloqueio. Em seguida, no computador, abrir o app [Blanc House CRM](https://developers.facebook.com/apps/1787928619110544) no painel da Meta → **Torne-se um parceiro** → **Configurador de cadastro incorporado** → **Criar configuração**: *Login do Facebook para Empresas*, variação *Cadastro Incorporado do WhatsApp*. Anotar o `config_id`.

Ordem depois disso:

1. Em **Gerenciar lista de permissão**, liberar o domínio https do CRM: `https://crm-deploy-gamma.vercel.app`.
2. Logado no CRM, abrir `https://crm-deploy-gamma.vercel.app/cadastro-whatsapp.html?config_id=<id>`.
3. **Teste curto:** iniciar o cadastro e **cancelar antes de concluir**. A página deve mostrar o evento `CANCEL`. Se a Meta recusar o app, parar aqui e esperar a análise das issues [#47](https://github.com/regency-ai/regency-ai-info/issues/47)/#48. Nada abaixo é feito.
4. **Cadastro de verdade**, fora do horário de pico, com o celular do administrativo na mão e o app aberto: concluir o fluxo, escanear o QR (ou colar o código que o app mostrar). A página deve mostrar `FINISH`, `waba_id` e `phone_number_id`. **Anotar os dois.** A página não troca o código por token e não grava nada no banco.
5. Preferir uma **WABA própria** para o administrativo (assim o webhook do 1155 não alcança o número novo por acidente). Se a Meta não permitir, usa-se a mesma WABA; as travas dos passos 1 a 3 já cobrem o canal sem cadastro (sem robô).
6. Garantir que o token do usuário de sistema do app alcança a WABA nova (atribuir o ativo no Business Manager). A inscrição do app (`subscribed_apps`) só acontece **depois** dos passos 1 a 3, que já estão no ar.
7. Cadastrar o canal no banco (passo 5 do documento; precisa de sim de sócio e reconferência). Trocar `<phone_number_id>` pelo valor anotado:

```sql
INSERT INTO public.whatsapp_canais(channel_id,nome,tipo,robo,lead_automatico,vincula_contratante)
VALUES('<phone_number_id>','Administrativo','administrativo',false,false,true);
```

8. **Prova sem resposta:** de um telefone de teste, mandar mensagem ao administrativo. A conversa aparece na aba Administrativo; o robô **não** responde; **não** cria lead; nada chega ao SDR; o 1155 segue normal.
9. **Prova com resposta:** responder pela aba (chega no teste, dentro de 24 h); responder pelo Web ou pelo celular (aparece como eco, sem pausar nem chamar o SDR); arquivo com legenda não vai ao SDR; se o telefone de teste for de cliente com contrato, a conversa já vem ligada à ficha.
10. Só depois das duas provas, avisar a equipe (todos os ativos de `crm_equipe` já veem as duas abas).

Preparação útil no celular, se ainda não estiver: perfil comercial completo (nome **Blanc House**, categoria, endereço, horário, site). Avisar a equipe: listas de transmissão do administrativo ficam só leitura; grupos **não** vão ao CRM; WhatsApp para Windows e relógio desconectam (usar o Web).

**Não fazer nunca** neste número nem no 1155: "Adicionar número de telefone" no Gerenciador do WhatsApp, nem `register` / `deregister` / `request_code` / `verify_code`. Isso pode tirar o número do celular ou derrubar o robô do 1155. Para desconectar, usar as Configurações do próprio app no celular.

Sobre o histórico no dia da conexão do **administrativo**: o documento de operação pede **não importar** ("não queremos conversa velha de fornecedor no CRM"). No fluxo da Meta, recusar o compartilhamento quando o app perguntar.

### O que é do Guga

Já feito: publicação dos fluxos 50 a 53 com as travas por canal.

Ainda dele, ou junto com o João:

- Se a prova do 1155 pedida em 12/11 ainda não foi registrada, confirmar que o comercial segue respondendo antes da fase 0.
- Depois do `FINISH`: inscrição do app na WABA nova (`subscribed_apps`), alcance do token, e o `INSERT` do canal (escrita em produção, com sim e reconferência).
- Conferir as duas provas no n8n e no log do SDR (nada do administrativo pode chegar ao robô).
- Se a Meta recusar o Cadastro Incorporado no app da Blanc, retomar a análise de Provedor de Tecnologia (#47).

## 2. Histórico de 6 meses (o que a Viver de IA alega)

A hipótese se confirma na documentação oficial da Meta. Não é um "puxar a qualquer momento": só existe no **onboarding de coexistência** (app WhatsApp Business + Cloud API, via Cadastro Incorporado).

### Como funciona

1. No fluxo, o dono do número confirma no app Business e escolhe se **compartilha o histórico** com o parceiro.
2. O parceiro (Tech Provider ou Solution Partner) tem **24 horas** após o onboarding para pedir a sincronização. Se perder a janela, o número precisa ser desconectado e o fluxo refeito.
3. Pedidos oficiais, uma vez só, em `POST https://graph.facebook.com/<versão>/<phone_number_id>/smb_app_data`:
   - `{ "messaging_product": "whatsapp", "sync_type": "smb_app_state_sync" }` — contatos; chegam no webhook `smb_app_state_sync` (e atualizações futuras de contato também).
   - `{ "messaging_product": "whatsapp", "sync_type": "history" }` — mensagens; chegam no webhook `history`.
4. Se o negócio compartilhou, a Meta envia as mensagens individuais dos **180 dias** anteriores ao onboarding, em três fases (dia 0–1, 1–90, 90–180), em pedaços que podem chegar fora de ordem (`chunk_order`). `progress: 100` indica o fim. Capturar o webhook primeiro e processar depois: um único envio pode trazer milhares de mensagens.
5. Se recusou, chega um `history` com erro **2593109** ("History sync is turned off by the business…").
6. Depois do onboarding, mensagens novas mandadas pelo app ou por aparelho vinculado chegam em `smb_message_echoes` (a ponte da Blanc **já** trata esse eco). Entradas novas seguem no campo `messages`.

Requisitos oficiais:

- App WhatsApp Business **2.24.17 ou mais novo** (não vale o WhatsApp comum).
- Quem conduz o cadastro já é **Solution Partner ou Tech Provider**.
- Webhooks assinados, no mínimo: `messages`, `history`, `smb_app_state_sync`, `smb_message_echoes` (e `account_update` para ciclo de conta).
- Cadastro Incorporado com session logging.
- Avisar o cliente para **manter o app aberto** durante a sincronização (pode levar vários minutos).
- A documentação oficial de onboarding **não lista restrição por país**. Listas antigas de mercados excluídos (algumas citavam o Brasil no lançamento) estão desatualizadas; o teste confiável é o próprio fluxo. Fonte de terceiros, não da Meta: fácil afirmar disponibilidade no Brasil em 2026, mas a fonte a seguir é a página oficial abaixo.

Limites oficiais:

- Só conversas **individuais** (1:1). **Grupos não vêm.**
- Mídia: o recado de histórico não traz o id do arquivo; ids de mídia só chegam à parte, e **só dos 14 dias** anteriores ao onboarding.
- Uma vez só. Para repetir, o cliente precisa desconectar e fazer o cadastro de novo.
- Mensagens temporárias, visualização única e localização ao vivo são desligadas nas conversas individuais. Listas de transmissão ficam só leitura. Chamadas, catálogo e perfil continuam no app, fora da API.
- Número em coexistência: teto fixo de 20 mensagens por segundo.

### O que isso exigiria da nossa ponte (Guga)

Hoje o fluxo 53 só assina `messages` e `smb_message_echoes`. A ponte já grava o eco ao vivo. **Não achei** implementação de `history`, `smb_app_state_sync` nem da chamada `smb_app_data`. A página `/cadastro-whatsapp.html` só mostra o `FINISH` e os ids; **não** troca o código por token e **não** dispara a sincronização.

Para oferecer o mesmo que a Viver de IA no onboarding de um cliente novo, a ponte precisaria:

1. Assinar também `history`, `smb_app_state_sync` e `account_update`.
2. Depois do `FINISH`, em até 24 h: trocar o código por token, inscrever o app e chamar `smb_app_data` duas vezes (contatos, depois histórico), guardando o `request_id`.
3. Receber os webhooks `history`, montar os pedaços por `phase`/`chunk_order`, processar fora da requisição e **deduplicar pelo id da mensagem** (o mesmo recado pode chegar de novo no fluxo ao vivo).
4. Baixar mídia só quando o id vier (14 dias).
5. Regra de produto já anotada em 16/10 e no documento de operação: **não criar lead para todo mundo** do histórico (fornecedor, família, cliente antigo). Anexar conversa só a lead/contrato que já existe; o resto fica de fora ou em fila para curadoria.
6. Tratar a recusa (2593109) sem quebrar o onboarding.
7. Se a sincronização falhar depois de 24 h, o caminho oficial é desconectar e refazer o cadastro — isso precisa estar escrito no playbook, porque no número comercial em produção é operação de risco.

### Situação da Blanc (1155) e do administrativo

O CRM só tem conversas do 1155 **desde 8/11/2026**. Isso combina com a data em que a ponte passou a receber o webhook, não com um import de 180 dias. A janela oficial de 24 h daquele onboarding (ainda no Kommo, depois só inscrição do app da Regency) **já passou**. Para puxar 6 meses do 1155 pelo caminho oficial, seria preciso desconectar e refazer o Cadastro Incorporado — risco para o número que já atende. Não recomendar isso sem um plano de volta e o sim dos sócios.

No administrativo, a decisão já registrada é **não importar**.

### Alternativas

- **Exportar conversa no app** (Configurações → Conversas → Exportar): manual, conversa por conversa, inclusive grupo; não popula o CRM sozinho. Dá para usar como cópia pontual, não como onboarding.
- **Baileys / Evolution / WuzAPI** (QR não oficial): dá para espelhar histórico de uma sessão, mas fere os termos da Meta e arrisca bloqueio do número. A Regency escolheu a Cloud API oficial; não é o caminho a seguir.

### Links (fontes)

Oficiais da Meta:

- [Onboard WhatsApp Business app users (coexistência / Cadastro Incorporado)](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/)
- [history webhook (180 dias, fases, erro 2593109)](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/history)
- [smb_message_echoes](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/smb_message_echoes)

Nossas fontes internas:

- [Issue #66 — canal administrativo](https://github.com/regency-ai/regency-ai-info/issues/66)
- [CANAL-ADMINISTRATIVO-OPERACAO.md](https://github.com/regency-ai/blanc-house-implantacao/blob/main/docs/CANAL-ADMINISTRATIVO-OPERACAO.md)
- [CANAL-ADMINISTRATIVO-DESENHO.md](https://github.com/regency-ai/blanc-house-implantacao/blob/main/docs/CANAL-ADMINISTRATIVO-DESENHO.md)
- [CANAL-ADMINISTRATIVO-PLANO.md](https://github.com/regency-ai/blanc-house-implantacao/blob/main/docs/CANAL-ADMINISTRATIVO-PLANO.md)
- Preparação de 16/10 (ainda útil para custos e mudanças no celular): `/workspace/contexto/agencia-solucoes-ia/piloto/blanc-house/WHATSAPP-COEXISTENCIA.md`
- Página do cadastro no CRM: `https://crm-deploy-gamma.vercel.app/cadastro-whatsapp.html`

O que não foi encontrado: o número exato do WhatsApp administrativo; um "prova do 1155 ok" formalizado na #66 depois de 12/11; implementação na ponte do import de 180 dias; restrição oficial por país na página atual de onboarding.
