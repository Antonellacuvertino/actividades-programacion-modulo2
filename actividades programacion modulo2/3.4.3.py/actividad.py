def validar_lista_numeros():
    while True:
        try:
            numeros = input("Ingrese una lista de números enteros separados por espacios: ")
            numeros = numeros.split()
            numeros = [int(num) for num in numeros]  
            return numeros
        except ValueError:
            print("Error: Ingrese solo números enteros válidos. Intente nuevamente.")

def identificar_pares_impares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

def mostrar_resultados(pares, impares):
    print("\nNúmeros pares encontrados:")
    if pares:
        print(pares)
    else:
        print("No se encontraron números pares.")

    print("\nNúmeros impares encontrados:")
    if impares:
        print(impares)
    else:
        print("No se encontraron números impares.")

def main():
    print("Programa para identificar números pares e impares")
    print("=================================================")

    numeros = validar_lista_numeros()
    pares, impares = identificar_pares_impares(numeros)
    mostrar_resultados(pares, impares)

if __name__ == "__main__":
    main()
