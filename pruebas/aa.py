import os
import fileinput

# Obtén la ruta completa del archivo "caca.py" en la misma carpeta que el script
ruta_archivo = os.path.join(os.path.dirname(__file__), "caca.py")

nuevo_valor = "jorgeewewdde"

# Itera sobre el archivo y reemplaza la línea que contiene "server = "maaaa""
with fileinput.FileInput(ruta_archivo, inplace=True) as archivo:
    for linea in archivo:
        if 'server = ' in linea:
            print(f'server = "{nuevo_valor}"')
        else:
            print(linea, end='')

print("")
input("Presione cualquier tecla para finalizar")

