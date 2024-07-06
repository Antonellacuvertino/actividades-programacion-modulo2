import json

datos = [
    {'run': '10744679-6', 'nombre': 'Jose Haro'},
    {'run': '19881120-3', 'nombre': 'Daniela Almonacid'},
    {'run': '16112356-0', 'nombre': 'Carlos González'},
    {'run': '17651562-7', 'nombre': 'Andrea Soto'},
    {'run': '13429495-7', 'nombre': 'Luis Torres'},
    {'run': '17470063-K', 'nombre': 'Maria Rodríguez'},
    {'run': '19089980-2', 'nombre': 'Pablo Fernández'},
    {'run': '17449807-5', 'nombre': 'Valentina Pérez'},
    {'run': '13154134-1', 'nombre': 'Nicolás Vargas'},
    {'run': '14073175-7', 'nombre': 'Antonella Muñoz'},
    {'run': '24052019-2', 'nombre': 'Felipe Silva'},
    {'run': '27779771-2', 'nombre': 'Sofía López'},
    {'run': '23135155-8', 'nombre': 'Juan Díaz'},
    {'run': '25449950-1', 'nombre': 'Isabel Castro'},
    {'run': '22398351-0', 'nombre': 'Diego Morales'},
    {'run': '20449542-4', 'nombre': 'Ana Smith'},
    {'run': '27730053-2', 'nombre': 'Matías Araya'},
    {'run': '27358198-7', 'nombre': 'Valeria Mendoza'},
    {'run': '25130662-1', 'nombre': 'Gabriel Pérez'},
    {'run': '24981167-K', 'nombre': 'Martina Ruiz'},
    {'run': '22096175-3', 'nombre': 'Sebastián Herrera'},
    {'run': '23010574-K', 'nombre': 'Francisca Flores'},
    {'run': '24218263-4', 'nombre': 'Ricardo González'},
    {'run': '28942147-5', 'nombre': 'Constanza Álvarez'},
    {'run': '27165749-8', 'nombre': 'Javiera Troncoso'},
    {'run': '22216307-2', 'nombre': 'Eduardo Navarro'},
    {'run': '22425010-K', 'nombre': 'Catalina Vargas'},
    {'run': '23811768-2', 'nombre': 'Ángela Soto'},
    {'run': '24661213-7', 'nombre': 'Cristian Mora'},
    {'run': '20781422-9', 'nombre': 'Carla Contreras'},
    {'run': '10363927-1', 'nombre': 'Mauricio Rojas'},
    {'run': '12598545-9', 'nombre': 'Marcela Fernández'},
    {'run': '19105327-3', 'nombre': 'Felipe Montes'},
    {'run': '19539754-6', 'nombre': 'Alejandra Oyarzún'},
    {'run': '15731749-0', 'nombre': 'Pedro Ramírez'},
    {'run': '12865638-3', 'nombre': 'Daniela Aravena'},
    {'run': '10294021-0', 'nombre': 'Francisco Valdés'},
    {'run': '14104975-5', 'nombre': 'Florencia Rojas'},
    {'run': '11975810-6', 'nombre': 'Rodrigo Gómez'},
    {'run': '17500269-3', 'nombre': 'Amanda Guzmán'}
]

terminaciones = ['92', '95', '84']

ganadores = []


for dato in datos:
    run = dato['run']
    nombre = dato['nombre']
    if any(run.endswith(t) for t in terminaciones):
        ganadores.append({'run': run, 'nombre': nombre})

archivo_json = 'ganadores.json'
with open(archivo_json, 'w', encoding='utf-8') as jsonfile:
    json.dump(ganadores, jsonfile, ensure_ascii=False, indent=4)

print(f'Se han encontrado {len(ganadores)} ganadores. Se han guardado en {archivo_json}.')

