def main():
    usuarios = {}
    
    while True:
        print("\nMenú:")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            iniciar_sesion(usuarios)
        elif opcion == "2":
            registrar_usuario(usuarios)
        elif opcion == "3":
            eliminar_usuario(usuarios)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

def iniciar_sesion(usuarios):
    print("\nInicio de sesión")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Error: Nombre de usuario o contraseña incorrectos.")

def registrar_usuario(usuarios):
    print("\nRegistro de usuario")
    usuario = input("Ingrese un nombre de usuario: ")
    
    if usuario in usuarios:
        print("Error: El usuario ya existe.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        usuarios[usuario] = contrasena
        print("Usuario registrado correctamente.")

def eliminar_usuario(usuarios):
    print("\nEliminar usuario")
    usuario = input("Ingrese el nombre de usuario que desea eliminar: ")
    
    if usuario in usuarios:
        contrasena = input("Por favor, confirme su contraseña para eliminar este usuario: ")
        
        if usuarios[usuario] == contrasena:
            del usuarios[usuario]
            print(f"Usuario '{usuario}' eliminado correctamente.")
        else:
            print("Error: Contraseña incorrecta. No se puede eliminar el usuario.")
    else:
        print("Error: El usuario especificado no existe.")

if __name__ == "__main__":
    main()
