# SDR do Blanc: placar de evidência, 1ª amostra (WIA-02)

> Reg · qua 18/11/2026, ~10h40 (Brasília); atualizado no mesmo dia após a conferência do Dev. Fonte: CRM do Blanc (Supabase "BLanc House CRM"), **só leitura e só contagens**, sem nome, telefone nem texto de cliente.
> Janela: 08/11 a 18/11/2026 (manhã). Serve à frente "comercial com evidência" (WIA-04): é a base para, um dia, dizer algo do SDR em proposta. **Ainda não é resultado para mostrar a cliente.**

## Como classifiquei (conferido pelo Dev em 18/11)
Em `whatsapp_mensagens`, na janela da amostra:

- Saída com `source` vazio/nulo e `actor_id` nulo = **robô**. O Dev (18/11, CRM `jpavila2/Blanchouse-crm` `origin/main` `3fe7f38`, só SELECTs agregados) concluiu: **certeza alta** de que não é eco do app (eco = `source = 'business_app'`, 415 mensagens) nem humano da aba Conversas do CRM (46 mensagens com `actor_id` + `request_id` batendo com 46 comandos `send`). **Certeza média-alta** de que é o SDR: o INSERT da ação `message` com `direction='out'` gera exatamente esse par e não marca `source` nem `actor_id`, mas o caller na ponte não foi pregado linha a linha. Template ainda não entra nessa conta.
- `source = business_app` = **equipe pelo app do WhatsApp Business** (eco). Confirmado.
- Saída com `actor_id` = **equipe pelo CRM**. Confirmado.

Os números de robô, equipe pelo app e equipe pelo CRM desta amostra ficam de pé com essa leitura.

## Números da amostra
| Indicador | Valor |
|---|---|
| Conversas no CRM | 113 (59 com mensagem do cliente na janela) |
| Conversas em que o robô respondeu | 43 |
| Conversas com mensagem do cliente e **sem** resposta do robô | 16 |
| Conversas em que a equipe respondeu pelo app | 107 |
| Estado agora (`state`) | **108 em "human"**, 5 em "bot" |
| Pausas do robô | 198 (100 automáticas, sem autor · 98 manuais) |
| "Devolver para IA" manual | 14 |
| 1ª resposta do robô (mediana) | **~16 s** após a 1ª mensagem do cliente |
| 1ª resposta da equipe pelo app, onde o robô não respondeu (mediana) | **~4h40** |
| Mensagens: cliente / robô / equipe pelo app | 488 / 412 / 415 |

Volume por dia (cliente · robô · equipe app): 09/11 52·45·15 · 10/11 107·140·63 · 12/11 71·18·89 · 15/11 35·69·0 · 17/11 57·18·55 · 18/11 (manhã) 36·17·86. Desde 12/11, a equipe pelo app responde mais que o robô na maioria dos dias.

## O que a amostra diz
1. **Velocidade é a evidência mais forte hoje:** ~16 s contra ~4h40. Mas são populações diferentes (conversas com e sem robô); não é comparação limpa de antes/depois.
2. **As 100 pausas sem autor vêm do auto-pause por eco (#104).** Conferência do Dev em 18/11, **certeza alta**: 98 `done` + 2 `cancelled`; as 100 têm um eco `business_app` na mesma conversa em até 2 minutos. No código, o único gerador de `pause` sem `actor_id` (salvo perfil apagado depois, que o cruzamento com o eco torna teórico aqui) é o auto-pause por eco. Ressalva do Dev, que **não muda o placar**: se a Meta devolver como eco uma mensagem do próprio robô, o código também pausa.
3. **Leitura (não é fato além do que o Dev mediu):** das 113 conversas, 108 estão hoje em "human". Com 100 das 198 pausas confirmadas como auto-pause por eco — e não necessariamente takeover humano deliberado —, boa parte dessas 108 "com a equipe" é efeito desse mecanismo. O Dev confirmou a origem das 100 pausas; não contabilizou quantas das 108 conversas em "human" vieram só daí (também houve 98 pausas manuais e 14 "Devolver para IA"). Enquanto o auto-pause por eco estiver assim, o piloto mede pouco o robô.
4. **O funil não fecha pelo CRM:** 103 das 113 conversas não têm mudança de estágio desde 08/11; só 7 chegaram a "orçamento online enviado", 1 a "visita agendada", 1 a "fechado". Sem ligar conversa → cliente → estágio, não dá para medir conversa → visita → comparecimento → fechamento.

## O que falta para virar argumento de venda
- [x] **Dev (18/11):** confirmou a classificação robô/equipe e que as pausas sem autor vêm do eco (#104), nos termos da seção "Como classifiquei".
- [ ] **Dev:** garantir que conversa nova crie/vincule cliente (#106) para o funil aparecer.
- [ ] **João/Blanc:** dizer qual era o tempo de resposta e a taxa de visita **antes** do robô (referência; os "15 atendimentos e baseline" citados no workshop não estão no caderno).
- [ ] Repetir esta contagem na **sex 27/11** (7 dias depois do ajuste da auto-pausa, se sair) e comparar.

## Regra
Nada disto vai para proposta, Minascal ou terceiros antes da revisão de 27/11 e do OK do João. Ganho só depois de medir.
