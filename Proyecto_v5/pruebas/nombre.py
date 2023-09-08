import os

# Directorio en el que se encuentran los archivos
directorio = 'Base_de_datos'

# Obtener una lista de todos los archivos en el directorio
archivos = os.listdir(directorio)

# Inicializar variables para el nombre y número máximo
nombre_max = None
numero_max = -1

# Iterar a través de los archivos
for archivo in archivos:
    # Comprobar si el archivo tiene la extensión ".sql"
    if archivo.endswith('.sql'):
        # Separar el nombre del archivo y la extensión
        nombre, extension = os.path.splitext(archivo)
        
        # Intentar convertir la parte final del nombre en un número
        try:
            numero = int(nombre[-1])  # Suponiendo que el número esté al final del nombre
        except ValueError:
            continue  # Ignorar archivos que no tienen un número válido al final
        
        # Si el número es mayor que el número máximo encontrado hasta ahora, actualizar
        if numero > numero_max:
            numero_max = numero
            nombre_max = archivo

if nombre_max:
    print("El archivo con el número más alto es:", nombre_max)
else:
    print("No se encontraron archivos con números al final.")
