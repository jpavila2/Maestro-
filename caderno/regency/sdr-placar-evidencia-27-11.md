# SDR do Blanc: placar de evidência, 2ª amostra (WIA-02)

> Reg · sex 27/11/2026, ~10h40 (Brasília). Fonte: CRM do Blanc (Supabase "BLanc House CRM"), **só leitura e só contagens agregadas**, sem nome, telefone nem texto de cliente.
> Janela: 18/11 (12h) a 27/11 (manhã). Mesma classificação da 1ª amostra (`sdr-placar-evidencia-18-11.md`): saída com `source` vazio e `actor_id` nulo = robô; `source = business_app` = equipe pelo app; saída com `actor_id` = equipe pelo CRM.
> **Ainda não é resultado para mostrar a cliente.** Semana de Black Friday: a equipe estava mais ativa que o normal.

## Comparação com a 1ª amostra
| Indicador | 1ª (08–18/11) | 2ª (18–27/11) |
|---|---|---|
| Conversas com mensagem do cliente na janela | 59 | 48 |
| Conversas em que o robô respondeu | 43 | 28 |
| Conversas com cliente e **sem** resposta do robô | 16 | 20 |
| 1ª resposta do robô (mediana) | ~16 s | **~21 s** (25 de 28 abaixo de 1 min; 3 acima de 1 h) |
| 1ª resposta da equipe onde o robô não respondeu (mediana) | ~4h40 (só app) | **~7,6 min** pelo app (n=17) · **~2,7 min** app + CRM |
| Só conversas novas (1ª mensagem já na janela): robô / equipe sem robô | — | ~21 s (23 conversas) / ~49 s (n=8) |
| Pausas automáticas sem autor (eco, #104) | 100 | **14** |
| Pausas manuais (com autor) | 98 | 44 (39 ok, 5 falharam) |
| Estado agora (todas as conversas) | 108 "human" · 5 "bot" (de 113) | 139 "human" · 6 "bot" · 2 "pausing" (de 147) |
| Conversas ativas na janela com cliente vinculado (`client_id`) | quase nenhuma (#106 pendente) | **54 de 66** |
| Mensagens: cliente / robô / equipe app / equipe CRM | 488 / 412 / 415 / 46 | 403 / 224 / 487 / 33 |

Por dia (cliente · robô · app): 19/11 36·15·65 · 20/11 45·31·38 · **21/11 22·0·51** · 22/11 15·16·17 · 23/11 40·36·40 · 24/11 100·24·124 · 25/11 26·45·10 · 26/11 74·35·76.

## O que muda na leitura
1. **O "16 s contra 4h40" caiu como argumento.** Nesta janela a equipe respondeu em minutos onde o robô não entrou. A diferença de velocidade existe (~21 s contra ~2,7–7,6 min), mas é pequena para vender, e a 1ª amostra comparava populações diferentes. **Parar de usar "a equipe levava umas 4h40"** no kit das autoescolas até o João decidir.
2. **O valor que sobra é cobertura, não velocidade:** o robô responde quando ninguém está olhando (noite, fim de semana). Esta amostra **não mede** horário; é a próxima conta a fazer.
3. **O auto-pause por eco caiu de 100 para 14.** O robô fica menos travado por engano, mas 139 das 147 conversas seguem em "human".
4. **Vínculo conversa → cliente andou (54 de 66).** O funil por estágio começa a ser mensurável; falta contar estágio.
5. **21/11 (sáb): o robô não mandou nenhuma mensagem** com 22 mensagens de cliente. Pode ser queda, pausa geral ou deploy. Conferência vai ao Dev.

## Ressalvas
- "Robô" agora pode incluir outras saídas automáticas sem `source` (follow-up automático, mídia do catálogo #91). O Dev conferiu a classificação só até 18/11.
- Medianas da equipe com n pequeno (8 a 17 conversas).
- Primeira mensagem do cliente = primeira **na janela**, não da conversa (salvo na linha "conversas novas").

## O que falta (dono)
- [ ] **Dev:** confirmar que `source` vazio + `actor_id` nulo ainda é só a Iris depois de 18/11, e o que houve em 21/11.
- [ ] **Reg:** próxima contagem com corte por horário (comercial × noite/fim de semana) e por estágio, agora que há vínculo.
- [ ] **João:** decidir se o argumento de venda passa de "velocidade" para "responde fora do horário" (precisa da conta por horário antes).

## Regra
Nada disto vai para proposta, Minascal, autoescolas ou terceiros sem OK do João.
