import os

def delete(file_path, passes=3):
    """
    Este método sobrescribe el archivo con datos aleatorios y luego lo borra de forma segura.
    Creado por ChatGPT con modificaciones propias.
    """
    try:
        if os.path.exists(file_path):
            # Sobrescribir el archivo con datos aleatorios
            with open(file_path, 'ba+') as f:
                length = f.tell()  # Obtener tamaño del archivo
                for _ in range(passes):
                    f.seek(0)  # Volver al inicio del archivo
                    f.write(os.urandom(length))  # Escribir datos aleatorios
                    f.flush()
            
            # Borrar el archivo después de sobrescribir
            os.remove(file_path)
            print(f"El archivo {file_path} ha sido eliminado de forma segura.")
        else:
            print(f"El archivo {file_path} no existe.")
    except Exception as e:
        print(f"Error al intentar borrar el archivo de forma segura: {e}")
