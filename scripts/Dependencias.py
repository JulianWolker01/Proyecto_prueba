import subprocess
import os

ruta_frontend = "frontend/proyecto-academico"
comando = "npm install"
ruta_backend = "backend/node_back"

try:
    proceso_frontend = subprocess.Popen(comando, shell=True, cwd=ruta_frontend)
    proceso_backend = subprocess.Popen(comando, shell=True, cwd=ruta_backend)

    proceso_frontend.wait()
    proceso_backend.wait()
    
    if proceso_backend.returncode == 0 and proceso_frontend.returncode == 0:
        env_path = "backend\\node_back\\.env"
        if not os.path.exists(env_path):
            with open(env_path, "w") as file:
                file.write('DATABASE_URL = "sqlserver://10.120.0.176:1433;initialCatalog=proyecto_academico;trustServerCertificate=true;user=123;Password=456"')
        else:
            print("El archivo .env ya existe en la ruta especificada.")
except Exception as e:
    print(f"Error: {str(e)}")

input("Presione cualquier tecla para continuar...")
