import subprocess
import os

ruta_frontend = "./frontend/proyecto-academico"
comando = "npm install"
ruta_backend = "./backend/node_back"

def dependencias_instaladas(ruta):
    return os.path.exists(os.path.join(ruta, "node_modules"))

try:

    if dependencias_instaladas(ruta_frontend) and dependencias_instaladas(ruta_backend):
        print("Las dependencias ya están instaladas en el frontend y el backend.")
        respuesta = input("¿Deseas volver a instalar las dependencias? (Sí/No): ").strip().lower()
        if respuesta == 'no':
            input("Presione cualquier tecla para continuar...")
            exit()
    
    if respuesta == 'si' or respuesta == 's':

        proceso_backend = subprocess.Popen(comando, shell=True, cwd=ruta_backend, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Instalando dependencias en el backend...")
        stdout_backend, stderr_backend = proceso_backend.communicate()
        if proceso_backend.returncode == 0:
            print("Dependencias instaladas en el backend.")
        else:
            print("Error al instalar dependencias en el backend.")
            print(f"Salida del backend:\n{stdout_backend.decode()}")
        
        proceso_frontend = subprocess.Popen(comando, shell=True, cwd=ruta_frontend, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Instalando dependencias en el frontend...")
        stdout_frontend, stderr_frontend = proceso_frontend.communicate()
        if proceso_frontend.returncode == 0:
            print("Dependencias instaladas en el frontend.")
        else:
            print("Error al instalar dependencias en el frontend.")
            print(f"Salida del frontend:\n{stdout_frontend.decode()}")
        
        env_path = "backend\\node_back\\.env"
        if not os.path.exists(env_path):
            with open(env_path, "w") as file:
                file.write('DATABASE_URL = "sqlserver://10.120.0.176:1433;initialCatalog=proyecto_academico;trustServerCertificate=true;user=123;Password=456"')
        else:
            print("El archivo .env ya existe")
    else:
        print("Respuesta no válida. Debes responder 'Sí' o 'No'.")
except Exception as e:
    print(f"Error: {str(e)}")

input("Presione cualquier tecla para continuar...")
