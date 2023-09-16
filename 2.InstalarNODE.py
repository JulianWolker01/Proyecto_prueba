import subprocess

# Verificar si Node.js está instalado
try:
    node_version = subprocess.check_output(['node', '--version'], stderr=subprocess.STDOUT, text=True)
    print("Node.js está instalado. Versión:", node_version)
except subprocess.CalledProcessError:
    print("Node.js no está instalado. Instalando...")

    # Instalar Node.js utilizando el administrador de paquetes nvm
    install_node_command = 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.nvm/nvm.sh && nvm install node'
    subprocess.run(install_node_command, shell=True, check=True)

    print("Node.js instalado correctamente.")

# Verificar la versión de Node.js
node_version = subprocess.check_output(['node', '--version'], stderr=subprocess.STDOUT, text=True).strip()
print("Versión de Node.js:", node_version)

print("")
input("Presione cualquier tecla")