import os

# Directorio en el que se encuentran los archivos
directorio = 'Base_de_datos'

# Obtener una lista de todos los archivos en el directorio
archivos = os.listdir(directorio)

# Inicializar variables para el nombre y fecha máxima
nombre_mas_actual = None

# Fecha máxima (inicializada con un valor mínimo para que cualquier fecha sea mayor)
fecha_mas_actual = "0000-00-00"

# Iterar a través de los archivos
for archivo in archivos:
    # Comprobar si el archivo tiene la extensión ".sql"
    if archivo.endswith('.sql') and archivo.startswith('proyecto_'):
        # Extraer la fecha del nombre del archivo (eliminando "proyecto_")
        fecha_str = archivo.replace('proyecto_', '').split('.')[0]
        
        # Comparar el nombre del archivo con la fecha más actual encontrada hasta ahora
        if fecha_str > fecha_mas_actual:
            fecha_mas_actual = fecha_str
            nombre_mas_actual = archivo

if nombre_mas_actual:
    print("El archivo más actual es:", nombre_mas_actual)
else:
    print("No se encontraron archivos con el formato esperado en el nombre.")
