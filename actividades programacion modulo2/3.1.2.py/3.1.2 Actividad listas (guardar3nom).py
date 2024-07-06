def main():
    nombres = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    
    nombre_mas_largo = ""
    for nombre in nombres:
        if len(nombre) > len(nombre_mas_largo):
            nombre_mas_largo = nombre
    
    print(f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}")

if __name__ == "__main__":
    main()
