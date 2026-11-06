#!/usr/bin/env python3
"""Modelo C: prepara sem enviar; envia somente rascunho conferido pelo João."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

CONFIG = Path.home() / '.hermes/maestro-compras.json'
DRAFTS = Path.home() / '.hermes/compras-pendentes'


def canonical(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()


def digest(data):
    return hashlib.sha256(canonical(data)).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prepare = commands.add_parser('preparar')
    prepare.add_argument('--dados', required=True, help='JSON: contract_id, event_date, purchase_date, supplier, total_centavos, notes')
    prepare.add_argument('--foto', required=True)
    send = commands.add_parser('enviar')
    send.add_argument('--rascunho', required=True)
    send.add_argument('--hash-aprovado', required=True)
    send.add_argument('--mensagem-aprovacao', required=True, help='ID da mensagem do João autorizando este resumo')
    send.add_argument('--confirmar', action='store_true')
    args = parser.parse_args()
    if args.command == 'preparar':
        data = json.loads(Path(args.dados).read_text())
        allowed = {'contract_id', 'event_date', 'purchase_date', 'supplier', 'total_centavos', 'notes'}
        if set(data) - allowed:
            raise ValueError('Campos inesperados no JSON de dados.')
        required = allowed - {'notes'}
        if not required <= set(data):
            raise ValueError('Faltam campos obrigatórios no JSON.')
        if type(data['total_centavos']) is not int or not 1 <= data['total_centavos'] <= 10000000:
            raise ValueError('Valor inválido: informe centavos inteiros.')
        photo = Path(args.foto)
        if not 0 < photo.stat().st_size <= 2 * 1024 * 1024:
            raise ValueError('Foto deve ter até 2 MiB; reduza a imagem antes de preparar.')
        mime = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp'}.get(photo.suffix.lower())
        if not mime:
            raise ValueError('Use foto JPG, PNG ou WebP.')
        data.update(mimetype=mime, base64=base64.b64encode(photo.read_bytes()).decode())
        fingerprint = digest(data)
        DRAFTS.mkdir(parents=True, exist_ok=True, mode=0o700)
        target = DRAFTS / (fingerprint + '.json')
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, 'w') as stream:
            json.dump(data, stream, ensure_ascii=False)
        print(json.dumps({'enviado': False, 'rascunho': str(target), 'hash_aprovado': fingerprint,
                          'resumo': {k: v for k, v in data.items() if k not in ('base64', 'mimetype')}}, ensure_ascii=False))
        return
    if not args.confirmar or not args.mensagem_aprovacao.strip():
        raise ValueError('Exige --confirmar e ID da mensagem de aprovação do João.')
    data = json.loads(Path(args.rascunho).read_text())
    if digest(data) != args.hash_aprovado:
        raise ValueError('Rascunho mudou. Mostre o resumo atualizado e peça nova aprovação.')
    config = json.loads(CONFIG.read_text())
    endpoint = config.get('endpoint', '')
    from urllib.parse import urlparse
    if urlparse(endpoint).scheme != 'https' or not endpoint.endswith('/api/maestro-compra'):
        raise ValueError('Configure endpoint HTTPS terminado em /api/maestro-compra.')
    token = config.get('token', '')
    if len(token) < 32:
        raise ValueError('Token da integração ausente/inválido.')
    data['approval'] = {'confirmed': True, 'message_id': args.mensagem_aprovacao}
    request = urllib.request.Request(endpoint, data=canonical(data), method='POST',
        headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token})
    # Não segue redirecionamentos com credencial da integração.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **kw):
            return None
    try:
        with urllib.request.build_opener(NoRedirect).open(request, timeout=55) as response:
            result = json.load(response)
    except urllib.error.HTTPError as error:
        print(error.read(4096).decode(errors='replace'), file=sys.stderr)
        sys.exit(1)
    except (TimeoutError, urllib.error.URLError):
        raise ValueError('Resultado incerto. Reenvie o mesmo rascunho e a mesma mensagem de aprovação; não prepare nova nota.')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        print('Erro: ' + str(error), file=sys.stderr)
        sys.exit(1)
