import subprocess
import os

archivo_sql = os.path.abspath("Base_de_datos\\basededatos.sql")
comando = f'sqlcmd -S DESKTOP-TVAQ0EC -d master -E -i "{archivo_sql}"'


# Ejecutar el comando en cmd
resultado = subprocess.run(comando, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Mostrar la salida del comando
print("Salida estándar:")
print(resultado.stdout)

# Mostrar errores (si los hay)
print("Errores:")
print(resultado.stderr)
