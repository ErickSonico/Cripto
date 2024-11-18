import os

def listar_archivos_documentos():
    documentos_path = os.path.join(os.environ["USERPROFILE"], "Documents")

    print(f"Archivos en la carpeta Documentos ({documentos_path}):")
    for root, _, files in os.walk(documentos_path):
        for file in files:
            print(os.path.join(root, file))

listar_archivos_documentos()
