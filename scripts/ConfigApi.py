import socket
import os
import psutil
import re

def obtener_ip_desde_archivo(nombre_variable, nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

        for linea in lineas:
            if nombre_variable in linea:
                match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', linea)
                if match:
                    ip = match.group()
                    return ip
    return None

nombre_variable = "URL_SERVIDOR"
nombre_archivo = "frontend/proyecto-academico/client/.env"

ip = obtener_ip_desde_archivo(nombre_variable, nombre_archivo)

if ip is not None:
    print(f"La dirección IP es: {ip}")
else:
    print(f"No se encontró la variable {nombre_variable} en el archivo {nombre_archivo}.")

nombre_interfaz_ethernet = "Ethernet"

mi_ip = None
for interfaz, direcciones in psutil.net_if_addrs().items():
    if interfaz == nombre_interfaz_ethernet:
        for direccion in direcciones:
            if direccion.family == socket.AF_INET:
                mi_ip = direccion.address
                break

if mi_ip:
    print(f"La dirección IP es: {mi_ip}")
else:
    print(f"No se pudo encontrar la dirección IP de la interfaz de Ethernet {nombre_interfaz_ethernet}.")

directorios = ['.\\backend', '.\\frontend']

for directorio in directorios:
    directorio_completo = os.path.join(os.getcwd(), directorio)
    ip_actual = ip
    nueva_ip = mi_ip

    def reemplazar_ip_en_archivo(ruta_archivo):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                contenido_modificado = contenido.replace(ip_actual, nueva_ip)

            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido_modificado)
                print(f'Reemplazo a {nueva_ip} en {ruta_archivo} completado.')
        except Exception as e:
            print(f"Error en archivo {ruta_archivo}: {str(e)}")

    for raiz, _, archivos in os.walk(directorio_completo):
        for nombre_archivo in archivos:
            if nombre_archivo.endswith('.env') or nombre_archivo.endswith('.js') or nombre_archivo.endswith('.json'):
                ruta_archivo = os.path.join(raiz, nombre_archivo)
                reemplazar_ip_en_archivo(ruta_archivo)
