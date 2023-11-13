import subprocess

ruta_backend = "./backend/node_back"
comando_backend = "node index.js"

ruta_frontend = "./frontend/proyecto-academico"
comando_frontend = "npm start"

proceso_frontend = subprocess.Popen(comando_frontend, shell=True, cwd=ruta_frontend)
proceso_backend = subprocess.Popen(comando_backend, shell=True, cwd=ruta_backend)

proceso_frontend.wait()
proceso_backend.wait()


print("")
input("Presione cualquier tecla")