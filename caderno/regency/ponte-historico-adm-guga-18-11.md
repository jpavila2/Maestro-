# Texto para o Guga: o que falta na ponte (histórico do administrativo)

18/11/2026, à tarde (America/Sao_Paulo). Pedido do João via Maestro, 16h57.

O CRM adiantou a parte dele na [PR #47](https://github.com/jpavila2/Blanchouse-crm/pull/47) (`POST /api/whatsapp/v1/historico` e `POST /api/whatsapp/v1/smb-app-data`). **A PR não foi mesclada, a migration não foi aplicada e não houve deploy.** Os endpoints só passam a existir em produção depois do OK do João para migration + deploy (pelo Mac; o deploy pelo GitHub deste repositório sai Blocked).

Este texto está pronto para colar na issue da ponte ([#28](https://github.com/jpavila2/Blanchouse-crm/issues/28)). **Ainda não foi publicado.** Só sai depois que o Maestro mostrar ao João.

Base: `caderno/regency/whatsapp-adm-e-historico-18-11.md` e `caderno/regency/ponte-historico-adm-18-11.md`.

---

## Texto para colar

Guga, o João quer o histórico de 6 meses do telefone **administrativo** da Blanc e **não vai conectar o número** até a ponte e o CRM estarem prontos. Se conectar antes, a Meta só dá 24 h para pedir a sincronização; passou, o histórico se perde (só refazendo o cadastro).

A parte do CRM já está desenhada e implementada na PR https://github.com/jpavila2/Blanchouse-crm/pull/47 (ainda sem merge, sem migration aplicada e sem deploy). Abaixo está o que falta na ponte (fluxos 52/53, VPS), com payloads, ordem, critério de pronto e teste.

### Dados

- App Meta: **Blanc House CRM** `1787928619110544`
- Embedded Signup (produto WhatsApp Cloud API): `config_id` **4547093442231419**
- Página: https://crm-deploy-gamma.vercel.app/cadastro-whatsapp.html?config_id=4547093442231419
- Supabase do CRM: `scaxbbeygirfzlpskirj`
- Canal: Administrativo, `robo=false` (nada deste número vai ao SDR)
- HMAC da ponte: o mesmo de hoje (`INTEGRACAO_SEGREDO`), headers `x-agency-timestamp` (10 dígitos, janela de ±300 s) e `x-agency-signature: v1=<hmac_sha256_hex(timestamp + "." + corpo_cru)>`

### O que falta na ponte

1. **Assinar os campos de webhook** no app 1787928619110544: `history`, `smb_app_state_sync` e `account_update` (além dos que já existem, como `messages` e `smb_message_echoes`).
2. No **FINISH** do Embedded Signup (hoje a página só mostra o evento e os ids; não troca token nem dispara nada):
   - trocar o `code` por token na hora;
   - inscrever o app na WABA nova (`POST /{waba_id}/subscribed_apps`);
   - cadastrar o canal em `whatsapp_canais` com `robo=false` (e `lead_automatico=false`, tipo administrativo).
3. **Encaminhar** os eventos `history` e `smb_app_state_sync` para o endpoint da PR, **um webhook por vez**, sem juntar:
   - `POST https://crm-deploy-gamma.vercel.app/api/whatsapp/v1/historico`
   - `Content-Type: application/json`
   - o corpo é o webhook da Meta **como veio** (`object` / `entry` / `changes[]` com `field` `history` ou `smb_app_state_sync`). Se a Meta mandar só o `value` (é o caso do exemplo oficial de recusa 2593109), encaminhe esse `value` mesmo.
   - assine com o HMAC de sempre (`x-agency-timestamp` + `x-agency-signature`).
   - respostas: `200` ok (`declined:true` = o João recusou o histórico no app, erro 2593109 — não é falha da ponte); `202` com `code:"processing_failed"` = o CRM gravou o bruto e o processamento falhou, pode reenviar o mesmo corpo (não duplica); `401` assinatura; `502` o bruto não gravou, reenviar; `503` o CRM ainda não está configurado (migration/env/deploy).
4. **Disparar o `smb_app_data` em até 24 h** depois do onboarding, de preferência **automaticamente, logo depois do FINISH**, via a função da PR (não chamar a Graph direto, para o `request_id` ficar no log do CRM):
   - `POST https://crm-deploy-gamma.vercel.app/api/whatsapp/v1/smb-app-data`
   - mesmo HMAC e `Content-Type: application/json`
   - corpo: `{"phone_number_id":"<id>","sync_types":["smb_app_state_sync","history"]}`
   - o CRM chama a Graph nessa ordem (contatos, depois histórico), uma vez por tipo. Se já houve sucesso, devolve `status:"skipped"` e não repete (a Meta só aceita uma vez; repetir exige offboard).
5. **Tráfego do administrativo longe do SDR**: não criar lead, não mandar mensagem ao fluxo do robô, não tratar histórico como mensagem ao vivo. As travas atuais (`robo=false`) continuam; histórico e contatos não entram no fluxo 52 do robô.

Enquanto a PR #47 não estiver em produção (com a migration aplicada e o `WHATSAPP_CLOUD_TOKEN` na Vercel), os dois endpoints acima respondem 404 ou 503. Dá para deixar o fluxo pronto apontando para essas URLs, mas o teste de ponta a ponta e a conexão do número esperam o OK do João nesse deploy.

### Payloads de exemplo

Pedido para disparar a sincronização (ponte → CRM), logo depois do FINISH:

```json
{
  "phone_number_id": "106540352242922",
  "sync_types": ["smb_app_state_sync", "history"]
}
```

O CRM, por baixo, chama duas vezes:

`POST https://graph.facebook.com/v23.0/{phone_number_id}/smb_app_data`

```json
{"messaging_product":"whatsapp","sync_type":"smb_app_state_sync"}
```

e em seguida:

```json
{"messaging_product":"whatsapp","sync_type":"history"}
```

Resposta de sucesso da Meta (o CRM grava o `request_id`):

```json
{
  "messaging_product": "whatsapp",
  "request_id": "<REQUEST_ID>"
}
```

Webhook de histórico aprovado (encaminhar este corpo para `/api/whatsapp/v1/historico`). Exemplo oficial da Meta: 2 conversas, textos e um `media_placeholder`. Chunks vêm com `phase`, `chunk_order` e `progress`; podem chegar fora de ordem; `progress: 100` é o fim.

```json
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "102290129340398",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "15550783881",
              "phone_number_id": "106540352242922"
            },
            "history": [
              {
                "metadata": {
                  "phase": 0,
                  "chunk_order": 1,
                  "progress": 55
                },
                "threads": [
                  {
                    "id": "16505551234",
                    "context": {
                      "wa_id": "16505551234",
                      "user_id": "US.13491208655302741918"
                    },
                    "messages": [
                      {
                        "from": "15550783881",
                        "id": "wamid.HBgLMTY0NjcwNDM1OTUVAgARGBIyNDlBOEI5QUQ4NDc0N0FCNjMA",
                        "timestamp": "1739230955",
                        "type": "text",
                        "text": {
                          "body": "Here's the info you requested! https://www.meta.com/quest/quest-3/"
                        },
                        "history_context": {
                          "status": "READ"
                        }
                      },
                      {
                        "from": "15550783881",
                        "id": "wamid.QyNUEHBgLMTY0NjcwNDM1OTUVAgARGBI1Rj3NEYxMzAzMzQ5MkEA",
                        "timestamp": "1739230970",
                        "type": "media_placeholder",
                        "history_context": {
                          "status": "PLAYED"
                        }
                      },
                      {
                        "from": "16505551234",
                        "from_user_id": "US.13491208655302741918",
                        "id": "wamid.N0FCNjMAHBgLMTY0NjcwNDM1OTUVAgARGBIyNDlBOEI5QUQ4NDc0",
                        "timestamp": "1739230970",
                        "type": "text",
                        "text": {
                          "body": "Thanks!"
                        },
                        "history_context": {
                          "status": "READ"
                        }
                      }
                    ]
                  },
                  {
                    "id": "12125557890",
                    "context": {
                      "wa_id": "12125557890",
                      "user_id": "US.10293847561029384756"
                    },
                    "messages": [
                      {
                        "from": "15550783881",
                        "id": "wamid.BIyNDlBOEI5N0FCNjMAHBgLMTY0NjcwNDM1OTUVAgARGQUQ4NDc0",
                        "timestamp": "1739230970",
                        "type": "text",
                        "text": {
                          "body": "Thanks for your order! As a thank you, use code THANKS30 to get 30% of your next order."
                        },
                        "history_context": {
                          "status": "DELIVERED"
                        }
                      }
                    ]
                  }
                ]
              }
            ]
          },
          "field": "history"
        }
      ]
    }
  ]
}
```

Webhook posterior de mídia (mesmo `wamid` do placeholder, agora com id; também vai para `/historico`):

```json
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "102290129340398",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "15550783881",
              "phone_number_id": "106540352242922"
            },
            "messages": [
              {
                "from": "16505551234",
                "from_user_id": "US.13491208655302741918",
                "id": "wamid.QyNUEHBgLMTY0NjcwNDM1OTUVAgARGBI1Rj3NEYxMzAzMzQ5MkEA",
                "timestamp": "1738796547",
                "type": "image",
                "image": {
                  "caption": "Black Prince echeveria",
                  "mime_type": "image/jpeg",
                  "sha256": "3f9d94d399fa61c191bc1d4ca71375a035cd9b9f5b1128e1f0963a415c16b0cc",
                  "id": "24230790383178626"
                }
              }
            ]
          },
          "field": "history"
        }
      ]
    }
  ]
}
```

Recusa do histórico (erro 2593109). O exemplo oficial da Meta vem **sem** o envelope `object/entry`. Encaminhe como veio; o CRM responde 200 com `declined:true` e não cria conversa.

```json
{
  "messaging_product": "whatsapp",
  "metadata": {
    "display_phone_number": "15550783881",
    "phone_number_id": "106540352242922"
  },
  "history": [
    {
      "errors": [
        {
          "code": 2593109,
          "title": "History sync is turned off by the business from the WhatsApp Business App",
          "message": "History sync is turned off by the business from the WhatsApp Business App",
          "error_data": {
            "details": "History sharing is turned off by the business"
          }
        }
      ]
    }
  ]
}
```

Webhook de contato (`smb_app_state_sync`, também para `/historico`):

```json
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "102290129340398",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "15550783881",
              "phone_number_id": "106540352242922"
            },
            "state_sync": [
              {
                "type": "contact",
                "contact": {
                  "full_name": "Pablo Morales",
                  "first_name": "Pablo",
                  "phone_number": "16505551234",
                  "user_id": "US.13491208655302741918"
                },
                "action": "add",
                "metadata": {
                  "timestamp": "1739321024"
                }
              }
            ]
          },
          "field": "smb_app_state_sync"
        }
      ]
    }
  ]
}
```

Fontes: [history](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/history), [smb_app_state_sync](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/smb_app_state_sync) e [onboarding / smb_app_data](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/).

### Ordem dos passos

1. Assinar no app os campos `history`, `smb_app_state_sync` e `account_update`.
2. Deixar o fluxo 52/53 pronto: FINISH → token + `subscribed_apps` + cadastro do canal (`robo=false`) → chamada imediata a `/api/whatsapp/v1/smb-app-data` → encaminhamento de `history` e `smb_app_state_sync` para `/api/whatsapp/v1/historico`. Nada disso entra no SDR.
3. Esperar o OK do João para aplicar a migration da PR #47, colocar o `WHATSAPP_CLOUD_TOKEN` na Vercel e publicar o CRM (pelo Mac). Sem isso os endpoints não existem em produção.
4. Só então o João conecta o número na página de cadastro, **aceita** o compartilhamento de histórico no WhatsApp Business e deixa o app aberto enquanto sincroniza.
5. A ponte dispara o `smb_app_data` na hora do FINISH (dentro das 24 h) e vai gravando o que a Meta mandar.
6. Conferir no Supabase: mensagens e contatos no canal Administrativo, sem duplicar, sem lead novo e sem nada no robô.

### Critério de pronto (quando o João pode conectar e aceitar o histórico)

Todos os itens abaixo:

- [ ] Campos `history`, `smb_app_state_sync` e `account_update` assinados no app 1787928619110544.
- [ ] Fluxo do FINISH no ar: troca do `code`, `subscribed_apps`, canal `robo=false`, disparo automático do `smb-app-data`.
- [ ] Encaminhamento dos webhooks para `/api/whatsapp/v1/historico` com o HMAC, um evento por vez.
- [ ] PR #47 em produção, com a migration aplicada e o `WHATSAPP_CLOUD_TOKEN` na Vercel — **só com OK do João**.
- [ ] Teste (payload oficial ou número de teste) gravou mensagens/contatos no Supabase **sem duplicar** e **sem chegar ao robô**.
- [ ] Alguém de plantão nas 24 h seguintes à conexão.

Com tudo marcado, o João pode conectar e aceitar o histórico no app.

### Plano de teste

1. **Payload de exemplo (sem conectar o número de verdade).** Depois do deploy da PR #47, mandar para `/api/whatsapp/v1/historico` (com HMAC) o JSON oficial de histórico aprovado e o de contato, acima. Esperado: 2 conversas e 4 mensagens no canal `106540352242922` (ou o `phone_number_id` do payload), `unread=0`, sem linha nova em `clients`, nenhum comando para o SDR. Reenviar o mesmo corpo não duplica. Mandar o JSON de recusa 2593109 devolve `declined:true` e não cria conversa. Mandar o webhook de mídia atualiza o placeholder do mesmo wamid.
2. **Número de teste (se houver um WhatsApp Business de laboratório, não o administrativo da Blanc).** Rodar o cadastro na página, aceitar o histórico, ver o FINISH disparar o `smb-app-data` e os webhooks chegarem ao CRM dentro da janela. Conferir o `request_id` em `whatsapp_smb_sync_log` e as mensagens em `whatsapp_mensagens`. Nada no fluxo do robô.
3. **No dia da conexão real:** o administrativo de produção só entra quando o critério de pronto estiver completo. O João aceita o histórico no app e fica alguém de plantão.

### Atenção (limites da Meta)

- Quem conduz o cadastro precisa ser **Tech Provider** ou **Solution Partner**. Se o app da Blanc for recusado, volta a análise da issue [regency-ai/regency-ai-info#47](https://github.com/regency-ai/regency-ai-info/issues/47).
- Conversas de **grupo não vêm**.
- O sync é **uma vez só** por tipo (`smb_app_state_sync` e `history`). Repetir exige offboard e novo cadastro.
- O **id de mídia vale 14 dias**; o resto do histórico chega como placeholder, sem arquivo.
- Pedido em até **24 h** depois do onboarding; depois disso a Meta não entrega mais o histórico.

Qualquer dúvida, responde nesta issue. Não conectar o número administrativo antes do critério de pronto.
