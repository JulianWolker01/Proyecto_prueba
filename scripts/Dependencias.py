import subprocess
import os
import psutil
import socket

def install_psutil():
    try:
        import psutil
        print("psutil ya está instalado.")
    except ImportError:
        try:
            subprocess.check_call(["pip", "install", "psutil"])
            print("psutil ha sido instalado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar psutil: {e}")

def obtener_direccion_ip(nombre_interfaz_ethernet):
    mi_ip = None
    for interfaz, direcciones in psutil.net_if_addrs().items():
        if interfaz == nombre_interfaz_ethernet:
            for direccion in direcciones:
                if direccion.family == socket.AF_INET:
                    mi_ip = direccion.address
                    break
    return mi_ip

def instalar_dependencias(ruta, comando, nombre):
    proceso = subprocess.Popen(comando, shell=True, cwd=ruta, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Instalando dependencias en {nombre}...")
    stdout, stderr = proceso.communicate()
    if proceso.returncode == 0:
        print(f"Dependencias instaladas en {nombre}.")
    else:
        print(f"Error al instalar dependencias en {nombre}.")
        print(f"Salida de {nombre}:\n{stdout.decode()}")

def dependencias_instaladas(ruta):
    return os.path.exists(os.path.join(ruta, "node_modules"))

if __name__ == "__main__":
    install_psutil()

    ruta_frontend = "./frontend/proyecto-academico"
    comando_npm = "npm install"
    ruta_backend = "./backend/node_back"

    nombre_interfaz_ethernet = "Ethernet"
    mi_ip = obtener_direccion_ip(nombre_interfaz_ethernet)

    if not mi_ip:
        print(f"No se pudo encontrar la dirección IP de la interfaz de Ethernet {nombre_interfaz_ethernet}.")
        exit()

    try:
        if dependencias_instaladas(ruta_frontend) and dependencias_instaladas(ruta_backend):
            print("Las dependencias ya están instaladas en el frontend y el backend.")
            respuesta = input("¿Deseas volver a instalar las dependencias? (Sí/No): ").strip().lower()
            if respuesta == 'no':
                input("Presione cualquier tecla para continuar...")
                exit()
        else:
            instalar_dependencias(ruta_backend, comando_npm, "backend")
            instalar_dependencias(ruta_frontend, comando_npm, "frontend")

            env_path = "backend\\node_back\\.env"
            if not os.path.exists(env_path):
                with open(env_path, "w") as file:
                    file.write(f'DATABASE_URL = "sqlserver://{mi_ip}:1433;initialCatalog=proyecto_academico;trustServerCertificate=true;user=123;Password=456"')
            else:
                print("El archivo .env ya existe")

        respuesta = input("¿Deseas instalar las dependencias de nuevo? (Sí/No): ").strip().lower()

        if respuesta == 'si':
            instalar_dependencias(ruta_backend, comando_npm, "backend")
            instalar_dependencias(ruta_frontend, comando_npm, "frontend")
                        
            env_path = "backend\\node_back\\.env"
            if not os.path.exists(env_path):
                with open(env_path, "w") as file:
                    file.write(f'DATABASE_URL = "sqlserver://{mi_ip}:1433;initialCatalog=proyecto_academico;trustServerCertificate=true;user=123;Password=456"')
            else:
                print("El archivo .env ya existe")
        elif respuesta == 'no':
            print("No se instalarán las dependencias nuevamente.")
        else:
            print("Respuesta no válida. Debes responder 'Sí' o 'No'.")
    except FileNotFoundError as e:
        print(f"Error al manipular archivos: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

    input("Presione cualquier tecla para continuar...")
