import subprocess

# Comando de instalación de Node.js para Windows
comando_instalacion = 'msiexec.exe /i https://nodejs.org/dist/v18.18.0/node-v18.18.0-x64.msi'

# Ejecutar el comando de instalación
try:
    subprocess.run(comando_instalacion, shell=True, check=True)
    print("Node.js se ha instalado correctamente.")
except subprocess.CalledProcessError as e:
    print(f"Error al instalar Node.js: {e}")

print("")
input("Presione cualquier tecla")
