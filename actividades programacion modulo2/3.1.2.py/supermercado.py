def main():
    productos = {
        1: {"nombre": "Leche", "precio": 2.50},
        2: {"nombre": "Pan", "precio": 1.50},
        3: {"nombre": "Huevos", "precio": 3.25},
        4: {"nombre": "Queso", "precio": 4.00},
        5: {"nombre": "Yogurt", "precio": 1.75}
    }
    carrito = []
    
    while True:
        print("\nMenú:")
        print("1. Agregar productos")
        print("2. Ver canasta")
        print("3. Ver total")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            agregar_productos(productos, carrito)
        elif opcion == "2":
            ver_canasta(carrito)
        elif opcion == "3":
            ver_total(carrito)
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema de ventas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

def agregar_productos(productos, carrito):
    print("\nAgregar productos:")
    print("Seleccione un producto para agregar al carrito:")
    
    for key, value in productos.items():
        print(f"{key}. {value['nombre']} - ${value['precio']:.2f}")
    
    while True:
        seleccion = input("Ingrese el número del producto (1-5) o '0' para salir: ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if seleccion == 0:
                break
            elif seleccion in productos:
                carrito.append(productos[seleccion])
                print(f"Producto '{productos[seleccion]['nombre']}' agregado al carrito.")
                break
            else:
                print("Número de producto no válido. Intente de nuevo.")
        else:
            print("Entrada no válida. Intente de nuevo.")

def ver_canasta(carrito):
    print("\nProductos en la canasta:")
    if not carrito:
        print("El carrito está vacío.")
    else:
        for producto in carrito:
            print(f"{producto['nombre']} - ${producto['precio']:.2f}")

def ver_total(carrito):
    total = sum(producto['precio'] for producto in carrito)
    print(f"\nTotal a pagar: ${total:.2f}")

if __name__ == "__main__":
    main()
