import socket
import os
import psutil

# Nombre de la interfaz de Ethernet que deseas obtener (puede variar según tu sistema)
nombre_interfaz_ethernet = "Ethernet"

# Obtener la dirección IP de la interfaz de Ethernet específica
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

directorios = ['backend', 'frontend']

for directorio in directorios:
    directorio_completo = os.path.join(os.getcwd(), directorio)
    ip_actual = "10.120.2.114"
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
