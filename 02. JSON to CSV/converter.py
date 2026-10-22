import csv
import json

#Usamos Json como imporacion para poder leer el erchivo

with open("personas.json", "r") as archivo_json:
    contenido = json.load(archivo_json)

print(type(contenido))
columnas = contenido[0].keys()

with open("personas.csv", "w") as archivo_csv:
    fieldnames = columnas
    escritor = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
    escritor.writeheader()
    escritor.writerows(contenido)