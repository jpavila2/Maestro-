# 🔄 RETOMAR — Maestro (centro de comando / "Jarvis")

Ponto de entrada pra continuar de onde parou — conta nova do Claude, Codex ou outra máquina.
> Num agente novo: **"Leia o RETOMAR.md e continue de onde parei."**

## 1. O que é
**Maestro** = monorepo pessoal do João, o "Jarvis" que vai orquestrar todas as automações.
Cada subsistema = uma pasta na raiz. Índice completo no `README.md`.
- **GitHub:** jpavila2/maestro- (branch `claude/banco-mcp-integrador-9qnk1x`)
- **Importante sobre o João:** NÃO é dev — está aprendendo. Sempre explicar didaticamente o quê/por quê/qual ferramenta, com analogias. (Ver `maestro-financeiro/CLAUDE.md`.)

## 2. Subsistemas
| Pasta | O que é | Status | Retomar |
|---|---|---|---|
| `maestro-financeiro/` | Painel que lê extrato do banco (CSV/OFX), categoriza e mostra saldo/gráficos | ✅ funcionando | `maestro-financeiro/RETOMAR.md` |
| `banco-mcp-integrador/` | Integração de banco via MCP | 🔜 inicial | (sem RETOMAR ainda) |

## 3. Estado atual (ATUALIZAR ao concluir etapas)
- 🔜 **EM ANDAMENTO:** sistema financeiro é o primeiro pilar. Caminho grátis: arrastar extrato do Nubank no `dashboard_simples.html`.
- Próximas ideias: conectar banco real (sair do sandbox), painel mais rico (evolução mensal/metas), interface por WhatsApp.

## 4. Regras de ouro
- Explicar didaticamente cada passo (o João está aprendendo).
- Audite antes de alterar dados; nada de escrita em massa sem mostrar os números.
- Ao terminar uma etapa: marque `[x]` no plano do subsistema e atualize esta seção.

## 5. Como retomar (cole num agente novo)
```
Estou continuando o Maestro. Leia RETOMAR.md na raiz e o README (índice de subsistemas).
Entre no subsistema em andamento (ver "Estado atual"), leia o RETOMAR.md dele e continue
do primeiro passo não marcado. Explique cada passo de forma didática — não sou dev.
```
