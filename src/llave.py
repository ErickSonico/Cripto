import os
import sys

from pathlib import Path

def extraeLlave():
    """ Extrae la llave pública y la guarda en la carpeta temporal del sistema.

    La llave viene dentro del ejecutable, se agrega al crearlo con PyInstaller.
    """
    temp_dir = Path(os.getenv("TEMP"))
    archivo_destino = temp_dir / "pubkey.pem"

    # _MEIPASS es una variable de PyInstaller que guarda la ruta de los recursos.
    ruta_recurso = Path(sys._MEIPASS) / "pubkey.pem"

    with open(ruta_recurso, "rb") as origen, open(archivo_destino, "wb") as destino:
        destino.write(origen.read())

    return str(archivo_destino)

def llave():
    """ Devuelve la ruta de la llave pública. """
    return extraeLlave()