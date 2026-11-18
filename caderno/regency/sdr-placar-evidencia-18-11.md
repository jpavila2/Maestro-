# SDR do Blanc: placar de evidência, 1ª amostra (WIA-02)

> Reg · qua 18/11/2026, ~10h40 (Brasília). Fonte: CRM do Blanc (Supabase "BLanc House CRM"), **só leitura e só contagens**, sem nome, telefone nem texto de cliente.
> Janela: 08/11 a 18/11/2026 (manhã). Serve à frente "comercial com evidência" (WIA-04): é a base para, um dia, dizer algo do SDR em proposta. **Ainda não é resultado para mostrar a cliente.**

## Como classifiquei (premissa a confirmar pelo Dev)
Em `whatsapp_mensagens`: saída com `source` vazio e sem `actor_id` = **robô**; `source = business_app` = **equipe pelo app do WhatsApp Business**; saída com `actor_id` = **equipe pelo CRM**. Se essa leitura estiver errada, os números de robô mudam.

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
2. **O robô está pausado em quase tudo:** 108 de 113 conversas estão com a equipe. As 100 pausas sem autor batem com a auto-pausa no eco do WhatsApp (issue #104 da plataforma). *Hipótese, a verificar pelo Dev.* Enquanto isso valer, o piloto mede pouco o robô.
3. **O funil não fecha pelo CRM:** 103 das 113 conversas não têm mudança de estágio desde 08/11; só 7 chegaram a "orçamento online enviado", 1 a "visita agendada", 1 a "fechado". Sem ligar conversa → cliente → estágio, não dá para medir conversa → visita → comparecimento → fechamento.

## O que falta para virar argumento de venda
- [ ] **Dev:** confirmar a classificação robô/equipe acima e se as pausas sem autor vêm do eco (#104).
- [ ] **Dev:** garantir que conversa nova crie/vincule cliente (#106) para o funil aparecer.
- [ ] **João/Blanc:** dizer qual era o tempo de resposta e a taxa de visita **antes** do robô (referência; os "15 atendimentos e baseline" citados no workshop não estão no caderno).
- [ ] Repetir esta contagem na **sex 27/11** (7 dias depois do ajuste da auto-pausa, se sair) e comparar.

## Regra
Nada disto vai para proposta, Minascal ou terceiros antes da revisão de 27/11 e do OK do João. Ganho só depois de medir.
