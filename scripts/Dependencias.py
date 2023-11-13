import subprocess
import os


def instalar_dependencias(ruta, comando, nombre):
    proceso = subprocess.Popen(comando, shell=True, cwd=ruta, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Instalando dependencias en {nombre}...")
    stdout, stderr = proceso.communicate()
    if proceso.returncode == 0:
        print(f"Dependencias instaladas en {nombre}.")
    else:
        print(f"Error al instalar dependencias en {nombre}.")
        print(f"Salida de {nombre}:\n{stdout.decode()}")

def dependencias_instaladas(ruta):
    return os.path.exists(os.path.join(ruta, "node_modules"))

if __name__ == "__main__":

    ruta_frontend = "./frontend/proyecto-academico"
    comando_npm = "npm install"
    ruta_backend = "./backend/node_back"
    try:
        if dependencias_instaladas(ruta_frontend) and dependencias_instaladas(ruta_backend):
            print("Las dependencias ya están instaladas en el frontend y el backend.")
            respuesta = input("¿Deseas volver a instalar las dependencias? (Sí/No): ").strip().lower()
            if respuesta == 'no':
                input("Presione cualquier tecla para continuar...")
                exit()
        else:
            instalar_dependencias(ruta_backend, comando_npm, "backend")
            instalar_dependencias(ruta_frontend, comando_npm, "frontend")

        respuesta = input("¿Deseas instalar las dependencias de nuevo? (Sí/No): ").strip().lower()

        if respuesta == 'si':
            instalar_dependencias(ruta_backend, comando_npm, "backend")
            instalar_dependencias(ruta_frontend, comando_npm, "frontend")
                        
        elif respuesta == 'no':
            print("No se instalarán las dependencias nuevamente.")
        else:
            print("Respuesta no válida. Debes responder 'Sí' o 'No'.")
    except FileNotFoundError as e:
        print(f"Error al manipular archivos: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

input("Presione cualquier tecla para continuar...")
