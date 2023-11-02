import subprocess

ruta_backend = "./backend"
comando_backend = "node index.js"  

proceso_backend = subprocess.Popen(comando_backend, shell=True, cwd=ruta_backend)
proceso_backend.wait()

print("")
input("Presione cualquier tecla")