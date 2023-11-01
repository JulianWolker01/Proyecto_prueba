import os
import subprocess

directorio = './base-de-datos'

archivos = os.listdir(directorio)
nombre_mas_actual = None
fecha_mas_actual = "0000-00-00"

for archivo in archivos:
    if archivo.endswith('.sql') and archivo.startswith('sql_'):

        fecha_str = archivo.replace('sql_', '').split('.')[0]
        
        if fecha_str > fecha_mas_actual:
            fecha_mas_actual = fecha_str
            nombre_mas_actual = archivo

if nombre_mas_actual:
    print("El archivo más actual es:", nombre_mas_actual)
else:
    print("No se encontraron archivos con el formato esperado en el nombre.")

archivo_sql = os.path.abspath(os.path.join(directorio, nombre_mas_actual))

server_name = "DESKTOP-TVAQ0EC\SQLEXPRESS"

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