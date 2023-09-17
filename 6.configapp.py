import fileinput

server = "DESKTOP-TVAQ0EC\SQLEXPRESS"
archivo_confi = "aplicacion-escritorio/PRUEAS/PRUEAS/DB_Querys.cs"

nuevo_valor = f'Integrated Security=SSPI;Persist Security Info=False;Initial Catalog=proyecto_academico;Data Source={server}'
reemplazado = False

with fileinput.FileInput(archivo_confi, inplace=True) as archivo:
    for linea in archivo:
        if 'private SqlConnection conn = new SqlConnection("Integrated ' in linea:
            print(f'        private SqlConnection conn = new SqlConnection("{nuevo_valor}");')
            reemplazado = True
        else:
            print(linea, end='')

if reemplazado:
    print("El valor se ha reemplazado correctamente.")
else:
    print("No se encontró la línea para reemplazar.")

input("Presione cualquier tecla para continuar")
