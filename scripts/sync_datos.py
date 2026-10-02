#!/usr/bin/env python3
"""Sync reclamos.json desde MuchoTexto Data (datos-publicos) al sitio Jekyll.

Descarga el dataset agregado de reclamos de la Municipalidad de Asunción desde
https://github.com/miravosqueinteresante/datos-publicos y lo escribe en
`_data/reclamos.json` para que el dashboard lo consuma vía `site.data.reclamos`.

Seguridad: `_data/reclamos.json` SIEMPRE existe (snapshot commiteado). Si la
descarga falla, no sobreescribe y sale 0: el build nunca se rompe por esto.

Uso:
    python scripts/sync_datos.py              # descarga y escribe si es válido
    python scripts/sync_datos.py --local-only # no toca la red
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(REPO_DIR, "_data", "reclamos.json")

BASE_URL = "https://raw.githubusercontent.com/miravosqueinteresante/datos-publicos/main/www/datos/reclamos.json"
TIMEOUT = 60
REQUIRED_KEYS = ("_meta", "kpis", "por_anio", "por_categoria", "por_dependencia")


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "municipalidad-sync/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def valid(payload):
    if not isinstance(payload, dict):
        return False
    return all(k in payload for k in REQUIRED_KEYS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-only", action="store_true")
    args = parser.parse_args()

    if args.local_only:
        with open(OUT_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        print("Snapshot local: %d registros (sync %s)" %
              (data.get("_meta", {}).get("registros", 0),
               data.get("_meta", {}).get("sincronizado", "?")))
        return 0

    try:
        payload = fetch_json(BASE_URL)
        if not valid(payload):
            raise ValueError("Estructura invalida")
    except Exception as exc:
        print("  WARN: sync fallido (%s). Se conserva el snapshot local." % exc)
        return 0

    payload["_meta"]["sincronizado"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("OK: _data/reclamos.json = %d registros desde %s" %
          (payload["_meta"]["registros"], BASE_URL))
    return 0


if __name__ == "__main__":
    sys.exit(main())
