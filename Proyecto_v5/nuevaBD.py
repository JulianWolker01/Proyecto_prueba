import os
import re
import subprocess
import socket

directorio = 'base-de-datos'
archivos = os.listdir(directorio)

nombre_max = None
numero_max = -1

# Iterar a través de los archivos
for archivo in archivos:
    # Comprobar si el archivo tiene la extensión ".sql"
    if archivo.endswith('.sql'):
        # Utilizar una expresión regular para extraer el número del nombre del archivo
        match = re.search(r'(\d+)\.sql$', archivo)
        if match:
            numero = int(match.group(1))
            if numero > numero_max:
                numero_max = numero
                nombre_max = archivo

if nombre_max:
    print("El archivo con el número más alto es:", nombre_max)
else:
    print("No se encontraron archivos con números al final.")

archivo_sql = os.path.abspath(os.path.join(directorio, nombre_max))

def ExistenciaSQL(server_name):
    try:
        subprocess.run(f'sqlcmd -S {server_name} -E -Q "SELECT 1"', shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def ExistenciaBD(server_name):
    try:
        comando_verificar_bd = f'sqlcmd -S {server_name} -d master -E -Q "SELECT name FROM sys.databases WHERE name = \'proyecto_academico\'"'
        resultado = subprocess.run(comando_verificar_bd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if "proyecto_academico" in resultado.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error al verificar la existencia de la base de datos en {server_name}: {e}")
        return False   

def ImporteDB(server_name):
    try:
        comando = f'sqlcmd -S {server_name} -d master -E -i "{archivo_sql}"'
        subprocess.run(comando, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al importar la base de datos en {server_name}: {e}")
        return False

def EliminarExistente(server_name):
    try:
        comando_eliminar_bd = f'sqlcmd -S {server_name} -d master -E -Q "DROP DATABASE proyecto_academico"'
        subprocess.run(comando_eliminar_bd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al eliminar la base de datos en {server_name}: {e}")
        return False

server_names = [socket.gethostname(), socket.gethostname() + "\\SQLEXPRESS", socket.gethostname() + "\\SQLEXPRESS01"]

for server_name in server_names:
    if ExistenciaSQL(server_name):
        print(f"Existe el Servidor en {server_name}, Se verifica la existencia de la BD")
        if ExistenciaBD(server_name):
            print("Existe la base de datos, Procede a eliminarse y actualizarse")
            if EliminarExistente(server_name):
                print("La base de datos fue eliminada")
                print("Se esta por importar la nueva base de datos")
                if ImporteDB(server_name):
                    print("La base de datos se importó correctamente")
                else:
                    print("Ocurrió un error en la importación de la BD")
            else:
                print("Error al eliminar la base de datos existente")
        else:
            print("La base de datos no existe, procede a importarla")
            if ImporteDB(server_name):
                print("La base de datos se importó correctamente")
            else:
                print("Ocurrió un error en la importación de la BD")
    else:
        print(f"El servidor no existe en {server_name}")