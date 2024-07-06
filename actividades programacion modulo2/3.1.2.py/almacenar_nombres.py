def main():
    nombres = []
    
    while True:
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
        
        respuesta = input("¿Desea agregar otro nombre? (Sí/No): ").lower()
        if respuesta != "sí" and respuesta != "si":
            break
    
    if nombres:
        nombre_menor = min(nombres, key=len)
        nombres.remove(nombre_menor)
        
        print(f"Lista de nombres, eliminando nombre con menor caracteres: ({nombre_menor}):")
        print(nombres)
    else:
        print("No se han ingresado nombres.")

if __name__ == "__main__":
    main()
