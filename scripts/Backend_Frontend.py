import subprocess

ruta_frontend = "./frontend/proyecto-academico"
comando_frontend = "npm start"

proceso_frontend = subprocess.Popen(comando_frontend, shell=True, cwd=ruta_frontend)

proceso_frontend.wait()

print("")
input("Presione cualquier tecla")

ruta_backend = "./backend"
comando_backend = "node index.js"  

proceso_backend = subprocess.Popen(comando_backend, shell=True, cwd=ruta_backend)
proceso_backend.wait()

print("")
input("Presione cualquier tecla")

