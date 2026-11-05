#!/bin/zsh
# Liga o Gmail do João ao Maestro (Hermes) com permissão SOMENTE LEITURA.
# A chave secreta é digitada aqui no terminal e vai direto pro arquivo do Hermes:
# nenhum agente de IA vê o valor.
set -e
PY=$(ls ~/.hermes/installs/*/environments/*/venv/bin/python | tail -1)
SKILL=~/.hermes/skills/productivity/google-workspace/scripts

echo "1) Cole o ID do cliente (termina em .apps.googleusercontent.com) e aperte Enter:"
read cid
echo "2) Cole a Chave secreta do cliente (começa com GOCSPX-). Ela NÃO aparece na tela. Aperte Enter:"
read -s sec
echo

TMP=$(mktemp)
chmod 600 "$TMP"
CID="$cid" SEC="$sec" "$PY" -I -c '
import json, os, sys
json.dump({"installed": {
  "client_id": os.environ["CID"].strip(),
  "client_secret": os.environ["SEC"].strip(),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "redirect_uris": ["http://localhost"]}}, open(sys.argv[1], "w"))
' "$TMP"
unset sec

READONLY='import sys; sys.path.insert(0, sys.argv[1]); import setup; setup.SCOPES=["https://www.googleapis.com/auth/gmail.readonly"]'

"$PY" -c "$READONLY; setup.store_client_secret(sys.argv[2])" "$SKILL" "$TMP"
rm -f "$TMP"
chmod 600 ~/.hermes/google_client_secret.json

URL=$("$PY" -c "$READONLY; setup.get_auth_url()" "$SKILL" | tail -1)
echo
echo "3) Vou abrir a autorização do Google no seu navegador."
echo "   Confira: deve pedir SÓ pra 'ver seus e-mails'. Clique em Continuar/Permitir."
echo "   No final a página vai dar erro em 'localhost' — isso é normal."
open "$URL"
echo
echo "4) Copie o endereço INTEIRO da barra do navegador (começa com http://localhost) e cole aqui:"
read cb
"$PY" -c "$READONLY; setup.exchange_auth_code(sys.argv[2])" "$SKILL" "$cb"
chmod 600 ~/.hermes/google_token.json 2>/dev/null || true
echo
echo "Pronto. Pode voltar pro chat e avisar o Claude."
