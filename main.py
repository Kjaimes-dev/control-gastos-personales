from menus import mostrar_menu_principal, menu_usuario, menu_finanzas, menu_metas

def main():
    usuario_actual = None
    while True:
        opcion = mostrar_menu_principal()
        if opcion == '1' or opcion == '2':
            usuario_actual = menu_usuario()

        elif opcion == '3':
            if usuario_actual:
                menu_finanzas(usuario_actual)
            else:
                print("Debes iniciar sesión primero.")

        elif opcion == '4':
            if usuario_actual:
                menu_metas(usuario_actual)
            else:
                print("Debes iniciar sesión primero.")

        elif opcion == '5':
            print("Saliendo... ¡Gracias!")
            break
        else:
            print("Opción inválida.")



if __name__ == "__main__":
    main()
