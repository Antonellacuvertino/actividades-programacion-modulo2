matriz = [[0 for _ in range(4)] for _ in range(3)]
for i in range(3):
    for j in range(4):
        matriz[i][j] = int(input(f"Ingrese el elemento para la posición [{i}][{j}]: "))

print("La matriz ingresada es:")
for fila in matriz:
    print(" ".join(map(str, fila)))
arreglo = [
    [["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "amarillo"], ["rojo", "Naranja", "Verde"]],
    [["Blanco", "Naranja", "Verde"], ["amarillo", "rojo", "Blanco"], ["Naranja", "Verde", "amarillo"]],
    [["rojo", "Naranja", "Verde"], ["Blanco", "amarillo", "rojo"], ["Naranja", "Verde", "Blanco"]]
]

contadores = {
    "amarillo": 0,
    "rojo": 0,
    "Naranja": 0,
    "Verde": 0,
    "Blanco": 0
}

for capa in arreglo:
    for fila in capa:
        for color in fila:
            if color in contadores:
                contadores[color] += 1
for color, cantidad in contadores.items():
    print(f"Número de elementos '{color}': {cantidad}")
bus = [[0 for _ in range(4)] for _ in range(10)]
numero_asiento = 1
for i in range(10):
    for j in range(4):
        bus[i][j] = numero_asiento
        numero_asiento += 1

print("Distribución de los asientos en el bus:")
for fila in bus:
    print(" ".join(map(str, fila)))
