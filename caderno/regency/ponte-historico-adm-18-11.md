# Ponte (fluxo 52/53): histórico de 6 meses no onboarding do ADMINISTRATIVO da Blanc

Registro de 18/11/2026, 16h56 (America/Sao_Paulo), pedido do João via Maestro.

## Decisão (muda a anterior)

O João **quer** o histórico de 6 meses do telefone administrativo. Isso substitui o "não importar" do documento de operação.
Por isso ele **não conecta o número até a ponte estar pronta**: a Meta só dá 24 h depois do onboarding para pedir a sincronização; perdeu, perdeu (só refazendo o cadastro).

Base técnica: `caderno/regency/whatsapp-adm-e-historico-18-11.md`.

## Dados

- App Meta: Blanc House CRM `1787928619110544`.
- Embedded Signup criado: `config_id` **4547093442231419** (WhatsApp Cloud API).
- Página: https://crm-deploy-gamma.vercel.app/cadastro-whatsapp.html?config_id=4547093442231419
- Supabase do CRM: `scaxbbeygirfzlpskirj`.

## O que a ponte precisa ter (Guga)

1. Assinar os webhooks `history` e `smb_app_state_sync` (além de `messages` e `smb_message_echoes`; `account_update` recomendado).
2. Capturar o `code` do `FINISH` e trocá-lo por token na hora (hoje a página só mostra o `FINISH` e os ids, não troca nem dispara nada). Inscrever o app na WABA (`subscribed_apps`).
3. Em até 24 h do onboarding, chamar `POST /{phone_number_id}/smb_app_data` duas vezes: `sync_type: smb_app_state_sync` (contatos) e `sync_type: history` (mensagens). Guardar o `request_id`. De preferência automático, logo depois do `FINISH`.
4. Receber o `history` primeiro numa fila/tabela bruta e processar depois (pode vir milhares de mensagens, fora de ordem por `phase`/`chunk_order`; fim em `progress: 100`).
5. Gravar mensagens e contatos no Supabase do CRM, no canal Administrativo, **deduplicando pelo id da mensagem**.
6. Não criar lead para todo contato do histórico e nada do administrativo vai ao robô/SDR (travas atuais continuam valendo).
7. Mídia só quando vier o id (só 14 dias); o resto fica como texto.
8. Tratar a recusa (erro `2593109`) sem quebrar.
9. Canal cadastrado em `whatsapp_canais` (robo=false) logo depois do `FINISH`.

## Critério de pronto (quando o João pode conectar)

- [ ] Guga confirma na issue que os itens 1–9 estão no ar no n8n/VPS.
- [ ] Webhooks `history` e `smb_app_state_sync` aparecem assinados no app 1787928619110544.
- [ ] Teste com o próprio payload de exemplo da Meta (ou um número de teste) gravando mensagens e contatos no Supabase sem duplicar e sem chegar ao robô.
- [ ] Existe um jeito de disparar o `smb_app_data` (automático ou manual) e um responsável disponível nas 24 h seguintes à conexão.
- [ ] Tabelas/colunas criadas com o OK do João (sem migration sem "pode").

Só com todos marcados o Maestro avisa o João que pode conectar e **aceitar** o compartilhamento de histórico no app.

## Atenção

- A Meta exige que quem conduz o cadastro seja Tech Provider ou Solution Partner. Se recusar no app da Blanc, volta a análise da issue regency-ai/regency-ai-info#47.
- Grupos não vêm; é uma vez só.
- Nada foi mexido em produção.

Registro na ponte: issue jpavila2/Blanchouse-crm#28.
