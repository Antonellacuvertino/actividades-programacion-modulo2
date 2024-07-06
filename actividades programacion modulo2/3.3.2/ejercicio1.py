import csv
import json
import os

datos_csv = """Nombre,Edad,Comuna
Juan,21,Puente Alto
María,30,Concepción
Carlos,22,Viña Del Mar
Estela,25,Puerto Montt
"""


csv_file_path = 'datos.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvfile.write(datos_csv)

print(f"El archivo {csv_file_path} ha sido creado.")

personas = []
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        row['Edad'] = int(row['Edad'])
        personas.append(row)
mayores = []
for persona in personas:
    nombre = persona['Nombre']
    edad = persona['Edad']
    comuna = persona['Comuna']
    
    if edad >= 18:
        estado_edad = 'Mayor de edad'
    else:
        estado_edad = 'Menor de edad'
    print(f"Nombre: {nombre}, Edad: {edad}, Estado: {estado_edad}, Comuna: {comuna}")
    if edad >= 25:
        mayores.append(persona)
json_file_path = 'mayores.json'
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(mayores, jsonfile, ensure_ascii=False, indent=4)

print(f"La lista de personas mayores o iguales a 25 años se ha guardado en '{json_file_path}'")
