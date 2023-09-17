import subprocess

scripts = [
    "1.clonar_repositorios.py",
    "2.InstalarNODE.py",
    "3.dependencias.py",
    "4.SelectServer2.py",
    "5.BasedeDatos.py",
    "6.configapp.py",
    "7.BackendYFrontend.py"
]

for script in scripts:
    subprocess.run(["python", script])