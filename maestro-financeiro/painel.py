#!/usr/bin/env python3
"""
painel.py — UM comando só faz tudo.

    python3 painel.py

O que ele faz sozinho:
  1. Procura extratos novos do Nubank na sua pasta Downloads e traz pra ca
  2. Le e categoriza tudo (mesmo motor do importar_extrato.py)
  3. Sobe o servidor local
  4. Abre o painel no seu navegador automaticamente

A unica coisa que VOCE faz: exportar o extrato no Nubank (que exige seu login)
e deixar o arquivo baixado. O resto e esse comando.
"""

import glob
import http.server
import os
import shutil
import socket
import socketserver
import threading
import webbrowser

import importar_extrato

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXTRATOS_DIR = os.path.join(BASE_DIR, "extratos")


def pegar_de_downloads():
    """Move extratos do Nubank que estiverem na pasta Downloads para extratos/."""
    downloads = os.path.expanduser("~/Downloads")
    if not os.path.isdir(downloads):
        return

    padroes = ["NU_*.csv", "Nubank*.csv", "nubank*.csv", "extrato*.csv", "*.ofx"]
    movidos = 0
    for padrao in padroes:
        for caminho in glob.glob(os.path.join(downloads, padrao)):
            destino = os.path.join(EXTRATOS_DIR, os.path.basename(caminho))
            try:
                shutil.move(caminho, destino)
                print(f"  trouxe da Downloads: {os.path.basename(caminho)}")
                movidos += 1
            except Exception as e:
                print(f"  (nao consegui mover {os.path.basename(caminho)}: {e})")
    if not movidos:
        print("  (nenhum extrato novo na Downloads — usando o que ja esta em extratos/)")


def porta_livre(inicial=8000):
    """Acha uma porta livre a partir de 'inicial' (caso 8000 ja esteja em uso)."""
    for porta in range(inicial, inicial + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", porta)) != 0:
                return porta
    return inicial


def main():
    os.makedirs(EXTRATOS_DIR, exist_ok=True)

    print("1/3  Procurando extratos novos na pasta Downloads...")
    pegar_de_downloads()

    print("2/3  Lendo e categorizando...")
    importar_extrato.salvar(importar_extrato.coletar())

    print("3/3  Abrindo o painel...")
    os.chdir(BASE_DIR)
    porta = porta_livre(8000)
    url = f"http://localhost:{porta}/dashboard_simples.html"
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    print(f"\n>>> Painel aberto em: {url}")
    print(">>> Deixe esta janela aberta. Para encerrar, aperte Ctrl+C.\n")

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", porta), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nPainel encerrado. Ate a proxima!")


if __name__ == "__main__":
    main()
