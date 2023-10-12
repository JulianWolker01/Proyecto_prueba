import os

directorio = 'base_de_datos'

archivos = os.listdir(directorio)
nombre_mas_actual = None
fecha_mas_actual = "0000-00-00"

for archivo in archivos:
    if archivo.endswith('.sql') and archivo.startswith('sql_'):

        fecha_str = archivo.replace('sql_', '').split('.')[0]
        
        if fecha_str > fecha_mas_actual:
            fecha_mas_actual = fecha_str
            nombre_mas_actual = archivo

if nombre_mas_actual:
    print("El archivo más actual es:", nombre_mas_actual)
else:
    print("No se encontraron archivos con el formato esperado en el nombre.")
