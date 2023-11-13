import os
import re
import fileinput

# Ruta al archivo .env
archivo_env = 'frontend/proyecto-academico/client/.env'  # Asegúrate de proporcionar la ruta correcta

# Expresión regular para buscar la dirección IP
patron_ip = r'http://(\d+\.\d+\.\d+\.\d+):'

# Función para obtener la dirección IP del archivo .env
def obtener_direccion_ip_desde_env(archivo_env):
    direccion_ip = None
    with open(archivo_env, 'r') as archivo:
        contenido = archivo.read()
        match = re.search(patron_ip, contenido)
        if match:
            direccion_ip = match.group(1)
    return direccion_ip

direccion_ip = obtener_direccion_ip_desde_env(archivo_env)

if direccion_ip:
    print(f'Dirección IP en el archivo .env: {direccion_ip}')
else:
    print('No se encontró una dirección IP en el archivo .env')

ruta_archivo = os.path.join(os.path.dirname(__file__), "ConfigApi.py")
nuevo_valor = direccion_ip

with fileinput.FileInput(ruta_archivo, inplace=True) as archivo:
    for linea in archivo:
        if 'ip_actual = "' in linea:
            print(f'    ip_actual = "{nuevo_valor}"')
        else:
            print(linea, end='')