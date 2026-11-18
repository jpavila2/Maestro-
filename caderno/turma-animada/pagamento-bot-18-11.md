# Pagamento do bot da Turma Animada — pesquisa 18/11/2026

Só pesquisa. Nada foi cadastrado, ninguém foi contactado e nenhuma conta bancária foi acessada. Fontes oficiais primeiro; o que não é público está marcado como tal.

**Contexto:** a Turma Animada (aluguel de brinquedos e festas infantis, Itaguaí/RJ) é Empresário Individual/MEI, CNPJ 47.094.191/0001-61. O bot de WhatsApp deve mandar um Pix ou um link de pagamento e reconhecer sozinho quando o dinheiro entrou, para subir a festa na agenda.

**Aviso:** a conta Sicoob que o João já usa (CNAB 240 do Blanc) é de outra empresa. A regra do Banco Central é que a credencial da API Pix fica presa ao CPF/CNPJ do dono da conta. A Turma precisaria de conta no próprio CNPJ. Essa credencial do Blanc não serve para a Turma.

O bot precisa de três coisas: criar uma cobrança com identificador único, mandar o Pix copia e cola ou o link no WhatsApp, e só então marcar a festa como paga — depois de conferir no sistema do recebedor, nunca por comprovante enviado pelo cliente.

## 1) Sicoob — API Pix

O Sicoob oferece a API **Pix Recebimentos**, no padrão do Banco Central: cobrança imediata (`cob`, com `txid`), cobrança com vencimento (`cobv`) e webhook de Pix recebido. A cartilha oficial lista gerar QR Code, alterar ou cancelar cobrança, conciliar e devolver. O caminho oficial é o [Portal Developers](https://developers.sicoob.com.br/portal/), e a cooperativa precisa liberar o produto.

**Requisitos (o que é oficial):**
- Ser cooperado pessoa jurídica e ter conta no Sicoob no CNPJ da Turma, com chave Pix. MEI pode abrir conta, presencialmente na cooperativa. A disponibilidade das APIs deve ser confirmada na cooperativa da conta.
- Cadastrar a aplicação no Portal Developers, em ambiente logado do banco. O manual do BCB exige isso, e a credencial (`client_id`) fica vinculada ao CNPJ.
- Autenticação no padrão da API Pix: OAuth 2.0 no fluxo *client credentials*, com TLS mútuo (mTLS) e certificado que não pode ser autoassinado. Quem emite o certificado (o próprio banco ou uma autoridade certificadora) é definido por cada banco. A página oficial de certificado do Sicoob existe ([documentação de certificado](https://developers.sicoob.com.br/portal/documentacao?slugItem=seguranca&slugSubItem=certificado-digital)), mas o portal é uma aplicação que pede cadastro: esta pesquisa não entrou na conta e não leu o detalhe interno (se o Sicoob exige e-CNPJ A1 ICP-Brasil, certificado próprio do banco, ou os dois).
- Escopos da API Pix (padrão BCB): `cob`, `cobv`, `pix`, `webhook` (leitura e escrita, conforme o que for liberado).
- Há ambiente de documentação e, em geral, um sandbox no portal. O funcionamento exato do sandbox do Sicoob não foi confirmado aqui, porque a documentação completa fica atrás do login.

**Webhook:**
- No padrão BCB, o recebedor cadastra uma URL com `PUT /webhook/{chave}`. Só entram Pix ligados a um `txid`. Pix solto na chave, sem cobrança, não dispara aviso.
- O canal do webhook, no regulamento, **usa mTLS**. Ou seja, o endpoint do bot (n8n ou servidor Node) precisa aceitar certificado mútuo, não basta uma URL HTTPS aberta. O certificado pode ser o mesmo da API, ou outro combinado com o banco.
- O aviso do webhook não basta sozinho: o desenho seguro é o webhook avisar e o sistema confirmar a cobrança com `GET /cob/{txid}` (status `CONCLUIDA`) ou `GET /pix?txid={txid}`.

**Custo:**
- O Sicoob anuncia **“sem custos adicionais para cooperados”** para usar as APIs. Isso não é a tarifa do Pix recebido.
- Para pessoa física, o Pix no Sicoob é isento. **Para empresa, a tarifa segue a tabela de cada cooperativa.** Não existe uma tarifa única pública do Sicoob. Exemplos de outras cooperativas (não são a da Turma): uma cobra 0,10% no Pix recebido, com mínimo de R$ 0,50 e máximo de R$ 30. A da Turma só a cooperativa dela informa.
- Certificado e-CNPJ A1 (se o Sicoob pedir um ICP-Brasil): não há tabela oficial do governo (o ITI não fixa preço). Em lojas de certificadoras consultadas em 19/10/2026, o A1 de 12 meses aparecia em geral entre cerca de R$ 200 e R$ 275; ofertas para MEI/PME saíam mais baixas, a partir de cerca de R$ 130–150.

**Esforço:** médio-alto. Conta no CNPJ da Turma, conversa com a cooperativa, certificado, mTLS no servidor e no webhook, cadastro no portal e homologação. O dinheiro cai direto na conta Sicoob da Turma.

## 2) InfinitePay — Checkout Integrado (não o “Link de Pagamento” do app)

O produto certo para o bot é o **Checkout Integrado**, que cria um link pela API e aceita Pix e cartão. O “Link de Pagamento” feito no aplicativo **aceita só cartão, sem Pix**. A Loja Online também aceita Pix, mas é vitrine, não API para o bot.

**Como liga:**
- Conta InfinitePay com CNPJ/MEI (app ou site). Pede CNPJ ativo, CPF do representante (que precisa ser sócio; no MEI, o titular), validação de identidade no app e análise. A resposta costuma sair na hora; em alguns casos, até 2 dias úteis.
- Ligar “Habilitar Checkout Integrado” e, se quiser as opções avançadas, criar uma API Key (`inchk_…`) só no servidor. Sem a chave, identifica a conta pela InfiniteTag (`handle`), sem o `$`.
- Não exige certificado digital nem cadastro em portal de banco.
- O servidor faz `POST https://api.checkout.infinitepay.io/links` com os itens (preço em centavos) e um `order_nsu` (número do pedido). A resposta traz a URL do checkout. O cliente paga numa página da InfinitePay (Pix copia e cola ou cartão) e pode voltar para uma `redirect_url`.
- Dá para limitar o link a um único pagamento (`single_payment`) e pôr validade (`valid_until`).
- **Não dá para desligar o cartão.** O checkout sempre oferece crédito em até 12x; o que se escolhe é se o Pix entra ou não.
- Não existe ambiente de teste. O caminho oficial é uma compra real de R$ 1,00 e, se quiser, estorno pelo app. Estorno não existe pela API, só no app ou na Conta Web.

**Webhook e confirmação:**
- No pedido do link, envia-se uma URL HTTPS e os eventos (`paid`, `settled`, `canceled`, `refunded`, `payment_failed`, `created`).
- Responder 200 depressa. Fora de 2xx, a InfinitePay tenta de novo.
- **O webhook não tem assinatura.** A orientação oficial é: o webhook só avisa; o servidor confirma com `POST https://api.checkout.infinitepay.io/payment_check` e só libera o pedido quando a resposta vier `paid: true`. A própria InfinitePay escreve que comprovante enviado pelo cliente não prova que o Pix caiu.

**Custo e prazo (consulta em 18/11/2026):**
- Integrar é grátis: sem mensalidade e sem taxa de implementação.
- **Pix: taxa 0%**, e o valor cai na hora, inclusive à noite, fim de semana e feriado.
- No cartão, valem as taxas do Link de Pagamento (tabela própria, que no plano de 1 dia útil **não muda com o faturamento**). No plano “em 1 dia útil”, crédito à vista está em **4,20%** (Visa, Mastercard, Elo e Amex), com antecipação das parcelas já incluída; 12x, 16,66%. No InfiniteNitro (receber na hora), crédito à vista está em 5,99%.
- O dinheiro entra na conta InfinitePay, não na conta Sicoob. Tirar para o banco é um passo à parte (esta pesquisa não fechou a tarifa desse saque).

**Esforço:** baixo. Uma chamada HTTP no n8n ou no Node, um endpoint HTTPS para o webhook e a confirmação pelo `payment_check`. Sem certificado e sem liberação de cooperativa.

## 3) Comparativo

| | Sicoob (API Pix) | InfinitePay (Checkout Integrado) |
|---|---|---|
| **Requisitos** | Conta PJ/MEI no Sicoob no CNPJ da Turma, chave Pix, liberação da cooperativa | Conta InfinitePay CNPJ/MEI, Checkout Integrado ligado; análise de cadastro |
| **Certificado** | Sim: mTLS na API e no webhook, no padrão BCB. Tipo exato (e-CNPJ A1 ou certificado do banco) só o portal/cooperativa confirma | Não |
| **Cadastro de desenvolvedor** | Portal Developers, aplicação, `client_id` e escopos, em ambiente logado | API Key ou InfiniteTag no app/web; pronto na hora |
| **Custo** | Uso da API: o Sicoob diz que não há custo extra para cooperado. Tarifa do Pix recebido: **varia por cooperativa** (não inventar). Certificado A1, se for o caso: cerca de R$ 130 a R$ 275/ano | Pix 0%. Cartão: 4,20% à vista no plano D+1. Sem mensalidade |
| **Webhook** | Padrão BCB, só Pix com `txid`; canal com mTLS; confirmar com `GET /cob/{txid}` | HTTPS simples, sem assinatura; confirmar com `payment_check` (`paid: true`) |
| **Esforço** | Médio-alto (conta, cooperativa, certificado, mTLS) | Baixo (API Key + 2 endpoints) |
| **Onde o dinheiro cai** | Conta Sicoob da Turma, na hora | Conta InfinitePay; Pix na hora, cartão conforme o plano |
| **O que o cliente recebe** | QR / Pix copia e cola da cobrança (`cob` ou `cobv`) | Link de checkout (Pix e, sempre, cartão) |

## 4) Qual é mais simples, e a recomendação

**Para ligar o bot (n8n ou servidor Node), a InfinitePay é mais simples.** Não pede certificado, mTLS nem aprovação de cooperativa. São duas chamadas HTTP e um webhook. O Pix é grátis e cai na hora. A própria documentação já manda confirmar o pagamento no `payment_check` e não confiar em comprovante.

O Sicoob é o caminho mais “de banco”: o dinheiro cai na conta da Turma, a cobrança usa `txid` oficial e a tarifa do Pix, se houver, tende a ser bem menor que a de cartão. O preço é o tempo de abertura de conta, liberação da cooperativa e a infraestrutura de certificado. A conta Sicoob do Blanc não encurta esse caminho.

**Recomendação:** começar o bot pela **InfinitePay Checkout Integrado**, com Pix (e cartão, que não dá para desligar). Usar `order_nsu` único por festa, `single_payment` e validade no link. O webhook avisa; o bot só sobe a festa na agenda depois do `payment_check` com `paid: true`.

O Sicoob fica como evolução, se a Turma abrir conta no próprio CNPJ e quiser o dinheiro caindo direto no banco, sem passar pela InfinitePay. Não misturar as duas contas nem reutilizar credencial do Blanc.

Para o sinal da festa, a cobrança imediata (`cob` no Sicoob, ou o link da InfinitePay) é o suficiente. A cobrança com vencimento (`cobv`) pode servir depois para o saldo, se for o caso.

## 5) Riscos (valem para os dois)

- **Nunca** confirmar pagamento por comprovante, print ou PDF enviado pelo cliente. Pode ser falso ou de um Pix que depois não cai.
- Tratar o webhook como aviso, não como verdade. Confirmar na API (`GET /cob/{txid}` ou `payment_check`).
- **Idempotência:** um `txid` ou `order_nsu` por festa; gravar também o `endToEndId` (Sicoob/BCB) ou o `transaction_nsu` (InfinitePay); se o mesmo aviso chegar duas vezes, não subir a festa de novo.
- Webhook falha. Precisa de uma checagem periódica das cobranças ainda abertas.
- No Sicoob, Pix recebido direto na chave, sem `txid`, não gera webhook e não amarra a festa.
- No cartão da InfinitePay, existe estorno e o prazo de arrependimento do CDC (7 dias, em compras à distância). Pix cai na hora e, em regra, não se cancela depois; devolução é um passo à parte.
- Sem sandbox oficial na InfinitePay: o primeiro teste é uma cobrança real de R$ 1,00.

## Fontes (consultadas em 18/11/2026)

**Banco Central**
- [Manual de Padrões para Iniciação do Pix, v. 2.10.0](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf) — `txid`, `cob`/`cobv`, webhook só com `txid`, OAuth + mTLS, webhook em canal mTLS. Versão divulgada pela IN BCB nº 769, de 19/08/2026.

**Sicoob**
- [Portal Developers](https://developers.sicoob.com.br/portal/) e [documentação da API Pix](https://developers.sicoob.com.br/portal/documentacao?slugItem=apis&slugSubItem=pix) (conteúdo interno exige cadastro; não foi acessado).
- [Certificado digital no portal](https://developers.sicoob.com.br/portal/documentacao?slugItem=seguranca&slugSubItem=certificado-digital) (mesma ressalva).
- [Portal para desenvolvedores](https://www.sicoob.com.br/web/sicoob/servicos-empresa/-/asset_publisher/lPNqdz0jZZX1/content/id/166036588) — APIs, inclusive Pix Recebimentos; “sem custos adicionais para cooperados”; produto para cooperado PJ; confirmar na cooperativa.
- [Cartilha API de Recebimento Pix](https://www.sicoob.com.br/documents/6320214/0/cartilha_api_recebimento_pix.pdf/cdc3b117-e8f3-0167-b4ad-e966e8a1c04d) — o que a API faz; “procure a sua cooperativa”.
- [Pix no Sicoob](https://www.sicoob.com.br/web/sicoobintegracao/pix) — PF isento; PJ conforme a cooperativa.
- Exemplo de que a tarifa muda (não é a tabela da Turma): [tarifas PJ de uma cooperativa, CIC 224/2026](https://www.sicoob.com.br/documents/d/sicoobcrediconquista/cic-224-anexo-tarifas-pj-3226-2026-pix?download=true).

**InfinitePay**
- [Documentação do Checkout](https://www.infinitepay.io/checkout-documentacao)
- [Como usar o Checkout Integrado](https://ajuda.infinitepay.io/pt-BR/articles/10766888-como-usar-o-checkout-integrado-da-infinitepay)
- [Integração em 5 passos](https://www.infinitepay.io/blog/integracao-infinitepay) — webhook sem assinatura; `payment_check`; crédito à vista D+1 a 4,20%; sem ambiente de teste.
- [Como aceitar Pix no site](https://www.infinitepay.io/blog/como-aceitar-pix-no-site) — Link de Pagamento do app não aceita Pix; comprovante do cliente não é prova; Pix cai na hora.
- [Taxas](https://www.infinitepay.io/taxas) e [taxas do Link de Pagamento](https://ajuda.infinitepay.io/pt-BR/articles/4800276-quais-sao-as-taxas-do-link-de-pagamento)
- [Cadastro](https://ajuda.infinitepay.io/pt-BR/articles/4844473-como-faco-o-meu-cadastro-na-infinitepay) e [conta PJ/MEI](https://ajuda.infinitepay.io/pt-BR/articles/8177697-como-criar-um-cadastro-de-pessoa-juridica)

**Certificado e-CNPJ A1 (faixa de mercado, não é tabela oficial)**
- Consulta a lojas da Valid, Certisign e Soluti em 19/10/2026, que também registra que o ITI não fixa preço: [Via Business](https://blog.viabusiness.com.br/quanto-custa-certificado-digital-e-cnpj/). Oferta MEI, exemplo: [Imprensa Oficial do RJ](https://certificadodigital.ioerj.com.br/empresas-ei-epp-me-e-mei/).
