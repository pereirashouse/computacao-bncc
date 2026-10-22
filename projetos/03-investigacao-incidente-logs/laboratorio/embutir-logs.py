"""Copia os arquivos de ../logs/ para dentro do index.html.

A página precisa funcionar aberta direto do pendrive (sem servidor), e o
navegador não deixa uma página local ler outros arquivos. Por isso os logs
ficam embutidos. Depois de editar algum arquivo em ../logs/, rode:

    python3 embutir-logs.py
"""
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
LOGS = AQUI.parent / "logs"
PAGINA = AQUI / "index.html"

dados = {p.name: p.read_text(encoding="utf-8") for p in sorted(LOGS.iterdir()) if p.is_file()}
bloco = json.dumps(dados, ensure_ascii=False, indent=1).replace("</", "<\\/")
html = PAGINA.read_text(encoding="utf-8")
novo, n = re.subn(r"/\*LOGS:INICIO\*/.*?/\*LOGS:FIM\*/", lambda _: f"/*LOGS:INICIO*/{bloco}/*LOGS:FIM*/", html, flags=re.S)
if n != 1:
    raise SystemExit("Marcadores LOGS:INICIO/LOGS:FIM não encontrados no index.html")
PAGINA.write_text(novo, encoding="utf-8")
print(f"{len(dados)} arquivos embutidos em {PAGINA.name}")
