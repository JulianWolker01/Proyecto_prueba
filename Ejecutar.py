import os
import subprocess

archivos = [
    ("scripts/NODE.py", "Instala NODE.js en el sistema."),
    ("scripts/Repositorios.py", "Clona o actualiza todos los repositorios de git"),
    ("scripts/Dependencias.py", "Instala las dependencias para el proyecto. (Sin esto, la página web no funciona)"),
    ("scripts/Servidor.py", "Selecciona un servidor para la base de datos."),
    ("scripts/BasedeDatos.py", "Importa o actualiza la Base de Datos. (Si aún no seleccionaste el servidor, NO EJECUTAR)"),
    ("scripts/ConfigApi.py", "Configura La API para poder utilizarla en tu máquina"),
    ("scripts/Backend_Frontend.py", "Abre la página. (Ejecuta el Backend y Frontend)")
]

def ejecutar_archivos(archivos_a_ejecutar):
    for archivo, descripcion in archivos_a_ejecutar:
        ruta_absoluta = os.path.join(os.getcwd(), archivo)
        if os.path.exists(ruta_absoluta):
            print(f"\nEjecutando {ruta_absoluta} - {descripcion}...\n")
            subprocess.run(["python", ruta_absoluta])
        else:
            print(f"\nEl archivo {ruta_absoluta} no existe y no será ejecutado.\n")

def main():
    print("Lista de archivos disponibles:")
    for i, (archivo, descripcion) in enumerate(archivos, start=1):
        archivo_sin_ruta = os.path.basename(archivo)
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
            print(f"\nLos siguientes archivos no existen o no son válidos: {', '.join(archivos_invalidos)}\n")

        if archivos_validos:
            ejecutar_archivos(archivos_validos)
        else:
            print("\nNo se seleccionaron archivos válidos para ejecutar.\n")

if __name__ == "__main__":
    main()
