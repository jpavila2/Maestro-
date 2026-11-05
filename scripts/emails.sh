#!/bin/zsh
# Leitura do Gmail pessoal do João (SOMENTE LEITURA, token gmail.readonly).
# Uso:
#   scripts/emails.sh                -> e-mails que podem importar, últimos 3 dias (sem promoção/social)
#   scripts/emails.sh "<busca>"      -> qualquer busca do Gmail (ex.: "from:tjkseguros newer_than:30d")
#   scripts/emails.sh ler <id>       -> texto de um e-mail
# Outras contas: CONTA=blanc scripts/emails.sh ...  (pastas em ~/.hermes/gmail-contas/)
#                CONTA=todas scripts/emails.sh       -> resumo de todas as contas ligadas
if [[ "$CONTA" == "todas" ]]; then
  echo "##### CONTA pessoal"; CONTA= "$0" "$@"
  for d in ~/.hermes/gmail-contas/*(N/); do echo; echo "##### CONTA ${d:t}"; CONTA=${d:t} "$0" "$@"; done
  exit
fi
[[ -n "$CONTA" ]] && export HERMES_HOME=~/.hermes/gmail-contas/$CONTA
PY=$(ls ~/.hermes/installs/*/environments/*/venv/bin/python | tail -1)
G=~/.hermes/skills/productivity/google-workspace/scripts/google_api.py

if [[ "$1" == "ler" ]]; then
  "$PY" "$G" gmail get "$2" | python3 -I -c '
import json,sys,re
m=json.load(sys.stdin); b=m.get("body") or ""
b=re.sub(r"<style.*?</style>","",b,flags=re.S); b=re.sub(r"[^{}<>]*\{[^{}]*\}","",b)
b=re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",b)).replace("&nbsp;"," ")
print("DE:",m.get("from")); print("ASSUNTO:",m.get("subject")); print("DATA:",m.get("date")); print(b[:3000])'
  exit
fi

Q=${1:-"in:inbox newer_than:3d -category:promotions -category:social -from:me -from:aliexpress -from:tiktok.com -from:twitch.tv"}
"$PY" "$G" gmail search "$Q" --max 40 | python3 -I -c '
import json,sys
for m in json.load(sys.stdin):
    lida = "" if "UNREAD" in m.get("labels",[]) else " (lido)"
    print(m["id"], "|", m["date"][5:16], "|", m["from"][:45], "|", m["subject"][:80] + lida)
    print("   ", (m.get("snippet") or "")[:160])'
