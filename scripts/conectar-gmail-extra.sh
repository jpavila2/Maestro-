#!/bin/zsh
# Liga OUTRA conta Gmail do João ao Maestro, SOMENTE LEITURA.
# Uso: scripts/conectar-gmail-extra.sh <apelido> [agenda]
#   <apelido>: blanc, jpavilabtc... ou "pessoal" (a conta principal, pasta ~/.hermes)
#   [agenda]:  vazio = só e-mail | leitura = + ver agenda | escrita = + ver agenda e criar/editar eventos
# Reaproveita o app "Maestro Mac" já configurado: não precisa colar chave de novo.
# Antes: a conta precisa estar em "Usuários de teste" no Google Cloud (projeto maestro-513800).
set -e
APELIDO="$1"
[[ -z "$APELIDO" ]] && { echo "Uso: $0 <apelido>  (ex.: blanc)"; exit 1; }
PY=$(ls ~/.hermes/installs/*/environments/*/venv/bin/python | tail -1)
SKILL=~/.hermes/skills/productivity/google-workspace/scripts
if [[ "$APELIDO" == "pessoal" ]]; then
  DIR=~/.hermes
else
  DIR=~/.hermes/gmail-contas/$APELIDO
  mkdir -p "$DIR"; chmod 700 ~/.hermes/gmail-contas "$DIR"
  cp ~/.hermes/google_client_secret.json "$DIR/"; chmod 600 "$DIR/google_client_secret.json"
fi
export HERMES_HOME="$DIR"

G="https://www.googleapis.com/auth"
ESC="\"$G/gmail.readonly\""
[[ "$2" == "leitura" ]] && ESC="$ESC,\"$G/calendar.readonly\""
[[ "$2" == "escrita" ]] && ESC="$ESC,\"$G/calendar.readonly\",\"$G/calendar.events\""
READONLY="import sys; sys.path.insert(0, sys.argv[1]); import setup; setup.SCOPES=[$ESC]"
URL=$("$PY" -c "$READONLY; setup.get_auth_url()" "$SKILL" | tail -1)
echo
echo "1) Vou abrir a autorização do Google no navegador."
echo "   ATENÇÃO: na tela 'Escolha uma conta', escolha a conta '$APELIDO'."
echo "   Deve pedir SÓ: ver e-mails${2:+ e a agenda ($2)}. Continuar > Permitir. O erro em 'localhost' no final é normal."
open "$URL"
echo
echo "2) Copie o endereço INTEIRO da barra (começa com http://localhost) e cole aqui:"
read cb
"$PY" -c "$READONLY; setup.exchange_auth_code(sys.argv[2])" "$SKILL" "$cb"
chmod 600 "$DIR/google_token.json" 2>/dev/null || true
EMAIL=$("$PY" -I -c '
import sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
c=Credentials.from_authorized_user_file(sys.argv[1])
print(build("gmail","v1",credentials=c).users().getProfile(userId="me").execute()["emailAddress"])' "$DIR/google_token.json")
echo
echo "Pronto: a pasta '$APELIDO' ficou ligada à conta $EMAIL."
echo "Se não era essa conta, avise o Claude."
