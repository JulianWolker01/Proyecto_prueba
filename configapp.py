import fileinput

server = "DESKTOP-H6CDQKL\SQLEXPRESS01"
reemplazado = server.replace("\\", "\\\\")

archivo_confi = "aplicacion-escritorio/PRUEAS/PRUEAS/DB_Querys.cs"
nuevo_valor = f'Integrated Security=SSPI;Persist Security Info=False;Initial Catalog=proyecto_academico;Data Source={reemplazado}'

def Cambio1():
    with fileinput.FileInput(archivo_confi, inplace=True) as archivo:
        for linea in archivo:
            if 'private SqlConnection conn = new SqlConnection("' in linea:
                print(f'        private SqlConnection conn = new SqlConnection("{nuevo_valor}");')
            else:
                print(linea, end='')
def Cambio2():
    with fileinput.FileInput(archivo_confi, inplace=True) as archivo:
        for linea in archivo:
            if 'private SqlConnection conn = new SqlConnection("' in linea:
                print(f'        private SqlConnection conn = new SqlConnection("Server=10.120.0.176;Database=proyecto_academico;User Id=123;Password=456;");')
            else:
                print(linea, end='')

opciones = {
    'T1': Cambio1,
    'T2': Cambio2,
}
respuesta = input("Quieres que la aplicacion funcione de la manera T1 o manera T2 =  ")
if respuesta in opciones:
    opciones[respuesta]()
    print("Se remplazo correctamente")
else:
    print("Fallo")