import GetTareas as gt
from Moodle import IniciarSesion
import getpass  # Importa el módulo getpass


#Link de la universidad
link = 'https://aulagradob.unemi.edu.ec'

# Inicia sesión
username = input("Por favor, ingresa tu usuario: ")

# Utiliza getpass para ocultar la contraseña al escribir
password = getpass.getpass("Por favor, ingresa tu contraseña: ")


token,user_id = IniciarSesion(username, password, link)

#Validamos si el usuario ingresado es correcto

if token:

    
    print("Por favor, espera un momento mientras cargamos tus tareas...")
    tareas = gt.Obtener_tareas(token, user_id, link)

    print("Tareas cargadas con éxito")

    dias = input("¿Cuántos días quieres ver hacia adelante? ")

    tareas_proximas = gt.TareasProximas(tareas, int(dias))

    print(tareas_proximas)

    with open("Tareas.txt", "w", encoding="utf-8") as file:
        file.write(str(tareas_proximas))

else:

    print("Usuario o contraseña incorrectos")
    print("Por favor, intenta de nuevo")
    

    




