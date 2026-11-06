# Compras pelo Maestro — modelo C

## Regra de operação (instrução para agentes)

O script é `scripts/maestro-compra.py`. Preparar não envia. Enviar grava no CRM.
Só enviar após aprovação explícita do João referente ao resumo ATUAL de uma nota.
Antes de pedir aprovação, mostrar festa/data, fornecedor, data da compra, valor destinado
à festa e itens excluídos/pessoais. Resolver qualquer ⚠️ antes de enviar.
Não interpretar aprovação da implementação como aprovação de notas. Não processar lote
sem o João conferir os valores de todas as notas. Não usar cron para enviar compras.

1. Ler todas as fotos e registrar no arquivo da festa. Associar a foto original correta.
2. Obter UUID e data do contrato previamente conferidos no CRM. Nunca escolher pela data
   sozinha, inventar UUID ou entregar login/service role ao Maestro.
3. Criar JSON com `contract_id`, `event_date`, `purchase_date` (datas AAAA-MM-DD),
   `supplier`, `total_centavos` (inteiro) e `notes` (itens excluídos/observações).
4. Preparar: `python3 scripts/maestro-compra.py preparar --dados <dados.json> --foto <foto.jpg>`.
   Rascunho privado fica em `~/.hermes/compras-pendentes/`; saída informa resumo e hash.
5. Mostrar resumo ao João. Só após “pode lançar” explícito, guardar o ID dessa mensagem
   junto do hash e caminho do rascunho no registro da festa.
6. Enviar: `python3 scripts/maestro-compra.py enviar --rascunho <caminho> --hash-aprovado <hash> --mensagem-aprovacao <id> --confirmar`.
7. Só dizer lançado se a saída indicar `ok: true`. Registrar IDs retornados no arquivo
   da festa. `duplicate: true` é confirmação do lançamento existente, sem nova compra.
8. Em timeout ou resposta incerta, reenviar o MESMO rascunho, hash e ID de aprovação.
   Nunca alterar a foto para contornar duplicidade. Conflito exige revisão no CRM.

## Ativação pendente

- Aplicar `blanc-house/crm/docs/migration-maestro-compras.sql` no Supabase correto.
- Vercel CRM: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` (somente servidor),
  `MAESTRO_TOKEN` (token exclusivo aleatório, pelo menos 32 caracteres).
- Configurar `~/.hermes/maestro-compras.json`, permissão 600, com `endpoint`
  (`https://crm-deploy-gamma.vercel.app/api/maestro-compra`) e `token` (mesmo MAESTRO_TOKEN).
  Não colocar segredos em chat, repositório, SOUL nem linha de comando.
- Publicar CRM e testar acesso negado sem token. Configurar UUID da festa pelo CRM.
- Só então validar a primeira nota real já conferida e autorizada pelo João.

Código preparado em 05/11; produção ainda NÃO ativada. Cinco notas de 07/11 continuam
pendentes de aprovação, inclusive os itens pessoais e a nota T&M.

Atualização de ativação: token dedicado e URL do Supabase já configurados na Vercel; arquivo privado do Hermes já existe (modo 600). Não gerar/rotacionar outro token sem necessidade. Falta acesso ao projeto Supabase, service role no servidor, migration e deploy.
