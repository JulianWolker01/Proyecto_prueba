import subprocess




ruta_frontend = "./frontend/proyecto-academico"
comando_frontend = "npm start"


proceso_frontend = subprocess.Popen(comando_frontend, shell=True, cwd=ruta_frontend)


proceso_frontend.wait()

print("")
input("Presione cualquier tecla")