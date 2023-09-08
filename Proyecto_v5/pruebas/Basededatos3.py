import socket
import subprocess
import os
import re

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

def get_sql_server_name():
    server_name = socket.gethostname()
    return server_name

def get_sql_server_name2():
    server_name2 = socket.gethostname() + "\SQLEXPRESS"
    return server_name2

if __name__ == "__main__":
    try:
        sql_server_name = get_sql_server_name()
        print("Nombre del servidor SQL Server:", sql_server_name)
    except Exception as e:
        print("Error al obtener el nombre del servidor SQL Server:", str(e))

if __name__ == "__main__":
    try:
        sql_server_name2 = get_sql_server_name2()
        print("Nombre del servidor SQL Server:", sql_server_name2)
    except Exception as e:
        print("Error al obtener el nombre del servidor SQL Server:", str(e))

archivo_sql = os.path.abspath(os.path.join(directorio, nombre_max))

comando_existe_bd = f'sqlcmd -S {sql_server_name} -d master -E -Q "IF DB_ID(\'proyecto_academico\') IS NOT NULL PRINT \'Exists\'"'
comando_existe_bd2 = f'sqlcmd -S {sql_server_name2} -d master -E -Q "IF DB_ID(\'proyecto_academico\') IS NOT NULL PRINT \'Exists\'"'
resultado_existe_bd = subprocess.run(comando_existe_bd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
resultado_existe_bd2 = subprocess.run(comando_existe_bd2, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if "Exists" in resultado_existe_bd.stdout or "Exists" in resultado_existe_bd2.stdout:
    print("La base de datos 'proyecto_academico' ya existe")
    
    # Eliminar la base de datos existente
    comando_eliminar_bd = f'sqlcmd -S {sql_server_name} -d master -E -Q "DROP DATABASE proyecto_academico"'
    resultado_eliminar_bd = subprocess.run(comando_eliminar_bd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    comando_eliminar_bd2 = f'sqlcmd -S {sql_server_name2} -d master -E -Q "DROP DATABASE proyecto_academico"'
    resultado_eliminar_bd2 = subprocess.run(comando_eliminar_bd2, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Verificar si la eliminación tuvo éxito
    if resultado_eliminar_bd.returncode == 0 or resultado_eliminar_bd2.returncode == 0:
        print("La base de datos 'proyecto_academico' existente ha sido eliminada.")
    else:
        print("Error al eliminar la base de datos existente.")
    print("La base de datos 'proyecto_academico' no existe. Importando el archivo SQL...")

    comando = f'sqlcmd -S {sql_server_name} -d master -E -i "{archivo_sql}"'
    comando2 = f'sqlcmd -S {sql_server_name2} -d master -E -i "{archivo_sql}"'

    resultado = subprocess.run(comando, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resultado2 = subprocess.run(comando2, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("Salida estándar:")
    print(resultado.stdout)
    print("Salida estándar:")
    print(resultado2.stdout)

    print("Errores:")
    print(resultado.stderr)
    print("Errores:")
    print(resultado2.stderr)

    if resultado.returncode == 0:
        print("El archivo SQL se importó con éxito.")
    else:
        print(f"Error al importar el archivo SQL. Código de retorno: {resultado.returncode}")

    if resultado2.returncode == 0:
        print("El archivo SQL se importó con éxito.")
    else:
        print(f"Error al importar el archivo SQL. Código de retorno: {resultado2.returncode}")
else:
    print("La base de datos 'proyecto_academico' no existe. Importando el archivo SQL...")

    comando = f'sqlcmd -S {sql_server_name} -d master -E -i "{archivo_sql}"'
    comando2 = f'sqlcmd -S {sql_server_name2} -d master -E -i "{archivo_sql}"'

    resultado = subprocess.run(comando, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resultado2 = subprocess.run(comando2, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("Salida estándar:")
    print(resultado.stdout)
    print("Salida estándar:")
    print(resultado2.stdout)

    print("Errores:")
    print(resultado.stderr)
    print("Errores:")
    print(resultado2.stderr)

    if resultado.returncode == 0:
        print("El archivo SQL se importó con éxito.")
    else:
        print(f"Error al importar el archivo SQL. Código de retorno: {resultado.returncode}")

    if resultado2.returncode == 0:
        print("El archivo SQL se importó con éxito.")
    else:
        print(f"Error al importar el archivo SQL. Código de retorno: {resultado2.returncode}")