import os
import re
import subprocess

directorio = 'base-de-datos'
archivos = os.listdir(directorio)

nombre_max = None
numero_max = -1

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
    print("El archivo mas actual es: ", nombre_max)
else:
    print("No se encontraron archivos con números al final.")

archivo_sql = os.path.abspath(os.path.join(directorio, nombre_max))

server_name = "DESKTOP-TVAQ0EC\SQLEXPRESS01"

def ExistenciaBD(server_name):
    try:
        comando_verificar_bd = f'sqlcmd -S {server_name} -d master -E -Q "SELECT name FROM sys.databases WHERE name = \'proyecto_academico\'"'
        resultado = subprocess.run(comando_verificar_bd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if "proyecto_academico" in resultado.stdout:
            print("La base de datos ya existe")
            return True
        else:
            print("La base de datos no existe, procede a importarla")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error al verificar la existencia de la base de datos en {server_name}: {e}")
        return False   

def ImporteDB(server_name):
    try:
        comando = f'sqlcmd -S {server_name} -d master -E -i "{archivo_sql}"'
        subprocess.run(comando, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("La base de datos se importó correctamente")
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

if ExistenciaBD(server_name):
    if EliminarExistente(server_name):
        print("La base de datos fue eliminada")
        ImporteDB(server_name)
    else:
        print("La base de datos no existe, procede a importarla")
        ImporteDB(server_name)
else:
    ImporteDB(server_name)

print("")
input("Presione cualquier tecla")