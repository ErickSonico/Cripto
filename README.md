# Ransomware y SpyWare Crypt0h0t.

El ejecutable no necesita la desactivación de Windows Defender y por el momento debe ejecutarse con permisos de administrador para cifrar archivos protegidos. 

Se adjuntan archivos de prueba en formato zip. Descomprimir y colocar en la carpeta Documents. 

Si se desea crear un ejecutable, se debe usar el siguiente comando en la carpeta ransom:
```
> pyinstaller --onefile --add-data "Malware.jpg;.-add-data "pubkey.pem;.-icon=exe.ico main.py
```


Caliente mx no tiene nada que ver en la realización de este malware y se usó la imagen con fines didácticos. 