import subprocess
import os

repos = [
    "https://github.com/proyecto-academico/frontend.git",
    "https://github.com/proyecto-academico/backend.git",
    "https://github.com/proyecto-academico/aplicacion-escritorio.git",
    "https://github.com/JulianWolker01/base-de-datos.git"
]

for repo_url in repos:
    # Extraer el nombre del repositorio de la URL
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    
    # Comando para clonar el repositorio sin autenticación
    command = ["git", "clone", repo_url]
    
    try:
        # Si el repositorio ya existe, realizar un git pull para actualizarlo
        if os.path.exists(repo_name):
            os.chdir(repo_name)
            subprocess.run(["git", "pull"], check=True)
            os.chdir("..")
            print(f"Repositorio {repo_name} actualizado exitosamente.")
        else:
            # Si el repositorio no existe, clonarlo
            subprocess.run(command, check=True)
            print(f"Repositorio {repo_name} clonado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al actualizar/clonar el repositorio {repo_name}: {e}")

print("")
input("Presione cualquier tecla para finalizar")
