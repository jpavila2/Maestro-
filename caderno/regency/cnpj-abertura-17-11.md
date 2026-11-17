# CNPJ da Regency AI — atualização de 17/11/2026

> **Decisão do João em 17/11/2026 (via Maestro):** o prazo de 19/11 para abrir a LTDA foi derrubado. A LTDA fica para quando houver fluxo de clientes. A Regency começa no MEI do João (CNPJ 47.094.191/0001-61, que hoje não emite nota) e, eventualmente, num MEI novo para o Guga. Ocupações e nota fiscal: `caderno/regency/mei-ocupacoes-17-11.md`.

> Entrega do Reg em 17/11/2026 (terça). O prazo de 19/11 para a LTDA foi derrubado no mesmo dia (ver aviso acima).
> Complementa `caderno/regency/cnpj-abertura-16-11.md`. O Reg não protocola, não paga taxa e não fala com o Guga, com o pai do João nem com contador.
> Dados pessoais sensíveis (CPF, e-mail, telefone, logradouro completo do MEI) ficam fora deste arquivo. O CNPJ e os demais dados cadastrais públicos entram aqui.

## O que mudou desde 16/11

O João, via Maestro, confirmou: o **MEI continua ativo** e a **sede da Regency será em Itaguaí/RJ**. Informou ainda o CNPJ que aparece no DAS, 47.094.191/0001-61, “supostamente” da Turma Animada. Esse número é o mesmo já anotado no fio `DAS MEI` de `caderno/fios.md` (desde 12/11).

## 1. Conferência pública do CNPJ 47.094.191/0001-61

Consultado em **17/11/2026** em duas APIs que republicam o cadastro da Receita Federal. Os campos centrais coincidiram. O comprovante oficial, se o João quiser emitir, está em [Consulta CNPJ da Receita](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/ConsultaSituacao.aspx).

Fontes:

- [BrasilAPI](https://brasilapi.com.br/api/cnpj/v1/47094191000161), consultada em 17/11/2026
- [ReceitaWS](https://www.receitaws.com.br/v1/cnpj/47094191000161), consultada em 17/11/2026 (campo `ultima_atualizacao`: 15/11/2026)

| Campo | Dado público conferido |
|---|---|
| CNPJ | 47.094.191/0001-61 (matriz) |
| Razão social | 47.094.191 JOAO PEDRO TEIXEIRA DE AVILA |
| Nome fantasia | vazio — **não aparece “Turma Animada”** no cadastro público |
| Situação cadastral | ATIVA (desde 11/07/2022) |
| Natureza jurídica | 213-5 — Empresário (Individual) |
| Porte | Microempresa |
| Simei (MEI) | optante desde 11/07/2022; sem data de exclusão |
| Simples Nacional | optante desde 11/07/2022; sem data de exclusão |
| Início de atividade | 11/07/2022 |
| Capital social | R$ 10.000,00 |
| Município da sede deste CNPJ | Itaguaí/RJ, bairro Centro, CEP 23.815-200 |
| QSA | vazio (esperado em empresário individual; a razão social identifica o titular) |

CNAE principal: **59.12-0-99** — Atividades de pós-produção cinematográfica, de vídeos e de programas de televisão não especificadas anteriormente.

CNAEs secundários:

- 74.20-0-04 — Filmagem de festas e eventos
- 43.21-5-00 — Instalações elétricas
- 47.63-6-01 — Comércio varejista de brinquedos e artigos recreativos
- 82.19-9-99 — Preparação de documentos e serviços especializados de apoio administrativo não especificados anteriormente
- 43.30-4-04 — Serviços de pintura de edifícios em geral
- 43.99-1-03 — Obras de alvenaria
- 82.30-0-01 — Serviços de organização de feiras, congressos, exposições e festas

Leitura cautelosa: o nome comercial “Turma Animada” **não está no cadastro**. Alguns CNAEs (filmagem de festas, organização de festas, comércio de brinquedos) são compatíveis com essa atividade, mas isso não prova que o CNPJ “é” a Turma Animada. O endereço completo, e-mail e telefone do cadastro não são copiados aqui.

Este CNPJ é o do MEI do João. **Não é o CNPJ da Regency** (ainda inexistente). O endereço deste MEI também **não foi escolhido** como sede da Regency — só o município (Itaguaí) está decidido.

## 2. Impacto de ser titular de MEI e sócio/administrador de uma LTDA

A vedação não é “proibido abrir a LTDA”. É **proibido permanecer no Simei** (o recolhimento em valor fixo do MEI) quem passa a participar de outra empresa como titular, sócio ou administrador.

Fontes oficiais:

- Portal do Empreendedor: [condições para ser MEI](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/quero-ser-mei/o-que-voce-precisa-saber-antes-de-se-tornar-um-mei/o-que-voce-precisa-saber-antes-de-se-tornar-mei-1/o-que-voce-precisa-saber-antes-de-se-tornar-mei) (“Você não pode ser ou se tornar titular, sócio ou administrador de outra empresa”) e [Transição do MEI para Microempresa](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/quero-crescer-desenquadramento) (motivo: “Participar de outra empresa (CNPJ) como administrador, sócio ou titular”)
- Lei Complementar nº 123/2006, art. 18-A, § 4º, III (vedação ao Simei) e § 8º (desenquadramento de ofício), conforme o [Perguntas e Respostas MEI e Simei](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoMEI.pdf) da Receita (itens 6.3 a 6.6)
- [Manual do Desenquadramento do Simei](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_DESENQUADRAMENTO_SIMEI.pdf) da Receita, itens 4.4.1, 5, 6 e 8
- Serviço [Comunicar desenquadramento do Simei](https://www.gov.br/pt-br/servicos/comunicar-desenquadramento-do-simei)

O que acontece se a Regency LTDA for aberta com o João como sócio ou administrador e o MEI ainda ativo:

1. Surge a obrigação de **comunicar o desenquadramento do Simei** no Portal do Simples Nacional, motivo “participação em outra empresa”.
2. Prazo: até o **último dia útil do mês seguinte** ao da entrada na LTDA.
3. Efeito: a partir do **primeiro dia do mês seguinte** ao da entrada — não é retroativo à data do contrato. Exemplo oficial do manual: entrou na LTDA em 15/02/2021 → efeito em 01/03/2021. Se a entrada for em novembro de 2026, o efeito é **01/12/2026** e a comunicação vai até o último dia útil de dezembro.
4. A partir dessa data, o CNPJ 47.094.191/0001-61 **deixa o Simei**, mas **em regra permanece no Simples Nacional** (sair do Simei não é sair do Simples). O DAS fixo do MEI cessa; o recolhimento passa às regras do Simples, pelo PGDAS-D. Contador entra aqui.
5. Isso **não é desenquadramento automático**. O automático (item 5 do manual) só ocorre quando o próprio MEI altera no CNPJ a natureza jurídica, inclui ocupação vedada ou abre filial. Virar sócio de *outra* empresa não altera, sozinho, o cadastro deste CNPJ.
6. Se a comunicação obrigatória não for feita no prazo: **desenquadramento de ofício** (efeitos iguais aos da comunicação) e **multa de R$ 50,00** (LC 123, art. 36-A). O Portal do Empreendedor também avisa que a Receita pode desenquadrar se a situação não for regularizada.
7. Retroatividade à data de ingresso no Simei (11/07/2022) só aparece no manual para o caso em que a vedação **já existia desde o ingresso** no regime — não é o caso típico de quem entra numa LTDA agora.

Não foi encontrada, nas fontes oficiais lidas, regra de que a JUCERJA ou a Redesim recusem o registro da LTDA só porque um sócio é MEI. O efeito documentado é a perda do Simei, não o bloqueio da nova empresa.

### Opções (o que cada uma faz de verdade)

**A. Baixar o MEI antes de entrar na LTDA.** Encerra o CNPJ 47.094.191/0001-61 no [Portal do Empreendedor](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/servicos-para-mei/baixa-de-mei) (gratuito; formalização em 11/07/2022, depois de 16/03/2022, então a conta gov.br precisa ser nível Prata ou Ouro). Depois da baixa há obrigações pós-extinção (o próprio portal aponta o que fazer; o Perguntão cita a DASN-Simei de extinção). Só faz sentido se essa atividade **não vai mais faturar** por este CNPJ. Atenção ao fio `DAS MEI` do caderno: o João quer ficar 6 meses em dia para compensar dívida ativa e já pagou o DAS de out/2026 em 17/11. O efeito da baixa (ou do desenquadramento) sobre esse plano **não está documentado aqui** — o contador precisa olhar antes.

**B. Desenquadrar o MEI para microempresa (recomendação se a atividade deste CNPJ continua).** O CNPJ permanece, sai só do Simei e, em regra, segue no Simples como empresário individual / ME, recolhendo pelo PGDAS-D. É o caminho oficial quando se “participa de outra empresa”. Pode ser feito no momento em que a vedação ocorrer (comunicação obrigatória) ou, se quiserem sair do Simei antes, por opção — mas a opção fora de janeiro só produz efeito em 1º de janeiro do ano seguinte, o que **não resolve** uma entrada na LTDA em novembro. João + Guga na Regency e este CNPJ vivo como ME é possível; o contador deve acompanhar o limite de receita bruta *global* das empresas no Simples (LC 123, art. 3º, § 4º).

**C. Guga como único sócio-administrador (SLU) “por enquanto”.** A vedação do Simei só se aplica se o João for titular, sócio **ou** administrador da outra empresa. Se ele realmente não for nenhum dos três, o MEI pode permanecer. Isso, porém, **muda quem é dono da Regency**: o combinado documentado é sociedade dos dois, e uma participação “de fato” sem constar no contrato não está no caderno e não deve ser usada só para burlar o Simei. Entrar depois exige alteração contratual. Não é a recomendação deste roteiro.

**Recomendação do Reg (para o João decidir com o contador, não um ato praticado aqui):** se este CNPJ ainda fatura (Turma Animada ou outra atividade), ir pela **opção B** — desenquadrar no prazo, manter o CNPJ, e o João entrar na LTDA como sócio. Se a atividade já acabou e o plano da dívida ativa permitir, **opção A** (baixa) deixa a LTDA mais simples. A opção C só faria sentido se os dois sócios quiserem, de propósito, uma Regency só do Guga no início — o que hoje não está decidido.

## 3. Roteiro da LTDA com sede em Itaguaí/RJ

O município da sede está decidido (Itaguaí). O **endereço completo** (logradouro, número, complemento, CEP) ainda não. Sem isso a viabilidade não anda.

A Prefeitura de Itaguaí informou em 03/09/2024 que, a partir de 01/09/2024, as análises de **alvará, alterações e baixas** passam a ser exclusivamente online no REGIN da JUCERJA, sem processo físico na prefeitura. Fonte: [REGIN — Prefeitura de Itaguaí](https://novoportal.itaguai.rj.gov.br/noticias/regin-1). Essa nota **não informa prazo** de análise e **não diz** que a viabilidade é automática.

A JUCERJA, na página [Informações sobre empresas](https://www.jucerja.rj.gov.br/Home/InformacoesEmpresas), no roteiro **“Passos para abertura de matriz e filial nos demais municípios”** (Itaguaí entra nessa categoria, não no roteiro da cidade do Rio / Carioca Digital), publica:

1. Cadastro no site da JUCERJA
2. **Pedido de viabilidade** em Serviços › REGIN › Pedido de Viabilidade. O pedido cobre atividade no endereço, disponibilidade do nome, enquadramento no Corpo de Bombeiros e restrições da SEFAZ-RJ. A Junta escreve: aguardar a **análise da prefeitura no prazo de D+2 dias úteis** (o dia do pedido + dois dias úteis). Acompanhar em “Acompanhamento do Pedido de Viabilidade”.
3. DBE / CNPJ no [Portal Redesim](https://www.gov.br/empresas-e-negocios/pt-br)
4. Protocolo Web na JUCERJA (boleto + ato constitutivo; com assinatura digital, aguarda o julgamento)
5. Depois do registro, os dados “serão enviados automaticamente para a prefeitura conceder o alvará pelo REGIN” (Acompanhamento de Alvará). A prefeitura de Itaguaí confirma que esse alvará agora corre no REGIN.
6. Certificado do Corpo de Bombeiros, conforme o relatório de viabilidade

O D+2 é o prazo **publicado pela JUCERJA** para a análise municipal da viabilidade nos demais municípios. Não foi encontrada publicação da Prefeitura de Itaguaí repetindo esse prazo, nem afirmando análise automática. Se o pedido cair em exigência ou vistoria, o calendário pode esticar — isso não está detalhado no texto municipal lido.

Demais passos (contrato social, MAT e opção pelo Simples no ato da inscrição do CNPJ) continuam como no arquivo de 16/11. Ainda faltam razão social exata, CNAEs da Regency, capital, quotas, administração, regime e contador.

## 4. O que cabe até qui 19/11 — próximo passo concreto

Hoje é **terça 17/11**. Faltam dois dias corridos. A viabilidade em Itaguaí, pelo prazo que a JUCERJA publica, leva D+2 dias úteis. Se o pedido sair **hoje**, o D+2 cai em **qui 19/11** — no limite do prazo, e ainda restariam DBE, contrato, registro na Junta e MAT. CNPJ da Regency na mão até quinta **não é realista**, a menos que endereço, nome e CNAEs já estejam prontos hoje e o deferimento saia no prazo cheio, no mesmo dia do registro. Se a viabilidade ficar para quarta 18/11, o D+2 publicado já cai em sexta 20/11, depois do prazo.

O que ainda bloqueia o protocolo de hoje: endereço completo da sede em Itaguaí, razão social a consultar (2–3 opções) e CNAEs da Regency. A decisão baixa vs. desenquadramento do MEI pode (e deve) correr em paralelo, com o contador, por causa também do plano da dívida ativa no fio do DAS.

**Próximo passo concreto (hoje, 17/11):** o João fecha o endereço completo da sede em Itaguaí e duas ou três razões sociais (a partir de “Regency AI”) e, com o contador ou sozinho no [REGIN/JUCERJA](https://www.jucerja.rj.gov.br/regin/), **protocola o pedido de viabilidade ainda hoje**. É o único passo da LTDA que ainda pode caber no D+2 publicado até quinta. O Reg não protocola.

## Pergunta única ao João

Esse CNPJ 47.094.191/0001-61 ainda fatura a Turma Animada ou outra atividade? (No cadastro público o nome fantasia está vazio.)
