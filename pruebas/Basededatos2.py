import os
import re
import subprocess
import socket

# Directorio en el que se encuentran los archivos
directorio = 'base-de-datos'

# Obtener una lista de todos los archivos en el directorio
archivos = os.listdir(directorio)

# Encontrar el archivo con el número más alto
nombre_max = max((archivo for archivo in archivos if archivo.endswith('.sql')), key=lambda x: int(re.search(r'(\d+)\.sql$', x).group(1)), default=None)

if nombre_max:
    print("El archivo con el número más alto es:", nombre_max)
else:
    print("No se encontraron archivos con números al final.")

# Función para obtener el nombre del servidor SQL Server Express
def get_sql_server_name_express():
    try:
        # Intenta conectarte a SQL Server Express
        server_name_express = socket.gethostname() + "\\SQLEXPRESS"
        return server_name_express
    except Exception as e:
        print(f"Error al obtener el nombre del servidor SQL Server Express: {str(e)}")
        return None

# Función para comprobar la existencia del servidor SQL Server
def sql_server_name_default():
    try:
        server_name = socket.gethostname() 
        return server_name
    except Exception as e:
        print(f"Error al obtener el nombre del servidor SQL Server: {str(e)}")
        return None

if __name__ == "__main__":
    sql_server_name_express = get_sql_server_name_express()
    
    if sql_server_name_express:
        print("Nombre del servidor SQL Server Express:", sql_server_name_express)
        
        # Comprobar si el servidor SQL Server Express existe
        try:
            subprocess.run(f'sqlcmd -S {sql_server_name_express} -E -Q "SELECT 1"', shell=True, check=True)

            
            # Si el servidor SQL Server (sin instancia) existe, ejecutar el archivo en ese servidor
            print("El servidor SQL Server (sin instancia) existe. Ejecutando el archivo en ese servidor.")
                        
            archivo_sql = os.path.abspath(os.path.join(directorio, nombre_max))
            
            # Ejecutar el comando en SQL Server Express
            comando_express = f'sqlcmd -S {sql_server_name_express} -d master -E -i "{archivo_sql}"'
            resultado_express = subprocess.run(comando_express, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Mostrar la salida del comando
            print("Salida estándar en SQL Server Express:")
            print(resultado_express.stdout)
            
            # Mostrar errores (si los hay) en SQL Server Express
            print("Errores en SQL Server Express:")
            print(resultado_express.stderr)
            
            # Verificar el código de retorno (0 indica éxito) en SQL Server Express
            if resultado_express.returncode == 0:
                print("El archivo se ejecutó con éxito en SQL Server Express.")
            else:
                print(f"Error al ejecutar el archivo en SQL Server Express. Código de retorno: {resultado_express.returncode}")
        except subprocess.CalledProcessError:
            print("El servidor SQL Server Express no existe.")
    else:
        print("No se pudo obtener el nombre del servidor SQL Server Express. El archivo no se ejecutará.")

    server_name_default = sql_server_name_default()
    if server_name_default:
        print("Nombre del servidor SQL Server (sin instancia):", server_name_default)
        
        # Comprobar si el servidor SQL Server (sin instancia) existe
        try:
            subprocess.run(f'sqlcmd -S {server_name_default} -E -Q "SELECT 1"', shell=True, check=True)

            
            # Si el servidor SQL Server (sin instancia) existe, ejecutar el archivo en ese servidor
            print("El servidor SQL Server (sin instancia) existe. Ejecutando el archivo en ese servidor.")
            
            # La dirección del archivo
            archivo_sql = os.path.abspath(os.path.join(directorio, nombre_max))
            
            # Ejecutar el comando en SQL Server (sin instancia)
            comando_default = f'sqlcmd -S {server_name_default} -d master -E -i "{archivo_sql}"'
            resultado_default = subprocess.run(comando_default, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Mostrar la salida del comando
            print("Salida estándar en SQL Server (sin instancia):")
            print(resultado_default.stdout)
            
            # Mostrar errores (si los hay) en SQL Server (sin instancia)
            print("Errores en SQL Server (sin instancia):")
            print(resultado_default.stderr)
            
            # Verificar el código de retorno (0 indica éxito) en SQL Server (sin instancia)
            if resultado_default.returncode == 0:
                print("El archivo se ejecutó con éxito en SQL Server (sin instancia).")
            else:
                print(f"Error al ejecutar el archivo en SQL Server (sin instancia). Código de retorno: {resultado_default.returncode}")
        
        except subprocess.CalledProcessError:
            print("El servidor SQL Server (sin instancia) no existe.")
    
    if not sql_server_name_express and not server_name_default:
        print("No se pudo obtener el nombre del servidor SQL Server ni SQL Server Express. El archivo no se ejecutará.")