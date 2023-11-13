import re

def obtener_ip_desde_archivo(nombre_variable, nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Lee todas las líneas del archivo
        lineas = archivo.readlines()

        # Itera sobre cada línea
        for linea in lineas:
            # Verifica si la línea contiene el nombre de la variable
            if nombre_variable in linea:
                # Usa expresiones regulares para encontrar la dirección IP en la línea
                match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', linea)
                if match:
                    ip = match.group()
                    return ip

    # Si no se encuentra la variable, devuelve None
    return None

# Ejemplo de uso
nombre_variable = "URL_SERVIDOR"
nombre_archivo = "frontend/proyecto-academico/client/.env"

ip = obtener_ip_desde_archivo(nombre_variable, nombre_archivo)

if ip is not None:
    print(f"La dirección IP es: {ip}")
else:
    print(f"No se encontró la variable {nombre_variable} en el archivo {nombre_archivo}.")
