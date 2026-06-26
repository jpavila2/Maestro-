# 🎛️ Maestro

Centro de comando pessoal — meu "Jarvis". A ideia é simples: um lugar só onde
moram todas as minhas automações e ferramentas pessoais. Cada projeto vive numa
pasta própria; com o tempo, um "regente" coordena a orquestra inteira.

> **Por que "Maestro"?** Um maestro não toca todos os instrumentos — ele
> coordena vários. É essa a proposta: orquestrar várias automações da minha
> vida pessoal num só lugar.

## 🗂️ Como este repositório é organizado

- Este é um **monorepo**: um repositório único guardando vários projetos.
- **Cada projeto = uma pasta** na raiz. Projetos diferentes ficam lado a lado,
  isolados, cada um com seu próprio `README`.
- Pra saber o que é cada um, é só ler este índice abaixo.

```
Maestro/
├── README.md               ← você está aqui (o índice)
└── banco-mcp-integrador/   ← projeto 1
```

## 📦 Projetos

| Projeto | O que faz | Status |
|---|---|---|
| [`banco-mcp-integrador`](./banco-mcp-integrador) | Puxa saldo e transações dos bancos (via Pluggy / Open Finance), já categorizados, e mostra num dashboard local | ✅ Funcionando (sandbox) |

## 🌱 Próximas ideias (a orquestra crescendo)

- Conectar o banco real (sair do sandbox)
- Painel mais rico (evolução mensal, filtros, metas)
- Interface por WhatsApp (consultar e registrar por mensagem)
- _(outras automações pessoais conforme forem surgindo)_
