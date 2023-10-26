import subprocess

archivo_sln = "aplicacion-escritorio//PRUEAS//PRUEAS.sln"

# Ejecutar 'dotnet build' en el archivo .sln
proceso_compilacion = subprocess.Popen(["dotnet", "build", archivo_sln], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
salida, error = proceso_compilacion.communicate()

if proceso_compilacion.returncode == 0:
    print("Compilación exitosa")
else:
    print("Fallo en la compilación:")
    print(error)
