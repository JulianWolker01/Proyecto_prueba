import subprocess
import socket
import os
import fileinput

server_names = [socket.gethostname(), socket.gethostname() + "\\SQLEXPRESS", socket.gethostname() + "\\SQLEXPRESS01",socket.gethostname() + "\\MSSQLEXPRESS", socket.gethostname() + "\\MSSQLEXPRESS01"]
def ExistenciaSQL(server_name):
    try:
        subprocess.run(f'sqlcmd -S {server_name} -E -Q "SELECT 1"', shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

servidores_existente = []
i = 0

for server_name in server_names:
    if ExistenciaSQL(server_name):
        i += 1
        servidores_existente.append(server_name) 
        print("")
        print(f"{i}.Servidor existente: {server_name}")
        print("")
    else:
        print("")
        print(f"El Servidor {server_name} no existe o no se encontro")
        print("")     
        
if servidores_existente:
    while True:
        try:
            print(f"Servidores Existentes : {servidores_existente}")
            print("")
            opcion = int(input("Elige el servidor en el que deseas trabajar (número): "))
            if 1 <= opcion <= len(servidores_existente):
                break  # Salir del bucle si la opción es válida
            else:
                print("Opción no válida. Por favor, ingresa un número válido.")
        except ValueError:
            print("Opción no válida. Por favor, ingresa un número válido.")
            
    server_name_seleccionado = servidores_existente[opcion - 1]

    print("")
    print(f"Se eligió el servidor {server_name_seleccionado}")
    print("")
    
ruta_archivo = os.path.join(os.path.dirname(__file__), "5.BasedeDatos.py")

nuevo_valor = server_name_seleccionado

with fileinput.FileInput(ruta_archivo, inplace=True) as archivo:
    for linea in archivo:
        if 'server_name = ' in linea:
            print(f'server_name = "{nuevo_valor}"')
        else:
            print(linea, end='')


ruta_archivo2 = os.path.join(os.path.dirname(__file__), "7.configapp.py")

with fileinput.FileInput(ruta_archivo2, inplace=True) as archivo:
    for linea in archivo:
        if 'server = ' in linea:
            print(f'server = "{nuevo_valor}"')
        else:
            print(linea, end='')
            
input("Presione cualquier tecla")