import ctypes
import os
import sys

from pathlib import Path


def extraeLlave():
    temp_dir = Path(os.getenv("TEMP"))
    archivo_destino = temp_dir / "pubkey.pem"


    if getattr(sys, "frozen", False):
        ruta_recurso = Path(sys._MEIPASS) / "pubkey.pem"
    else:
        ruta_recurso = Path(__file__).parent / "pubkey.pem"

    with open(ruta_recurso, "rb") as origen, open(archivo_destino, "wb") as destino:
        destino.write(origen.read())

    return str(archivo_destino)

def llave():
    return extraeLlave()