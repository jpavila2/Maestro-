# SDR modular — estimativa curta (para o caderno)

- **Data:** 19/11/2026
- **Modo:** somente leitura. Estimativa, não implementação. Nada foi alterado, commitado ou enviado.
- **SHAs lidos:** plataforma `a5d4b57`, blanc-impl `93e1efa`, CRM `3fe7f38`. PRs: plataforma #91 `44181a3`, blanc-impl #41 `dff11b7`, CRM #41 `bafb60c`, plataforma #88 `0062e30`.
- **Fonte:** `EVIDENCIAS.md` de 19/11 (+ retrato de 18/11 onde marcado CITADO).
- **Limite dos PRs:** worktrees rasos, sem diff. O que o PR faz foi inferido por listagem de arquivos e termos.
- **Prazos abaixo são ESTIMATIVA, não medição.** Unidade: dias de trabalho do Claude + dias de revisão do Guga. Só o que AINDA falta.
- Tamanhos: P ≈ até 2 dias, M ≈ 3–6, G ≈ 7+.

---

## 1) Módulos

### 1.1 Catálogo com foto (busca + envio de mídia) — **M**

**Prazo estimado:** 4–6 dias Claude + 1–2 dias de revisão Guga (≈ 5–8 dias corridos de trabalho).
Se o Guga aceitar mergear os três PRs quase como estão: perto de 4. Se a #91 tiver de ser portada para `sdr-base` ao mesmo tempo: perto de 6.

**Já existe (em PR aberto, NÃO mergeado):**
- Plataforma #91: `agentes/sdr/sdr/midia.py` (164 linhas, leitura do catálogo do CRM com HMAC, `versao_tabela`), ferramentas `consultar_midias` e `enviar_midia` (`ferramentas.py:62,66,260`), erros `midia_fora_do_catalogo` / `midia_vencida`, limite por tipo. Testes listados (`test_midia.py`, `test_midia_servidor.py`), **não rodei**.
- blanc-impl #41: `limite_midias` no JSON (`blanc-house.json:77`), documentação do envio no fluxo 51. O `ferramentas.py` desse PR **não** tem `enviar_midia`.
- CRM #41: rota `api/midia/v1/catalogo.mjs`, `js/midia-robo.js` (tela), migration `migration-midia-aprovada.sql` (+ volta), 3 testes.
- Estado hoje no main: nada disso existe. `andamento.json:154`: "Robô enviar fotos, vídeos e PDF… ainda não existe".

**Ponto de atenção:** o #91 está em `agentes/sdr`, **ainda não em `sdr-base`**. Hoje o `sdr-base` não tem mídia.

**Falta (o trabalho a estimar):**
1. Revisar e mergear os 3 PRs na ordem certa (CRM → plataforma → blanc). Comparar contrato `midia.catalogo` linha a linha (não foi feito).
2. Decidir onde o código mora (`agentes/sdr` vs `sdr-base`) e ajustar para o `sdr-base`.
3. Rodar os testes dos PRs e escrever o teste ponta a ponta (robô → catálogo → envio).
4. Fluxos n8n 50/51/52: envio real de imagem/vídeo/PDF pela Meta (hoje o envio do robô é só `type: 'text'`, CITADO). O que o #91 já mudou nesses fluxos: **não verificado**.
5. Subir a migration no Supabase e testar a tela de aprovação de mídia.
6. Ajuste de prompt/regra: o que o robô pode prometer com foto.

**Dependências:** blanc #41 depende do código do #91 (SUPOSIÇÃO); catálogo só responde com o CRM #41 no ar; migration aplicada; mídia aprovada cadastrada pela equipe (trabalho de negócio, fora desta estimativa).

**Risco principal:** fluxos n8n e VPS não verificados. Pode estourar para o fim da faixa.

### 1.2 Agendamento real — **G**

**Prazo estimado:** 7–10 dias Claude + 2–3 dias revisão Guga. Faixa larga porque a decisão de fonte da agenda ainda não existe.

**Já existe:**
- Consulta **só de leitura**: `sdr-base/sdr/agenda.py:32` (`/api/agenda/v1/disponibilidade`), `moldes_agenda.py`, `turno_agenda.py`. CRM: `api/_agenda/disponibilidade.mjs` (ocupada se há contrato na data/casa ou lead fechado; erro vira `indisponivel`).
- Blanc main **não tem** esses 3 arquivos (estão no `sdr-base` e no PR #91).
- Hoje o robô só anota dia/período no campo `visita`; a equipe confirma (CITADO).

**Não existe em lugar nenhum:** criar evento, agenda própria, Google Calendar (só menções em HTML/`vercel.json`, não li), confirmação com o cliente.

**Falta:**
1. Decisão de produto: fonte da agenda (contrato/lead do CRM como hoje, agenda própria ou Google Calendar). Sem isso não dá para fechar prazo.
2. Ferramenta de criar/remarcar/cancelar evento + endpoint de escrita no CRM (hoje só leitura) + HMAC.
3. Regras: conflito, antecedência, horário de atendimento, dupla reserva.
4. Fluxo de confirmação com o cliente e aviso à equipe.
5. Remover do `sdr-base` o regex de festa fixo (`turno_agenda.py:41`) ou parametrizar.
6. CRM é amarrado ao Blanc (`CASAS = ['house','lounge']`, `disponibilidade.mjs:6`): para outro cliente precisa generalizar.
7. Testes e deploy.

**Dependências:** decisão de fonte; CRM com endpoint de escrita; migração para `sdr-base` se for módulo reutilizável.

### 1.3 Fora desta estimativa
- Link de pagamento: fica para depois, não estimado.

---

## 1b) Leitura de áudio e de print/imagem — CONFIRMAÇÃO (sem prazo)

**Divergência:**
- João: já existe.
- Retrato de 18/11 e código de 19/11: **no SDR do Blanc não existe**. Os dois documentos coincidem entre si; a divergência é com a fala do João.

**Evidência (arquivo:linha):**
- `plataforma/implantacoes/andamento.json:150`: áudio do cliente "só em desenho". `:154`: ler imagens e documentos "ainda não existe".
- Kit 44, nó "Preparar para o SDR" (`integracoes/n8n/fluxos/kit/sdr/44-kit-whatsapp-para-sdr.json`, linha 44): áudio vira "(o contato mandou um áudio, que o atendimento automático não consegue ouvir)"; imagem/vídeo/documento sem legenda viram "(…mídia que o atendimento automático não consegue abrir)".
- `blanc-impl/agentes/sdr/sdr/passagem.py:58-61` (`MIDIA_SEM_TEXTO`) e `:97-98` (vai para a equipe após conversa de pagamento). Mesmo aviso em `plataforma/agentes/sdr-base/sdr/passagem.py:81-82`.
- Busca por `whisper`, `speech`, `input_audio`, `image_url`, `ocr`: vazia em mains, PRs, CRM e fluxos. `transcri` no SDR (`motor.py:104,173,195`, `api.py:113`, `servidor.py:246,260`) é transcrição de sessão do Agent SDK, não de áudio.
- PR plataforma #88: só desenho (mensagem do commit).

**Onde a leitura existe de fato (único caso verificado):**
- `crm/api/ler-comprovante.js`: manda imagem ou PDF à API da Anthropic (blocos `image` e `document`, `:192-193`; endpoint `:196`; modelos `:18-19`). Finalidade: comprovante de PIX e nota de gasto, **financeiro do CRM**. **Não é o robô** e não achei chamada dele pelo SDR.
- Não é leitura: `crm/js/conversas-audio.js` (player) e `crm/js/gravar-audio.js` (equipe grava nota de voz).

**Limites desta confirmação:** não verifiquei a VPS nem o n8n publicado. Não afirmo de onde vem a memória do João. Não afirmo nada que não vi no código.

---

## 2) Cliente novo sem mexer em código

**JÁ configurável (JSON em `implantacoes/<cliente>/sdr/<id>.json`, `carregar_implantacao`, `implantacao.py:191`):**
- Identidade e oferta: `id`, `nome`, `aviso`, `empresa_oferta`, `cliente_ideal`, `preco`, `diferenciais`, `objecoes`, `tom`, `objetivo`.
- Comportamento: `gatilho_passagem_humano` (lista), `horario_atendimento`, `textos_retorno`, `aviso_ia`, `modo_envio` (Blanc usa `automatico`), `objetos_contrato`, `criterios_qualificacao`, `campos_resumo`, `campos_qualificacao`, `fontes`.
- Limites (defaults no código, o JSON do Blanc não os define; podem ser sobrescritos): `limite_respostas_hora` 20, `limite_custo_conversa_usd` 1.0, `limite_custo_diario_usd` 20.0, `limite_respostas_dia` 1000 (`implantacao.py:66-71`).
- Só no PR #41: `limite_midias`.
- O prompt usa esses campos (`sdr-base/prompt.py:116-124`). No código do SDR não achei nome, cidade ou marca do Blanc.

**AINDA FIXO no Python:**
- Ferramentas: lista fechada de 9 (`ferramentas.py:24-56`).
- Temas de passagem: regex por tema (`passagem.py:20-57`); só a lista `gatilho_passagem_humano` vem do JSON.
- Aviso de mídia (`passagem.py:60`).
- Regex de festa, **de nicho, dentro da base genérica** (`sdr-base/.../turno_agenda.py:41`).
- Regex de aviso de IA (`atendimento.py:618` Blanc; `:1208` sdr-base).
- Modelo: `MODELO_PADRAO = "claude-haiku-5-5"` (`motor.py:31`), esforço `medium` (`motor.py:89`), teto por mensagem 0,05 (`motor.py:88`). Não vêm do JSON. Se há variável de ambiente para trocar: não verificado.

**AINDA FIXO no n8n / fora do SDR:**
- Aviso de mídia no kit 44 (linha 44).
- Envio do robô só texto (fluxo 51, CITADO).
- Placeholders `SDR_IMPLANTACAO__` / `SDR_URL` nos fluxos: não li o gerador (`ponte-gerar-fluxos.mjs` só existe no PR #41), não sei como são preenchidos no deploy.
- CRM inteiro amarrado ao Blanc (`CASAS` fixo, título "BLANC HOUSE CRM"). Não é multi-tenant.

**O que falta para o "arquivo de conhecimento editável" (a estimar depois, não estimado aqui):**
1. Mover para o JSON: modelo/esforço/tetos, textos de aviso de mídia, regex/temas de passagem e de nicho, e lista de ferramentas habilitadas.
2. Tirar o regex de festa da base.
3. Arquivo de conhecimento (FAQ/preço/objeções) em formato que o cliente edite, com validação do JSON.
4. Gerador de fluxos n8n por cliente documentado.
5. CRM por cliente (ou desacoplar a agenda dele).
Registro: regra do repo é "clientes são implantações isoladas" (`plataforma-pr91/CLAUDE.md:6`, CITADO).

---

## 3) Custo por conversa no Blanc (IA + API do WhatsApp)

### DADO REAL (visto no código)
- Modelo: `claude-haiku-5-5` (`blanc-impl/agentes/sdr/sdr/motor.py:31`), padrão; o JSON do Blanc não define modelo.
- Custo do turno vem do motor: `custo_usd = resultado.total_cost_usd` (`motor.py:188`).
- **Tetos, não médias:** US$ 0,05 por mensagem (`motor.py:88`, passado como `max_budget_usd` `:134`); US$ 1,00 por conversa (`implantacao.py:69`); US$ 20,00 por dia (`:70`); 20 respostas/hora e 1000/dia (`:67,:71`).
- Acumulado da conversa: `custo_conversa_usd` (`atendimento.py:48`); checagem do teto `:157-158`; diário `:163-168`.
- **Custo em memória do processo:** `repositorio.py:8` guarda `conversas_em_andamento`, `respostas_por_mensagem` e `consumo_diario` só em memória. O gasto diário **zera ao reiniciar**.
- Não há tabela nem log de tokens médios em nenhum repo (`input_tokens`/`output_tokens` só em testes e `experiments/`).

### SUPOSIÇÃO
- O comentário em `atendimento.py:48` diz que o custo da conversa "vai à ficha do lead"; não verifiquei se é de fato gravado no CRM/Supabase.

### NÃO MEDIDO / A CONFIRMAR
- **Média de tokens e custo médio por conversa:** não medido. Precisaria de um agregado no Supabase (se o campo for gravado na ficha). Não consultei banco. Não há número honesto para colocar aqui.
- **Preço do modelo Anthropic (Haiku 5.5):** **a confirmar na fonte oficial.** A página oficial redirecionou para `platform.claude.com/docs/en/about-claude/pricing` e eu não completei a leitura. Sem número.
- **API do WhatsApp (Meta), consulta em `developers.facebook.com/docs/whatsapp/pricing`:**
  - Estrutura confirmada na página: cobrança por mensagem enviada pelo negócio e entregue; mensagem do usuário não é cobrada; categorias com template (marketing, utility, authentication) e sem template (service, só dentro da janela de 24 h aberta pelo usuário).
  - Franquia grátis: 1.000 mensagens de service por mês por número comercial; janela de entrada gratuita de 7 dias para contato vindo de anúncio Click-to-WhatsApp (só apps Android/iOS).
  - Página reflete preços com vigência de **1º/10/2026**; a Meta só altera preços em 1º de jan/abr/jul/out.
  - **Valores de Brasil: a página não os lista no texto** (estão no rate card CSV/PDF, em BRL e USD). Há uma referência de ~US$ 0,0068 por mensagem de utility/authentication no Brasil, lida por resumo automático da página; **a confirmar no rate card oficial, não usar como número fechado.** Marketing e service no Brasil: **a confirmar na fonte oficial.**
  - Implicação qualitativa (não é número): enquanto o robô responde dentro da janela, a resposta é service; template fora da janela (reengajamento) é cobrado por categoria.

---

## Resumo

- Catálogo com foto é **M**: ~4–6 dias Claude + 1–2 do Guga, porque o grosso está pronto em 3 PRs abertos; falta mergear, portar para `sdr-base`, testar e provar envio real na Meta.
- Agendamento real é **G**: ~7–10 dias Claude + 2–3 do Guga; hoje só lê a agenda, não cria nada, e falta decidir a fonte da agenda.
- Áudio e print: no SDR do Blanc **não existe** (aviso fixo no kit 44 e `passagem.py`); só existe leitura por IA no CRM financeiro (`ler-comprovante.js`). Divergência com o João registrada, sem prazo.
- Cliente novo sem código: o JSON cobre oferta, tom, critérios e limites; modelo, ferramentas, regras de passagem, avisos de mídia, regex de nicho e o CRM ainda são fixos.
- Custo: teto por conversa US$ 1,00 e modelo Haiku 5.5 são dados reais; média por conversa e preços (Meta Brasil, Anthropic) **não confirmados**.

## A confirmar / não visto

- VPS e n8n publicado (não li); se o fluxo 51 e o kit 44 em produção batem com o repo.
- Diff real dos PRs (worktrees rasos); o que o #91 mudou nos fluxos 50/52.
- Testes: nenhum rodado (inclusive os dos PRs).
- Contrato `midia.catalogo` entre #91 e CRM #41: não comparado linha a linha.
- Supabase: não consultei; não sei se o custo por conversa é gravado.
- Média de tokens e custo médio por conversa: não medido.
- Preço do modelo Anthropic: a confirmar (página oficial não lida até o fim).
- Preço WhatsApp Brasil (marketing/utility/service): a confirmar no rate card oficial da Meta.
- Gerador de fluxos (`ponte-gerar-fluxos.mjs`) e variável de ambiente de modelo: não verificados.
- Google Calendar no CRM: só menções, não li.
- Link de pagamento: fora do escopo.
