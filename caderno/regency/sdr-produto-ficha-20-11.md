# SDR da Regency como produto: ficha v0 (20/11/2026)

> Reg, rascunho interno para o João revisar. **Não é proposta e não sai para cliente nem para o Guga sem OK do João.**
> Fontes: estimativa do Dev de 19/11 (Claude Code, só leitura; `/workspace/sdr-modular-estimativa-19-11.md` no computador do bot), placar do SDR do Blanc (`caderno/regency/sdr-placar-evidencia-18-11.md`) e a conversa do João com o Reg em 19/11.
> Prazos são **estimativa**, não medição. Preços são **hipótese do João**, não validados.

## 1. A promessa (o que dá para dizer hoje sem mentir)
"Seu WhatsApp responde em segundos, 24h, qualifica o lead e passa para a sua equipe quem está pronto para fechar."
- Evidência que já existe: no Blanc (08–18/11), 1ª resposta do robô com mediana ~16 s, contra ~4h40 da equipe nas conversas em que o robô não entrou (43 de 113 conversas com resposta do robô).
- Evidência que **ainda não existe**: conversão, agendamentos e vendas atribuídas ao robô (103 de 113 conversas sem mudança de estágio). Nova contagem: sex 27/11.
- Não prometer: ouvir áudio, ler print/foto, mandar foto de produto, marcar na agenda. Nada disso existe hoje no robô de conversa.

## 2. Módulos: o que existe de verdade
| Módulo | Situação hoje (código, 19/11) | Falta | Esforço estimado (Claude + revisão do Guga) |
|---|---|---|---|
| **Base: responder, qualificar, passar para humano** | ✅ no ar no Blanc. Oferta, tom, objeções, horário, qualificação e limites já vêm de um arquivo por cliente | Tirar do código o que ainda é fixo: modelo, regras de passagem, avisos de mídia, regra de festa na base genérica, CRM amarrado ao Blanc | não estimado (o Dev listou os itens, sem prazo) |
| **Catálogo com foto** | 🟡 quase tudo em 3 PRs abertos, sem merge (plataforma #91, blanc-implantacao #41, CRM #41) | Juntar, portar para o sdr-base, testar e provar um envio real pela Meta | M: 4–6 dias + 1–2 |
| **Agendamento real** | 🔴 robô só consulta a disponibilidade e anota a visita; a equipe confirma | Decidir a agenda-fonte; criar/remarcar/cancelar evento; confirmação com cliente | G: 7–10 dias + 2–3 |
| **Áudio e print** | 🔴 robô responde aviso fixo ("não consigo ouvir / abrir"). A única leitura por IA é a de comprovante PIX no financeiro do CRM | Pedido próprio ao Dev, se o João quiser | não estimado |
| **Link de pagamento** | fora (decisão do João, 19/11) | — | — |

## 3. Por que 2–5 dias de implantação ainda não é real
Hoje cada cliente novo exige mexer no código (CRM preso ao Blanc, regras fixas no Python, fluxos do n8n por cliente). Os 2–5 dias só valem quando "implantar" for **configurar**: subir o catálogo e as regras do negócio, ligar os módulos contratados e conectar o WhatsApp.
**Ordem sugerida para o Dev:** (1) cliente novo sem mexer em código + catálogo com foto (andam juntos); (2) gravar o consumo de cada conversa; (3) agendamento, depois de escolhida a agenda-fonte.

## 4. Preço (hipótese do João) e o que falta para sustentar
- Entrada: **R$ 600–800/mês + R$ 1–2 mil de implantação**.
- Custo de IA por conversa: **não medido** (não há registro de tokens; o gasto fica só na memória do processo e zera ao reiniciar). Só existem tetos: US$ 0,05/mensagem, US$ 1,00/conversa, US$ 20/dia.
- Conta de pior caso, só com o teto: no ritmo do Blanc (43 conversas com robô em ~11 dias, ~120/mês), o teto permite até ~US$ 120/mês de IA por cliente. É limite, não média. O custo real tende a ser bem menor, mas só a medição diz quanto.
- WhatsApp (Meta): resposta dentro da janela de 24h é categoria "service"; mensagem fora da janela (template) é cobrada por categoria. Valores do Brasil: **a confirmar no rate card oficial**.
- Conclusão: o preço de entrada é defensável na promessa de velocidade, mas a margem só fecha com o item (2) da ordem acima.

## 5. Pacote de venda v0 (rascunho para o João decidir)
- **Essencial** (vendável quando o item 1 estiver pronto): resposta 24h + qualificação + passagem para a equipe + relatório quinzenal de velocidade. Preço de entrada.
- **+ Catálogo com foto**: para loja e serviço com vitrine. Adicional na mensalidade (valor a definir).
- **+ Agendamento**: para clínica, salão e visita. Adicional (valor a definir), só depois do módulo pronto.
- Prova para venda: placar do Blanc com velocidade + (a partir de 27/11) contagem de conversas qualificadas.

## 6. Próximos passos
- Reg: refazer o placar do Blanc em 27/11 e juntar aqui.
- Dev (pedido via Maestro): estimar o item 1 (cliente novo sem código) e incluir o registro de consumo por conversa.
- João: decidir se a 1ª versão vendável sai sem agendamento (pergunta abaixo).
