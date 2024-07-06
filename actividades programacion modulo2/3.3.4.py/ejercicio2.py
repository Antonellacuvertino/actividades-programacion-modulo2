def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

def validar_numero(entrada):
    try:
        valor = float(entrada)
        if valor.is_integer():
            valor = int(valor)
        return valor
    except ValueError:
        return None

def main():
    print("Calculadora básica")
    print("==================")

    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elija una operación (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        try:
            num1 = input("Ingrese el primer número: ")
            num1 = validar_numero(num1)
            if num1 is None:
                print("Error: Ingrese un número válido.")
                continue

            num2 = input("Ingrese el segundo número: ")
            num2 = validar_numero(num2)
            if num2 is None:
                print("Error: Ingrese un número válido.")
                continue
        except ValueError:
            print("Error: Ingrese números válidos.")
            continue

        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"Resultado de sumar {num1} y {num2}: {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"Resultado de restar {num2} de {num1}: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"Resultado de multiplicar {num1} por {num2}: {resultado}")
        elif opcion == '4':
            resultado = dividir(num1, num2)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"Resultado de dividir {num1} por {num2}: {resultado}")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
