#!/bin/zsh
# Liga OUTRA conta Gmail do João ao Maestro, SOMENTE LEITURA.
# Uso: scripts/conectar-gmail-extra.sh <apelido>     (ex.: blanc, regency, turma)
# Reaproveita o app "Maestro Mac" já configurado: não precisa colar chave de novo.
# Antes: a conta precisa estar em "Usuários de teste" no Google Cloud (projeto maestro-513800).
set -e
APELIDO="$1"
[[ -z "$APELIDO" ]] && { echo "Uso: $0 <apelido>  (ex.: blanc)"; exit 1; }
PY=$(ls ~/.hermes/installs/*/environments/*/venv/bin/python | tail -1)
SKILL=~/.hermes/skills/productivity/google-workspace/scripts
DIR=~/.hermes/gmail-contas/$APELIDO
mkdir -p "$DIR"; chmod 700 ~/.hermes/gmail-contas "$DIR"
cp ~/.hermes/google_client_secret.json "$DIR/"; chmod 600 "$DIR/google_client_secret.json"
export HERMES_HOME="$DIR"

READONLY='import sys; sys.path.insert(0, sys.argv[1]); import setup; setup.SCOPES=["https://www.googleapis.com/auth/gmail.readonly"]'
URL=$("$PY" -c "$READONLY; setup.get_auth_url()" "$SKILL" | tail -1)
echo
echo "1) Vou abrir a autorização do Google no navegador."
echo "   ATENÇÃO: na tela 'Escolha uma conta', escolha a conta '$APELIDO' (não a pessoal)."
echo "   Deve pedir SÓ pra ver os e-mails. Continuar > Permitir. O erro em 'localhost' no final é normal."
open "$URL"
echo
echo "2) Copie o endereço INTEIRO da barra (começa com http://localhost) e cole aqui:"
read cb
"$PY" -c "$READONLY; setup.exchange_auth_code(sys.argv[2])" "$SKILL" "$cb"
chmod 600 "$DIR/google_token.json" 2>/dev/null || true
echo
echo "Pronto: conta '$APELIDO' ligada. Pode voltar pro chat."
