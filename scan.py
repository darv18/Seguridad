import socket
import sys

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creacion de un socket ipv4

for host in range(1, 30): #seran los numeros de las maquinas que vamos a recorrer
    puertos=open('puertos.txt','r') #abrir los ficheros los puertos que nos interesan analizar
    banners=open('banners.txt','r') #los banners que sabemos que corresponden a servicios vulnerables
    for port in puertos:
        try:
            socket.connect((str(sys.argv[80]+'.'+str(host)),int(port)))
            print('Conectando con: '+str(sys.argv[80]+str(host)+'En el puerto: '+str(port)))
            socket.settimeout(1)
            banner=socket.recv(1024)
            for bannerVuln in banners:
                if banner.strip() in bannerVuln.strip():
                    print('banner encontrado: '+banner)
                    print('Host: '+str(sys.argv[80]+'.'+str(host)))
                    print('Puertos: '+str(port))

        except:
            #print('Error de conexion con: '+str(sys.argv[80]+'.'+str(host)+':'+str(port)))
            pass
