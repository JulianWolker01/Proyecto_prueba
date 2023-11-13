import subprocess

ruta_frontend = "./frontend/proyecto-academico"
comando_frontend = "npm start"
proceso_frontend = subprocess.Popen(comando_frontend, shell=True, cwd=ruta_frontend, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

ruta_backend = "./backend/node_back"
comando_backend = "node index.js"
proceso_backend = subprocess.Popen(comando_backend, shell=True, cwd=ruta_backend, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

while True:
    output_frontend = proceso_frontend.stdout.readline()
    output_backend = proceso_backend.stdout.readline()

    if output_frontend == '' and output_backend == '' and proceso_frontend.poll() is not None and proceso_backend.poll() is not None:
        break

    if output_frontend:
        print(f"Frontend: {output_frontend.strip()}")

    if output_backend:
        print(f"Backend: {output_backend.strip()}")

proceso_frontend.wait()
proceso_backend.wait()




