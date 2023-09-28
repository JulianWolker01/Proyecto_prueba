import subprocess

scripts = [
    "2.clonar_repositorios.py",
    "3.dependencias.py",
    "4.SelectServer.py",
    "5.BasedeDatos.py",
    "6.BackendYFrontend.py"
]

for script in scripts:
    subprocess.run(["python", script])