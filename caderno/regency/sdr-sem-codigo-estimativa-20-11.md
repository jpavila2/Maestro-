# SDR "cliente novo sem mexer em código" — estimativa (20/11/2026)

- **Data:** 20/11/2026
- **Modo:** somente leitura. Estimativa, não implementação. Nenhum checkout alterado; só comandos de leitura (`git show`, `git grep`, `git diff`, `grep`). Nada commitado, enviado ou migrado. Nenhum banco consultado. Nenhum teste rodado. VPS e n8n publicado não verificados.
- **SHAs lidos:**
  - **MAIN:** plataforma `a5d4b57` (motor `agentes/sdr-base`); Blanc `93e1efa` (`blanc-impl`, copia `agentes/sdr`, o que roda no Blanc); CRM `3fe7f38`.
  - **#113 (rascunho, NÃO mergeado):** plataforma `3634cc5`, implantação `7fe556a`, CRM `d696b88` (branch `claude/ia-vendas-correcoes-19-11`).
- **Base:** `sdr-modular-estimativa-19-11.md` e `EVIDENCIAS.md` de 19/11. Só o que mudou ou o que não bate com o código de hoje está aqui.
- **Prazo é ESTIMATIVA.** Unidade: dias de trabalho do Claude + dias de revisão do Guga. É esforço somado, não calendário.
- **Tamanho:** P ≤ 2 dias; M 3–6; G 7+.
- **Convenção de citação:** `P:` = plataforma (main), `B:` = Blanc main (`blanc-impl`), `C:` = CRM main, `#113-P/B/C` = os três branches do #113.

---

## 1) Cliente novo sem mexer em código

### a) Modelo (hoje `claude-haiku-5-5`) — **P**

- **Fixo hoje:** `B:agentes/sdr/sdr/motor.py:31` (`MODELO_PADRAO`), `:86` (default do campo `modelo`). Mesmo em `P:agentes/sdr-base/sdr/motor.py:31,88`.
- Esforço `medium` e teto por mensagem: `motor.py:88` (`max_custo_usd = 0.05`), 19/11 citou `:89` para o esforço; não reverifiquei essa linha.
- Não achei variável de ambiente para trocar o modelo: `grep environ|getenv` em `motor.py` só mostra a lista de permissão de ambiente (`:11`, `:33`, `:110`).
- **Já configurável:** nada do modelo vem do JSON. `carregar_implantacao` (`implantacao.py:191`) lê o JSON, mas não traz modelo.
- **Como fica configurável:** campo `modelo` (e `esforco`) em `Implantacao` + validação (há faixas em `implantacao.py:96`) + repassar ao motor.
- **#113:** não toca `motor.py` (stat dos três branches).
- **Dias:** 1–2 Claude + 0,5 Guga.

### b) Regras de passagem para humano — **M**

- **Já configurável:** lista de gatilhos (`B:implantacoes/blanc-house/sdr/blanc-house.json:54`, `gatilho_passagem_humano`).
- **Fixo hoje:**
  - Temas de passagem em regex: `B:agentes/sdr/sdr/passagem.py:19` (tupla `_MODELOS`), `:90` (`tema_obrigatorio`).
  - Contexto de pagamento: `B:passagem.py:61` (`_CONTEXTO_PAGAMENTO`, lista de palavras fixa).
- **#113:** não toca `passagem.py` (stat).
- **Como fica configurável:** temas e palavras de contexto no JSON, com validação; ajustar os testes de passagem.
- **Dias:** 3–4 Claude + 1 Guga.

### c) Avisos de mídia (áudio, imagem, documento que o robô não abre) — **P**

- **Fixo hoje:**
  - Texto do aviso: `B:passagem.py:60` (`MIDIA_SEM_TEXTO`); `P:agentes/sdr-base/sdr/passagem.py:83`.
  - Regra que usa o aviso (com pagamento no contexto): `B:passagem.py:97`.
  - Aviso repetido no fluxo n8n do kit 44: `integracoes/n8n/fluxos/kit/sdr/44-kit-whatsapp-para-sdr.json`, linha 44 (**19/11**; não reli hoje).
- **#113:** não toca esse ponto.
- **Atenção:** mudar o texto é barato. Mudar a capacidade (o robô ouvir ou ver mídia) é outro módulo e **não está estimado aqui** (ver 19/11, item 1b).
- **Como fica configurável:** texto no JSON; ajustar a regra em `passagem.py:97`; atualizar o kit 44 no n8n (fluxo separado).
- **Dias:** 1–2 Claude + 0,5 Guga (inclui o kit 44).

### d) Regra de festa (tipos de evento, preço, qualificação antes do preço) — **M** (o #113 já fez parte; ver nota)

**Hoje no MAIN:**
- **Regex de festa dentro da base genérica:** `P:agentes/sdr-base/sdr/turno_agenda.py:41` (`_ASSUNTO_DE_FESTA`); `:26` (`marcar ... festa|evento`).
- **Tipos de evento:** não achei lista de tipos em JSON nem em código do Blanc main. O JSON main só tem "infantil" no texto de `empresa_oferta` (`B:blanc-house.json:5`). O campo `tipo_evento` existe em `campos_resumo` / `campos_qualificacao` (`B:blanc-house.json:200`).
- **Preço:** é lista de textos livres, não tabela estruturada: `B:blanc-house.json:7` (`preco`), `:9` (`pacotes-2027`). O valor sai do texto, sem campo de valor.
- **Qualificação antes do preço:** não existe no main. `preco.py` não está no main (é arquivo novo no #113).
- **CRM (default de tipo):** `C:js/core.js:392`, `:427`, `:1149` ("15 anos" como padrão quando o tipo vem vazio). Regex de nicho em `C:js/fonte-unica.js:103` (`infantil|formatura|...`).

**O que o #113 já fez (NÃO mergeado):**
- `#113-P` cria `agentes/sdr-base/sdr/preco.py` (142 linhas). Trava o preço até qualificar (`preco.py:23` `TURNOS_DE_PERGUNTA_APOS_PEDIDO_DE_PRECO = 2`).
- **Ponto de atenção:** o texto de Blanc continua no código da base: `preco.py:33` (`PERGUNTA_VALORIZA_INFANTIL`) e a lista `PERGUNTAS_PADRAO` (`:25`). O número 2 também é constante no código, não config.
- `#113-B` (implantação) muda **só JSON e teste** (stat). Acrescenta `pacote-infantil`, `tipos-de-evento`, `qualificacao_antes_do_preco` e reescreve preço e ordem do atendimento. **Não há código Python no branch da implantação.**
- `#113-C` (CRM) corrige o default: tira `'15 anos'` de `core.js` (diff: `tipo_evento||''`). Não mexe em `CASAS` nem na regex de nicho.

**Consequência importante:** o código do #113 está só no `sdr-base`. O Blanc roda a cópia `B:agentes/sdr`, que o #113 não toca. Hoje, a regra nova **não chega ao Blanc** sem portar ou migrar o Blanc para `sdr-base`. Isso é verificado pelo stat; o comportamento em produção não foi verificado (VPS).

**O que falta (fora do #113):**
1. Revisar e mergear `#113` (Guga; testes não rodados): 1–2 Guga.
2. Mover tipos de evento, preço estruturado (valor por pacote, até N convidados, ano), constante de turnos e `PERGUNTA_VALORIZA_INFANTIL` para config com validação.
3. Regex de festa (`turno_agenda.py:41`) e regex de nicho (`fonte-unica.js:103`) para config.
4. Decidir: o Blanc migra para `sdr-base`? Se não, portar `preco.py` para `B:agentes/sdr` (2–3 dias extras).

- **Dias (restante, depois do merge):** otimista 2 Claude; realista 5 Claude + 2 Guga (inclui merge do #113 e a estrutura de preço).

### e) Desacoplar o CRM do Blanc — **G** (ou M, se só config)

**Amarrado ao Blanc hoje (MAIN):**
- Casas fixas: `C:api/_agenda/disponibilidade.mjs:6` (`CASAS = ['house','lounge']`); usado em `:46`, `:52`, `:63`. Vale para outro cliente só se trocar o código.
- Default "15 anos": `C:js/core.js:392`, `:427`, `:1149`. O #113-C corrige (ver d).
- Regex de nicho: `C:js/fonte-unica.js:103`.
- Título "BLANC HOUSE CRM" em `C:js/relogio.js`, `js/avisos.js`, `js/fonte-unica.js` (**19/11**; apareceu na busca de hoje, sem linha exata).
- Agenda: `C:api/_agenda/disponibilidade.mjs` só lê; não cria evento.

**Dois caminhos:**
- **Config por cliente (M, 4–6 dias Claude + 2 Guga):** casas, tipos e nomes vêm de um JSON por implantação. O CRM continua uma instância por cliente.
- **Multi-tenant (G, 8–12 dias Claude + 3 Guga):** um CRM para vários clientes, com isolamento de dados no Supabase (RLS, chaves por cliente) e migração. Não é só código.

- **Escolha para o total:** o realista usa **G**; o otimista usa **M** (config).

---

### TOTAL — itens a–e (sem catálogo, sem agendamento)

| Item | Tamanho | Otimista (Claude / Guga) | Realista (Claude / Guga) |
|---|---|---|---|
| a) Modelo | P | 1 / 0,5 | 2 / 0,5 |
| b) Passagem para humano | M | 2 / 1 | 4 / 1 |
| c) Avisos de mídia | P | 1 / 0,5 | 2 / 0,5 |
| d) Regra de festa (já com #113 em parte) | M | 2 / 1,5 | 5 / 2 |
| e) Desacoplar CRM | M / G | 6 / 2 | 10 / 3 |
| **Total** | | **12 / 5,5** | **23 / 7** |

- **Total realista ≈ 30 dias de esforço somado** (23 Claude + 7 Guga). **Otimista ≈ 18** (12 + 5,5, arredondado).
- **Não somei o que os PRs já fazem.** O #113 entra só como "merge + revisão" (1–2 dias de Guga) e como "o que sobra". Os PRs #91, #41 e #41 (catálogo) estão fora deste total.
- **Fora do total (não estimado):** gerador de fluxos n8n por cliente (19/11 citou `ponte-gerar-fluxos.mjs`, só existe no PR #41, não reverificado) e como os placeholders `SDR_IMPLANTACAO__` / `SDR_URL` são preenchidos no deploy.
- **Catálogo com foto e agendamento:** ver 19/11 (catálogo M; agendamento G). Não estimado aqui.

---

## 2) Registro de tokens e custo por conversa

### Estado de hoje (VERIFICADO no código)

- **Main, motor base (`P:agentes/sdr-base`):** já existe um custo diário persistido, mas **atrás de flag e só em SQLite local**, não no Supabase:
  - `P:sdr/beta.py:205` `registrar_custo(agora, usd_micro, tipo)`; `:214` sai se `telemetria_agregada` está desligada (padrão `:83`).
  - Tabela SQLite `custo_diario` (README `P:agentes/sdr-base/README.md:497–499`). Liga com `SDR_TELEMETRIA_AGREGADA=sim` (`README:52`).
  - Ponto de chamada: `P:sdr/atendimento.py:247` (`_registrar_custo`) e `P:sdr/api.py:407` (`ao_custo`).
- **Blanc main (`B:agentes/sdr`):** tem `beta.py` (`B:api.py:29` importa `EstadoBeta`), mas **não chama `registrar_custo`**. A busca por `registrar_custo`, `ao_custo=` e `SDR_TELEMETRIA` em `agentes` deu vazio. **O que roda no Blanc não grava custo diário.**
- **Teto em memória (ainda verdade no Blanc):** `B:repositorio.py:8`, `:35–37` (`respostas_por_mensagem`, `conversas_em_andamento`, `consumo_diario`). Zera ao reiniciar.
- **Conversa:** `B:atendimento.py:48` (`custo_conversa_usd`) é campo em memória. O comentário "vai à ficha do lead" **não verifiquei**; não achei gravação de custo por conversa no CRM main.
- **Tokens:** `motor.py` não lê uso de tokens (`grep usage|input_tokens` vazio). Só custo: `B:motor.py:188` (`custo_usd = resultado.total_cost_usd`). Se o SDK expõe tokens na versão instalada: não verificado.
- **CRM main:** não achei tabela de custo de IA. Os achados de `custo|gasto` são do financeiro (`api/ler-comprovante.js`, `js/comprovantes.js`, `js/despesas.js`).
- **#113-P:** não cria tabela nem migração. Mexe no fluxo de custo: soma o custo de uma segunda chamada em `atendimento.py` (linhas `+` com `custo = custo + segunda.custo_usd`). Reusa o hook `ao_custo`. **Não é gravação nova.**

### Correção ao 19/11

- 19/11 disse "custo só em memória, sem log persistente". **Vale para o Blanc**, mas **não para o motor base do main**, que já tem custo diário em SQLite atrás de flag. O 19/11 não viu isso.

### Proposta de tabela (Supabase, só o que é necessário)

| Tabela | Campos essenciais | Observação |
|---|---|---|
| `sdr_custo_chamada` | `id`, `implantacao_id`, `conversa_ref` (hash, sem telefone), `instante` (timestamptz), `modelo`, `tokens_in`, `tokens_out` (se o SDK der), `custo_usd_micro` (bigint), `tipo` (`medida` / `estimada` / `sem_custo`) | 1 linha por chamada ao motor. Sem texto da conversa (privacidade) |
| `sdr_custo_diario` (view) | `dia` (São Paulo), `implantacao_id`, soma de `custo_usd_micro`, contagem por tipo | Agrega a tabela acima; substitui o `consumo_diario` quando for o caso |

- **Onde capturar:** `P:sdr/atendimento.py:247` (ponto que já passa `custo` e `teto_declarado`) e o hook `ao_custo` em `P:sdr/api.py:407`. No Blanc: `B:agentes/sdr/sdr/atendimento.py` (a cópia não tem o hook; precisa portar ou migrar).

### Esforço (estimativa)

- Tabela e escrita a partir do hook (sem tokens): **2–3 dias Claude**.
- Tokens (se o SDK expuser): **+1 dia Claude**, depois de confirmar o campo.
- Consulta/relatório simples: **+1–2 dias Claude** (opcional).
- **Do Guga:** aprovar a migration no projeto Supabase (aplicação não feita aqui), definir quem escreve (chave só no servidor, sem expor no cliente), definir retenção (hoje a SQLite tem 30 dias: `beta.py:82`).
- **Número de custo médio por conversa:** não há. Não medido.

---

## 3) Riscos e incertezas

- **Duas cópias do motor:** `sdr-base` (plataforma) e `agentes/sdr` (Blanc). Divergem; o #113 só atinge a base. Cliente novo "sem código" pede escolher uma. Esse é o maior risco de prazo.
- **Blanc roda a cópia antiga do motor:** o que está no #113 não chega ao Blanc sem porte ou migração (ver 1d).
- **VPS não verificada.** As cópias do GitHub podem estar atrás do que roda. Também não sei se `SDR_TELEMETRIA_AGREGADA` está ligada na VPS.
- **n8n publicado não verificado.** O kit 44 e os fluxos 50/51/52 podem diferir do repo.
- **PRs abertos:** o #113 não tem teste rodado; o #91 e os #41 têm diff raso (19/11). Qualquer "já está pronto" depende de merge e revisão.
- **CRM amarrado ao Blanc:** a estimativa de "sem código" só vale se o cliente usar o CRM do Blanc como base e aceitar as casas e tipos por config. Multi-tenant é G e não é só código.
- **Preço em texto livre:** o robô calcula o valor lendo texto. Config estruturada muda o comportamento e pede testes de regressão.
- **Sem teste rodado:** nenhum teste foi executado nesta sessão, nem nos PRs.
- **Mudança de regra por cliente (hipótese, não medida):** se passagem e regra de festa não estiverem em config, cada ajuste pedido por um cliente novo vira alteração de código e reabre o prazo.

---

## Resumo

- **Cliente novo sem código** não está pronto. Estimativa realista: **≈ 23 dias Claude + 7 dias Guga** (≈ 30 de esforço somado); otimista **≈ 12 + 5,5**. Já descontado o que o #113 faz, que ainda precisa de merge.
- **Modelo (P)** e **avisos de mídia (P)** são fáceis: 1–2 dias cada.
- **Passagem para humano (M)** pede tirar os temas do código: 3–4 dias.
- **Regra de festa (M)** tem o maior trecho já feito em PR (#113), mas o código fica só no `sdr-base` e o Blanc roda outra cópia. Sem migrar ou portar, a regra não chega ao Blanc.
- **CRM (M ou G)**: M se for só config por cliente; G se for multi-tenant. Realista: G.
- **Custo:** o motor base do main tem custo diário em SQLite atrás de flag; o Blanc não grava nada. Proposta de tabela Supabase `sdr_custo_chamada` + view diária: 2–3 dias Claude + aprovação do Guga.
- **Catálogo com foto e agendamento** continuam fora deste total (ver 19/11).

## A confirmar / não visto

- VPS: se o Blanc roda `blanc-impl` ou `sdr-base`, e se `SDR_TELEMETRIA_AGREGADA` está ligada.
- n8n publicado (kit 44; fluxos 50/51/52) e o gerador de fluxos (`ponte-gerar-fluxos.mjs`).
- Diff completo dos PRs (`#113-P` implantação não lido linha a linha; `implantacao.py +8` no `#113-P` não lido).
- Testes: nenhum rodado.
- Supabase: não consultado. Não sei se o CRM já guarda algum custo.
- SDK: se expõe tokens na versão instalada.
- Linha exata do título "BLANC HOUSE CRM" e do esforço `medium` (`motor.py:89`): não reverificadas.
- Preço do modelo e preço WhatsApp (Brasil): fora deste pedido; 19/11 já marcou como a confirmar.
- Dias de Guga: estimativa de tempo de revisão, não agenda real.
