from usuarios import registrar_usuario, iniciar_sesion

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Menú de Finanzas")
    print("4. Ver Metas")
    print("5. Salir")
    return input("Selecciona una opción: ")

def menu_usuario():
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Volver al menú principal")
        opcion = input("Selecciona opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario = iniciar_sesion()
            if usuario:
                return usuario
        elif opcion == '3':
            return None
        else:
            print("Opción inválida.")

from finanzas import registrar_movimiento, ver_movimientos

def menu_finanzas(usuario):
    while True:
        print(f"\n--- Menú Finanzas ({usuario['nombre']}) ---")
        print("1. Registrar ingreso")
        print("2. Registrar gasto")
        print("3. Ver todos los movimientos")
        print("4. Volver al menú principal")
        opcion = input("Selecciona opción: ")

        if opcion == '1':
            registrar_movimiento(usuario, tipo='ingreso')
        elif opcion == '2':
            registrar_movimiento(usuario, tipo='gasto')
        elif opcion == '3':
            ver_movimientos(usuario)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")


from metas import registrar_meta, ver_metas, eliminar_meta, editar_meta

def menu_metas(usuario):
    while True:
        print(f"\n--- Menú de Metas ({usuario['nombre']}) ---")
        print("1. Registrar nueva meta")
        print("2. Ver mis metas")
        print("3. Eliminar meta")
        print("4. Editar meta")
        print("5. Volver al menú principal")
        opcion = input("Selecciona opción: ")

        if opcion == "1":
            registrar_meta(usuario)
        elif opcion == "2":
            ver_metas(usuario)
        elif opcion == "3":
            eliminar_meta(usuario)
        elif opcion == "4":
            editar_meta(usuario)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
