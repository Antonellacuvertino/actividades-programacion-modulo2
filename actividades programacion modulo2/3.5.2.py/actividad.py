def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero.")
    return a / b

def main():
    print("Calculadora básica")
    print("==================")

    while True:
        try:
            opcion = int(input("\nElija una operación:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\nOpción: "))
            
            if opcion == 5:
                print("¡Hasta luego!")
                break
            
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == 1:
                print(f"Resultado de sumar {num1} y {num2}: {sumar(num1, num2)}")
            elif opcion == 2:
                print(f"Resultado de restar {num2} de {num1}: {restar(num1, num2)}")
            elif opcion == 3:
                print(f"Resultado de multiplicar {num1} por {num2}: {multiplicar(num1, num2)}")
            elif opcion == 4:
                try:
                    print(f"Resultado de dividir {num1} por {num2}: {dividir(num1, num2)}")
                except ValueError as e:
                    print(e)
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Error: Ingrese números válidos.")

if __name__ == "__main__":
    main()
