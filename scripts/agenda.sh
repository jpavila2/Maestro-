#!/bin/zsh
# Agenda do João para o Maestro.
# Uso:
#   scripts/agenda.sh [dias]       -> eventos de hoje até +dias (padrão 2) em: pessoal, VISITA (Blanc), blancofficeeventos
#   scripts/agenda.sh marcar "<título>" <inicio ISO> <fim ISO> ["descrição"]
#        -> cria evento SÓ na agenda pessoal (ex.: 2026-11-06T08:30:00-03:00)
# Agendas do Blanc: SOMENTE LEITURA (quem alimenta são as vendedoras).
PY=$(ls ~/.hermes/installs/*/environments/*/venv/bin/python | tail -1)
G=~/.hermes/skills/productivity/google-workspace/scripts/google_api.py

if [[ "$1" == "marcar" ]]; then
  "$PY" "$G" calendar create --calendar primary --summary "$2" --start "$3" --end "$4" ${5:+--description "$5"}
  exit
fi

DIAS=${1:-2}
INI=$(date -v0H -v0M -v0S +%Y-%m-%dT%H:%M:%S-03:00)
FIM=$(date -v+${DIAS}d -v23H -v59M -v0S +%Y-%m-%dT%H:%M:%S-03:00)
for cal in "primary|Pessoal" "blanchousecasadefesta@gmail.com|Blanc VISITA" "blancofficeeventos@gmail.com|Blanc eventos"; do
  id=${cal%%|*}; nome=${cal##*|}
  echo "## $nome"
  "$PY" "$G" calendar list --calendar "$id" --start "$INI" --end "$FIM" --max 50 2>&1 | python3 -I -c '
import json,sys
raw=sys.stdin.read()
try: evs=json.loads(raw)
except Exception: print("  (erro ao ler:", raw[:200].strip(), ")"); sys.exit()
if not evs: print("  (nada)")
for e in evs:
    s=e.get("start",""); s=s.get("dateTime",s.get("date","")) if isinstance(s,dict) else s
    print("  ", s[:16].replace("T"," "), "|", e.get("summary","(sem título)"), ("| "+e["location"]) if e.get("location") else "")'
done
