import sys
import subprocess

def modo_uso():
    print('python listarMacs.py inteface cidr')
    print('Lista todas las direcciones MAC de la red dada')
    print('\t-inteface: interface de red')
    print('\t-cidr: dirección de red con mascara')
    print('Ejemplo:')
    print('\t python listarMacs.py wlo1 192.168.1.0/24')

def salidaArpScan(interface, cidr):
    comando = f'arp-scan -interface {interface} {cidr}'
    preparacion = subprocess.Popen(comando.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = preparacion.communicate()
    if not error:
        return str(salida)
    print(error)
    print('Hubo un error en arp-scan')
    exit(1)

def parsearMacs(salidaScan):
    partes = salidaScan.split('\\t')[1:]
    macs = []
    for i in range(len(partes)):
        if i % 2 == 0:
            macs.append(partes[i])
    return macs

if __name__ == '__main__':
    if len(sys.argv[1:]) != 2:
        modo_uso()
        exit(1)

    salidaScan = salidaArpScan(sys.argv[1], sys.argv[2])
    for mac in parsearMacs(salidaScan):
        print(mac)
