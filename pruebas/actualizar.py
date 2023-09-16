import subprocess

def obtener_nombre_usuario():
    
    try:
        resultado = subprocess.run(['git', 'config', '--global', 'user.name'], stdout=subprocess.PIPE, text=True, check=True)
        return resultado.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el nombre de usuario: {e}")
        return ""

def obtener_correo_electronico():
    try:
        resultado = subprocess.run(['git', 'config', '--global', 'user.email'], stdout=subprocess.PIPE, text=True, check=True)
        return resultado.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el correo electrónico: {e}")
        return ""

def actualizar_nombre_usuario(nuevo_nombre):
    subprocess.run(['git', 'config', '--global', 'user.name', nuevo_nombre])

def actualizar_correo_electronico(nuevo_email):
    subprocess.run(['git', 'config', '--global', 'user.email', nuevo_email])

def actualizar_credenciales():
    nuevo_nombre = input("Nuevo nombre de usuario: ").strip()
    nuevo_email = input("Nuevo correo electrónico: ").strip()
    
    actualizar_nombre_usuario(nuevo_nombre)
    actualizar_correo_electronico(nuevo_email)
    
    print("Credenciales actualizadas con éxito.")

opciones = {
    'no': actualizar_credenciales,
    'yes': lambda: print("ta bien"),
}

nombre_actual = obtener_nombre_usuario()
email_actual = obtener_correo_electronico()

print(f"Usuario actual: {nombre_actual}")
print(f"Correo electrónico actual: {email_actual}")

respuesta = input("¿Esta persona eres vos? (Yes/No): ").strip().lower()  
if respuesta in opciones:
    opciones[respuesta]()
else:
    print("Respuesta no válida. Debes ingresar 'Yes' o 'No'.")