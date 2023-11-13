import psutil
import socket

# Nombre de la interfaz de Ethernet que deseas obtener (puede variar según tu sistema)
nombre_interfaz_ethernet = "Ethernet"

# Obtener la dirección IP de la interfaz de Ethernet específica
mi_ip = None
for interfaz, direcciones in psutil.net_if_addrs().items():
    if interfaz == nombre_interfaz_ethernet:
        for direccion in direcciones:
            if direccion.family == socket.AF_INET:
                mi_ip = direccion.address
                break

if mi_ip:
    print(f"La dirección IP de la interfaz de Ethernet {nombre_interfaz_ethernet} es: {mi_ip}")
else:
    print(f"No se pudo encontrar la dirección IP de la interfaz de Ethernet {nombre_interfaz_ethernet}.")
