import winreg
import os
import fileinput

# Ruta del registro a consultar
registry_key = r'SOFTWARE\Microsoft\Microsoft SQL Server'
registry_value_name = 'InstalledInstances'

instancias_sql = []

try:
    # Abrir la clave del registro
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key) as key:
        # Leer el valor del registro
        installed_instances = winreg.QueryValueEx(key, registry_value_name)
        
        # El resultado es una lista, por lo que no necesitas convertirla
        instances = installed_instances

        # Si hay instancias instaladas, agregar sus nombres con el nombre del servidor a la lista
        if instances:
            server_name = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 0, winreg.KEY_READ), 'Hostname')[0]
            for instance_list in instances:
                for instance in instance_list:
                    instancia_completa = f"{server_name}\\{instance}"
                    instancias_sql.append(instancia_completa)
        else:
            print("No se encontraron instancias de SQL Server instaladas.")
except Exception as e:
    print("Error al acceder al registro:", e)

# Mostrar las instancias
print("Instancias de SQL Server instaladas:")
for i, instancia in enumerate(instancias_sql, start=1):
    print(f"{i}. {instancia}")

# Pedir al usuario que elija una instancia
if instancias_sql:
    while True:
        opcion = input("Por favor, elija una instancia (número): ")
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(instancias_sql):
                instancia_elegida = instancias_sql[opcion - 1]
                print(f"Ha elegido la instancia: {instancia_elegida}")
                break  # Salir del bucle cuando la opción sea válida
            else:
                print("Opción no válida.")
        except ValueError:
            print("Opción no válida. Debe ingresar un número válido.")

# Resto del código para actualizar los archivos y otras operaciones
ruta_archivo = os.path.join(os.path.dirname(__file__), "5.BasedeDatos.py")
nuevo_valor = instancia_elegida

with fileinput.FileInput(ruta_archivo, inplace=True) as archivo:
    for linea in archivo:
        if 'server_name = ' in linea:
            print(f'server_name = "{nuevo_valor}"')
        else:
            print(linea, end='')

ruta_archivo2 = os.path.join(os.path.dirname(__file__), "configapp.py")

with fileinput.FileInput(ruta_archivo2, inplace=True) as archivo:
    for linea in archivo:
        if 'server = ' in linea:
            print(f'server = "{nuevo_valor}"')
        else:
            print(linea, end='')

input("Presione cualquier tecla")