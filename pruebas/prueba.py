import socket
import subprocess
import getpass

def get_sql_server_name():
    server_name = socket.gethostname()
    return server_name

if __name__ == "__main__":
    sql_server_name = get_sql_server_name()
    print("Nombre del servidor SQL Server:", sql_server_name)

    # Obtener el nombre de usuario actual de la computadora
    nombre_usuario = getpass.getuser()

    # Imprimir el nombre de usuario
    print("Nombre de usuario:", nombre_usuario)

    # Comando que deseas ejecutar en el CMD
    
    comando = f"sqlcmd -S {sql_server_name} -d master -E -i C:\\Users\\{nombre_usuario}\\Desktop\\Proyecto\\Base de datos\\basededatos.sql"

    # Ejecuta el comando en el CMD
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Captura la salida estándar y la salida de error
    salida_estandar = resultado.stdout
    salida_error = resultado.stderr

    # Imprime la salida estándar y la salida de error
    print("Salida estándar:")
    print(salida_estandar)

    print("Salida de error:")
    print(salida_error)

    # Verifica el código de retorno (0 indica éxito)
    if resultado.returncode == 0:
        print("El comando se ejecutó con éxito.")
    else:
        print(f"Error al ejecutar el comando. Código de retorno: {resultado.returncode}")
