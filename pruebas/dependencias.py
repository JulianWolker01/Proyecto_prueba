import subprocess


ruta_frontend = "frontend/proyecto-academico"
comando= "npm install"
ruta_backend = "backend/node_back"


proceso_frontend = subprocess.Popen(comando, shell=True, cwd=ruta_frontend)
proceso_backend = subprocess.Popen(comando, shell=True, cwd=ruta_backend)

proceso_frontend.wait()
proceso_backend.wait()