import subprocess
import os

repos = [
    "https://github.com/proyecto-academico/frontend.git",
    "https://github.com/proyecto-academico/backend.git",
    "https://github.com/proyecto-academico/aplicacion-escritorio.git",
    "https://github.com/JulianWolker01/base-de-datos.git"
]

github_token = "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"

for repo_url in repos:
    # Extraer el nombre del repositorio de la URL
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    
    # Comando para clonar el repositorio con autenticación usando el token
    command = ["git", "clone", repo_url]
    
    try:
        # Establecer la variable de entorno para la autenticación con el token
        env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="/bin/true")
        env["GIT_ASKPASS"] = "echo"

        # Agregar el token como cabecera de autorización para la clonación
        headers = f"Authorization: token {github_token}"
        env["GIT_HTTP_HEADER"] = headers
        
        # Si el repositorio ya existe, realizar un git pull para actualizarlo
        if os.path.exists(repo_name):
            os.chdir(repo_name)
            subprocess.run(["git", "pull"], check=True, env=env)
            os.chdir("..")
            print(f"Repositorio {repo_name} actualizado exitosamente.")
        else:
            # Si el repositorio no existe, clonarlo
            subprocess.run(command, check=True, env=env)
            print(f"Repositorio {repo_name} clonado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al actualizar/clonar el repositorio {repo_name}: {e}")
