import ctypes
import os
import sys
import winreg as reg
from pathlib import Path

def fondo(ruta_imagen):
    """
    Cambia el fondo de pantalla en Windows utilizando el registro.
    
    Parámetros:
    ruta_imagen -- Ruta de la imagen.
    """
    clave_registro = r"Control Panel\Desktop"
    with reg.OpenKey(reg.HKEY_CURRENT_USER, clave_registro, 0, reg.KEY_SET_VALUE) as clave:
        reg.SetValueEx(clave, "WallpaperStyle", 0, reg.REG_SZ, "2")
        reg.SetValueEx(clave, "TileWallpaper", 0, reg.REG_SZ, "0")

    ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)

def extraeImagen(nombre_archivo):
    """
    Extrae la imagen del ejecutable y la guarda en la carpeta temporal del sistema.
    """
    temp_dir = Path(os.getenv("TEMP"))
    archivo_destino = temp_dir / nombre_archivo


    if getattr(sys, "frozen", False):
        ruta_recurso = Path(sys._MEIPASS) / nombre_archivo
    else:
        ruta_recurso = Path(__file__).parent / nombre_archivo

    with open(ruta_recurso, "rb") as origen, open(archivo_destino, "wb") as destino:
        destino.write(origen.read())

    return str(archivo_destino)

def cambiarFondo(nombre_archivo):
    """
    Función que facilita la llamada a las funciones para cambiar el fondo de pantalla.

    Parámetros:
    nombre_archivo -- Nombre de la imagen.
    """
    path = extraeImagen(nombre_archivo)
    fondo(path)