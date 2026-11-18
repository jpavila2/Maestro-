# Plano: Turma Animada no sistema dos Animados (18/11/2026)

Só plano. Nada foi alterado no sistema nem no banco. Opção A (mesmo sistema, mesmo banco), confirmada pelo João em 18/11.

**Aviso de certeza:** não lemos o banco ao vivo nem o código do Mac (estava offline, e a pasta não tem git). O plano parte dos documentos e do site/JS de produção. Vou marcar cada ponto assim:
- **(JS)**: confirmado no código publicado do site.
- **(doc)**: está escrito nos docs, mas ainda não conferido no banco.
- **(conferir)**: depende do `schema-cloud.sql` ou do banco, que ainda não lemos.

A primeira ação da implementação é conferir o `schema-cloud.sql` e as regras de acesso no painel da conta certa do Supabase.

---

## 1) O que muda no banco (schema)

### Provavelmente já existe
- Tabela `empresas`, com coluna `slug` (um apelido curto, tipo `os-animados`). **(JS)** O site busca a empresa pelo slug.
- Tabela `usuarios_empresas`: liga cada pessoa às empresas que ela pode ver. **(doc)**
- Coluna `empresa_id` em `servicos`, `festas` e `lancamentos`. `festa_servicos` herda a empresa pela festa. **(doc)**
- Funções `salvar_contrato` (grava festa + itens + sinal de uma vez), `importar_local` e `tem_acesso`. **(JS)** para os nomes que o site chama; **(conferir)** o que cada uma faz no banco.
- Regra que liga o e-mail certo à empresa quando a pessoa cria conta. **(doc)**

### Novo ou a completar
- Uma segunda linha em `empresas` para a Turma, com slug próprio (ex.: `turma-animada`).
- **Dados da contratada por empresa.** Hoje o nome, CNPJ e endereço estão escritos no código do contrato, não no banco. **(JS)** Precisa virar dado da empresa. O CNPJ é o mesmo nas duas empresas (empresário individual), mas o nome fantasia é diferente.
- **Marca e modelo de contrato por empresa.** Hoje o visual e as cláusulas são só dos Animados. **(JS)**
- **Filtro por empresa no site.** Hoje as listas puxam tudo que o banco deixar passar, sem filtrar pela empresa escolhida. **(JS)** Com o João nas duas empresas, festas e financeiro iriam misturar. Esse filtro é obrigatório antes de a Turma ter dados.
- **Regra de salão.** O site hoje não deixa salvar festa sem nome de salão. **(JS)** Isso não serve para a Turma (aluguel também em casa e clube). Vira regra por empresa.
- Catálogo da Turma, estoque e reservas (abaixo).

### RLS: o que precisa garantir
RLS é a regra do próprio banco que decide quem vê cada linha. Sem ela, quem está logado vê tudo.

- Gustavo vê só os Animados.
- João vê as duas.
- Cadastro aberto (qualquer um criar conta) deve ser desligado, depois de confirmar.

Os docs dizem que isso já está pronto, mas o que confirmamos por escrito é só que o banco recusa quem não está logado. **Não está confirmado que as regras separam por empresa.** Só afirmamos isso depois de ler as regras no painel.

### Storage de PDFs
Hoje o PDF é gerado no navegador (janela de impressão, "salvar como PDF") e não é guardado em lugar nenhum. **(JS)**
**Recomendação:** não criar armazenamento de arquivos neste ciclo.

### Numeração de contrato
Hoje não existe número de contrato. **(JS)**
**Recomendação:** não inventar agora. Se um dia for preciso, numerar por empresa (ex.: `OA-001` para os Animados, `TA-001` para a Turma).

### Catálogo e preços por empresa
A Turma usa a tabela oficial do João (18/11). **(doc: confirmada pelo João)**

| Item | Preço |
|---|---|
| Futebol de Sabão | R$550 |
| Tobogã | R$420 |
| Pula-pula 2,44 m | R$120 |
| Pula-pula 3,05 m | R$150 |

Pacotes (preço cheio / último caso):

| Pacote | Preço cheio | Último caso |
|---|---|---|
| Futebol + PP 2,44 m | R$600 | R$550 |
| Futebol + PP 3,05 m | R$650 | R$600 |
| Tobogã + PP 2,44 m | R$500 | (só um preço) |
| Tobogã + PP 3,05 m | R$530 | (só um preço) |
| Futebol + Tobogã + PP 2,44 m | R$950 | (só um preço) |
| Futebol + Tobogã + PP 3,05 m | R$1.000 | (só um preço) |
| Futebol + Tobogã + os dois pula-pulas | R$1.100 | (só um preço) |

Regras do catálogo:
- Cada serviço tem o **preço cheio** e um **preço de último caso**. O de último caso fica vazio quando não existir.
- Na hora de fechar a festa, o sistema pergunta qual preço foi usado e grava essa escolha na festa. O catálogo não muda.
- **Frete é lançamento à parte**, nunca dentro do preço do brinquedo. Itaguaí fora do centro: R$30. **Centro: ainda não confirmado** (não inventamos número).
- Fora de Itaguaí: o sistema não fecha o frete sozinho. Mostra aviso e passa para o João decidir.
- Frete grátis só existe como concessão de último caso, marcada na festa. Nunca como regra no catálogo.
- **Não cadastrar:** mini tobogã, casinha de bolinhas e Área Baby. O João confirmou que não temos mais.
- Os Animados seguem com o catálogo deles. A coluna de último caso existe, mas fica vazia para eles.
- **Quantidade física de cada brinquedo ainda não foi informada.**

### Estoque: brinquedos e reservas por data (novo, só para a Turma)
Hoje não existe controle de estoque no banco. **(JS)** Confirmar no `schema-cloud.sql`.

Duas tabelas novas:
1. `brinquedos`: nome, quantidade que a empresa tem, ativo. Ex.: futebol, tobogã, pula-pula 2,44 m, pula-pula 3,05 m.
2. `festa_brinquedos` (a reserva): liga festa + brinquedo + quantidade reservada + data.

Como o sistema calcula o que está livre numa data:
**livre = quantidade do brinquedo − soma das reservas daquele dia (só festas não canceladas)**

Regras:
- Festa cancelada libera o brinquedo.
- Evento de vários dias = uma reserva por dia.
- Pacote reserva cada brinquedo que o compõe, no mesmo dia.
- Os Animados não usam isso (sem linhas em `brinquedos`, a agenda deles não muda).

Na agenda da Turma, cada dia aparece como **livre**, **parcial** (cabe algum brinquedo) ou **ocupada**.

### Consulta de disponibilidade para o bot (só leitura)
O bot de WhatsApp só consulta. Ele não cria, não altera e não lê festas, clientes, CPF ou valores.

Como fica:
- **Função no banco** (ex.: `disponibilidade(data)`), que devolve só: data, brinquedo, quantidade total e quantidade livre. Não devolve nome de cliente, valor, documento nem festa.
- **Endpoint na Vercel** (um endereço do próprio sistema, tipo `GET /api/disponibilidade?data=2026-12-20`). O bot chama esse endereço com uma **chave do bot** no cabeçalho da requisição. O servidor da Vercel usa uma conexão restrita ao banco.
- A chave do bot fica como **variável de ambiente da Vercel** (um cofre de configuração do servidor), não no código do site. Pode ser trocada sem publicar o site de novo.
- A conexão usada pelo endpoint só pode **executar essa função**. Sem gravar, alterar, apagar, nem ler tabelas diretamente.
- A chave pública que o site usa fica visível no código (isso é normal). **Por isso o bot não usa essa chave.**
- Hoje o sistema não tem nenhum servidor próprio na Vercel. **(JS)** Esse endpoint é o primeiro pedaço de backend. Trabalho novo.

---

## 2) Caminho de migração (passos reversíveis)

Cada passo pode ser desfeito. Nenhum passo começa antes do anterior estar testado.

**(0) Guardar o código atual e um backup do banco. Antes de tudo.**
- O código está só no Mac e sem git (sistema de versões). Duas opções:
  - Copiar a pasta `~/projetos/os-animados/sistema` para `/workspace/os-animados-sistema`.
  - Ou o João roda `git init` no Mac (e de preferência cria um repositório privado no GitHub, para não ficar com uma cópia só).
- Backup (dump) do banco na conta certa do Supabase. **Não** a organização JOAO do CRM Blanc. A conta dos Animados se chama "PROJETOS JP" nos docs.
- Sem isso, não se mexe no banco.

**(1) Conferir a empresa Animados e preencher `empresa_id` onde faltar.**
- Ver se toda linha já tem empresa. Se faltar, preencher com a empresa Animados. Não muda o comportamento.

**(2) Regras de acesso (RLS) por empresa.**
- Conferir ou apertar as regras. Gustavo só Animados; João nas duas. Desligar cadastro aberto.
- **Testar o isolamento antes de a Turma ter qualquer dado real.** Gustavo não pode ver a Turma.

**(3) Seletor de empresa e visual da Turma.**
- Um seletor (abas) para trocar de empresa. O site passa a filtrar tudo pela empresa escolhida.
- Visual da Turma (versão V2 da marca, que está no Mac).
- Agenda da Turma com dias livres, parciais e ocupados. Depende do passo (5), então pode entrar como tela vazia até lá.

**(4) Catálogo da Turma e contrato próprio.**
- Catálogo com a tabela de 18/11 (acima).
- Contrato da Turma com texto próprio: não reaproveitar o texto dos Animados (que é do robô de LED). Cláusulas de água e energia, monitor e frete são da Turma.
- Local de residência permitido (regra por empresa).
- Pix da Turma separado do Pix dos Animados.

**(5) Estoque, reservas e consulta para o bot.**
- Tabelas de brinquedos e reservas, regra de disponibilidade, função de leitura e endpoint da Vercel.
- Testes: festa cancelada libera o brinquedo; pacote reserva os itens certos; o bot não enxerga dados de outra empresa.
- **Só em teste. Nenhum deploy em produção sem o OK do João.**

### Ambiente de teste
O João está no limite de 2 projetos grátis do Supabase. **Não criar branch nem projeto pago sem o OK dele.** Opções:
- (a) Branch de teste do Supabase, se o João aceitar o custo.
- (b) Preview da Vercel (deploy sem `--prod`, que não vai para o site oficial) apontando para uma cópia do banco.
- (c) Se não houver teste separado: passos (1) e (2) em horário combinado, com dump feito à mão e rollback escrito. O seletor (passo 3) só em preview até o OK.

---

## 3) Riscos para os Animados

| O que pode quebrar | Como testar | Como voltar atrás |
|---|---|---|
| Financeiro misturado (festa da Turma aparecer nos Animados, ou o contrário) | Entrar com as duas contas e conferir totais de uma festa antiga | Dump do banco |
| RLS travando acesso do João ou do Gustavo aos dados atuais | Login dos dois, cada um nas abas que deve ver | Voltar as regras antigas (guardadas no passo 0) |
| Contrato saindo com marca, cláusula ou dados da contratada errados | Gerar contrato de uma festa antiga e comparar com o PDF anterior | Rollback do site |
| Política do salão bloqueando festa da Turma | Salvar festa da Turma sem nome de salão | Regra por empresa |
| `salvar_contrato` e `importar_local` sem respeitar a empresa | Testar cada uma com as duas empresas | Dump; não usar até corrigir |
| Chave do bot com permissão além da leitura | Tentar gravar, apagar e ler tabelas com a chave do bot (tem que falhar) | Trocar a chave na Vercel |
| Testes de cálculo quebrando | Rodar `node tests/calc.test.mjs` (na pasta do Mac) | Git |

**Rollback do site:** o último deploy de produção é de **28/09/2026 14:18** (horário de Brasília), id `dpl_A1EhpNE2VMHCSZ7Ga7grsxKwAhN2`. É o candidato para voltar, se preciso. Dois deploys anteriores também estão prontos.

---

## 4) O que falta para começar

- [ ] Pasta do Mac: `~/projetos/os-animados/sistema` inteira, principalmente `docs/schema-cloud.sql` e `tests/`.
- [ ] Visual V2 da Turma: `~/projetos/turma-animada/marca/design-system/`.
- [ ] A tabela oficial de preços (18/11) já está no caderno. Se quiser no contrato/agenda: fotos, medidas e textos que estejam no Mac. A quantidade física é o item abaixo.
- [ ] Acesso à conta Supabase onde está o projeto dos Animados. O conector atual não enxerga esse projeto.
- [ ] Quantidade de cada brinquedo (futebol, tobogã, pula-pula 2,44 m, pula-pula 3,05 m).
- [ ] Frete do centro de Itaguaí.
- [ ] Pix separado para a Turma.
- [ ] Confirmação: Gustavo só nos Animados; João nas duas.
- [ ] OK do João para o ambiente de teste (e o custo, se houver branch).
- [ ] Git + dump feitos antes de qualquer mudança.

---

## 5) Tamanho estimado (P/M/G)

| Passo | Tamanho | Por quê |
|---|---|---|
| (0) Git + dump | P | Trabalho manual, sem código |
| (1) Empresa e `empresa_id` | P (se o schema já estiver pronto) / M (se faltar coluna ou regra) | Depende do `schema-cloud.sql` |
| (2) RLS e isolamento | M | Risco alto, trabalho curto mas cuidadoso |
| (3) Seletor e visual da Turma | M | Mexe em todas as telas |
| (4) Catálogo e contrato da Turma | M | Preço de último caso, frete, contrato próprio |
| (5) Estoque, reservas e consulta do bot | M | **Trabalho novo** (primeiro backend) |

**Conjunto:** M, se o `schema-cloud.sql` confirmar o que os docs dizem. Vira G se o banco for diferente do que os docs descrevem, ou se `salvar_contrato` não separar as empresas de verdade.

**Número de festas:** não sabemos quantas festas existem hoje. Não houve consulta ao banco.
