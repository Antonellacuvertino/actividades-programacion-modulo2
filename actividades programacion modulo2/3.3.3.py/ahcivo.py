import csv
import json
import os

datos_csv = """rut,nombre,ventas
72642413-6,Comercial Calcetas Runner,150000000
76437473-2,Reparación Mac,300000000
76254356-9,ProgramaSoftware,27500000
76077262-3,Calzados Roma,15000000
76310800-8,Empresa Arcos,80000000
76283690-4,Casino Coffe,120000000
76952985-5,Cafe Express ltda,50000000
76081440-2,Vino Export SA,20000000
76216579-1,Cepa Merl LTDA,30000000
76597875-0,Comercial Ropa America,60000000
76852106-3,Empresas JP,90000000
76887745-8,Empresas ICata SA,100000000
76210124-2,Buses Peñalolen,150000000
76802052-4,Sandias Paine LTDA,70000000
76575973-1,Modas Junior P,400000000
76869384-2,Bar del 81,25000000
76877803-6,Empresas LLS,8000000
76706124-0,Empresas luz y vida SA,3000000
76162938-1,Empresa Matrix,120000000
"""


csv_file_path = 'listadoRutEmpresa.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvfile.write(datos_csv)

print(f"El archivo {csv_file_path} ha sido creado.")

empresas = []
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       
        row['ventas'] = int(row['ventas'])
        empresas.append(row)
for empresa in empresas:
    ventas = empresa['ventas']
    if ventas <= 100000000:
        empresa['clasificacionEmpresa'] = 'Pequeño Contribuyente'
    elif 100000001 <= ventas <= 200000000:
        empresa['clasificacionEmpresa'] = 'Mediano Contribuyente'
    else:
        empresa['clasificacionEmpresa'] = 'Gran Contribuyente'
json_file_path = 'segmentacionEmpresas.json'
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(empresas, jsonfile, ensure_ascii=False, indent=4)

print(f"La segmentación de empresas se ha guardado en '{json_file_path}'")
