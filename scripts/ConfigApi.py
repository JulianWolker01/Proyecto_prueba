import os
import re
import subprocess

def obtener_ip_desde_archivo(nombre_variable, nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                if nombre_variable in linea:
                    match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', linea)
                    if match:
                        return match.group()
        return None
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {str(e)}")
        return None

def obtener_direccion_ip_interfaz(nombre_interfaz):
    try:
        if os.name == 'nt':  
            resultado = subprocess.run(['ipconfig'], stdout=subprocess.PIPE, text=True)
            ip_match = re.search(r'IPv4 Address[.\s]*: ([^\s]+)', resultado.stdout)
            if ip_match:
                return ip_match.group(1)
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener la dirección IP de la interfaz: {str(e)}")
    except Exception as e:
        print(f"Error en obtener_direccion_ip_interfaz: {str(e)}")
    return None


def crear_o_actualizar_archivo_env(env_path, mi_ip):
    try:
        if not os.path.exists(env_path):
            with open(env_path, "w") as file:
                file.write(f'DATABASE_URL = "sqlserver://{mi_ip}:1433;initialCatalog=proyecto_academico;trustServerCertificate=true;user=123;Password=456"')
        else:
            print("El archivo .env ya existe")
    except Exception as e:
        print(f"Error al crear o actualizar el archivo {env_path}: {str(e)}")

def reemplazar_ip_en_archivos(directorio_completo, ip_actual, nueva_ip):
    try:
        for raiz, _, archivos in os.walk(directorio_completo):
            for nombre_archivo in archivos:
                if nombre_archivo.endswith(('.env', '.js', '.json')):
                    ruta_archivo = os.path.join(raiz, nombre_archivo)
                    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                        contenido = archivo.read()
                        contenido_modificado = contenido.replace(ip_actual, nueva_ip)

                    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                        archivo.write(contenido_modificado)
                        print(f'Reemplazo a {nueva_ip} en {ruta_archivo} completado.')
    except Exception as e:
        print(f"Error al reemplazar la dirección IP en los archivos: {str(e)}")

def main():
    nombre_variable = "URL_SERVIDOR"
    nombre_archivo = "frontend/proyecto-academico/client/.env"
    ip = obtener_ip_desde_archivo(nombre_variable, nombre_archivo)

    if ip:
        print(f"La dirección IP es: {ip}")
    else:
        print(f"No se encontró la variable {nombre_variable} en el archivo {nombre_archivo}.")

    nombre_interfaz_ethernet = "Ethernet"
    mi_ip = obtener_direccion_ip_interfaz(nombre_interfaz_ethernet)

    if mi_ip:
        print(f"La dirección IP es: {mi_ip}")
        env_path = "backend\\node_back\\.env"
        crear_o_actualizar_archivo_env(env_path, mi_ip)

        directorios = ['.\\backend', '.\\frontend']
        reemplazar_ip_en_archivos('.', ip, mi_ip)

    else:
        print(f"No se pudo encontrar la dirección IP de la interfaz de Ethernet {nombre_interfaz_ethernet}.")

if __name__ == "__main__":
    main()

