import getpass
from utils import cargar_json, guardar_json

USUARIOS_FILE = "datos/usuarios.json"

def registrar_usuario():
    usuarios = cargar_json(USUARIOS_FILE)

    nombre = input("Ingresa nombre de usuario: ").strip()
    if any(u['nombre'] == nombre for u in usuarios):
        print("Error: El usuario ya existe.")
        return False

    contrasena = getpass.getpass("Ingresa contraseña: ")
    contrasena_confirm = getpass.getpass("Confirma contraseña: ")
    if contrasena != contrasena_confirm:
        print("Error: Las contraseñas no coinciden.")
        return False

    usuarios.append({"nombre": nombre, "contrasena": contrasena})
    guardar_json(USUARIOS_FILE, usuarios)
    print(f"Usuario '{nombre}' registrado con éxito.")
    return True

def iniciar_sesion():
    usuarios = cargar_json(USUARIOS_FILE)

    nombre = input("Ingresa nombre de usuario: ").strip()
    usuario = next((u for u in usuarios if u['nombre'] == nombre), None)
    if not usuario:
        print("Error: Usuario no encontrado.")
        return None

    contrasena = getpass.getpass("Ingresa contraseña: ")
    if contrasena != usuario['contrasena']:
        print("Error: Contraseña incorrecta.")
        return None

    print(f"Bienvenido, {nombre}!")
    return usuario
