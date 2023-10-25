import os
import subprocess

archivos = [
    ("scripts/NODE.py", "Instala NODE.js en el sistema."),
    ("scripts/Repositorios.py", "Clona o actualiza todos los repositorios de git"),
    ("scripts/Dependencias.py", "Instala las dependencias para el proyecto. (Sin esto, la pagina web no funciona)"),
    ("scripts/Servidor.py", "Selecciona un servidor para la base de datos."),
    ("scripts/BasedeDatos.py", "Importa o actualiza la Base de Datos. (Si aun no seleccionaste el servidor, NO EJECUTAR)"),
    ("scripts/Backend_Frontend.py", "Abre la pagina. (Ejecuta el Backend y Frontend)")
]

def ejecutar_archivos(archivos_a_ejecutar):
    for archivo, descripcion in archivos_a_ejecutar:
        if os.path.exists(archivo):
            print("")
            print(f"Ejecutando {archivo} - {descripcion}...")
            print("")
            subprocess.run(["python", archivo])
        else:
            print("")
            print(f"El archivo {archivo} no existe y no será ejecutado.")
            print("")

def main():
    print("Lista de archivos disponibles:")
    for i, (archivo, descripcion) in enumerate(archivos, start=1):
        archivo_sin_ruta = archivo.split("/")[-1]
        print(f"{i}. {archivo_sin_ruta} - {descripcion}")

    seleccion = input("Elija los archivos a ejecutar (separe con comas o escriba 'Todo' para ejecutar todos): ").strip()

    if seleccion.lower() == "todo":
        archivos_a_ejecutar = archivos
        ejecutar_archivos(archivos_a_ejecutar)
         
    else:
        indices_seleccionados = [int(idx) - 1 for idx in seleccion.split(",")]
        archivos_validos = [(archivos[i][0], archivos[i][1]) for i in indices_seleccionados if 0 <= i < len(archivos)]
        archivos_invalidos = [str(int(idx)) for idx in seleccion.split(",") if int(idx) < 1 or int(idx) > len(archivos)]

        if archivos_invalidos:
            print("")
            print(f"Los siguientes archivos no existen o no son válidos: {', '.join(archivos_invalidos)}")
            print("")

        if archivos_validos:
            ejecutar_archivos(archivos_validos)
        else:
            print("No se seleccionaron archivos válidos para ejecutar.")

if __name__ == "__main__":
    main()
