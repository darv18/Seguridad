from subprocess import PIPE, Popen #Importo las clases popen y pipe del modulo subprocess 

for ip in range(1, 30): #rango de ip's
    ipAddress ='192.168.0.' +str(ip) 
    subprocess =Popen(['/bin/ping','-c 1',ipAddress],stdout=PIPE,stdin=PIPE,stderr=PIPE) #creo una instancia de la clase popen 
    stdout,stderr=subprocess.communicate(input=None) #capturo el flujo de salida y de error

    if b"bytes from "in stdout: #analizo el flojo de salida para ver si la cadena contiene bytes from en ese caso la maquina remota contesta con un mensaje de tipo Echo Request
        print("IP %s"%(ipAddress)) #
        
