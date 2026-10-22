#Pasos
#1. Importar libreria necesaria -> Random
#2. Abrir con R el archivo TXT
#3. Permitir separar el archivo TXT en una lista
#4. Crear una variable que tome alguna palabra con randomchoice de la lista

import random

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    partes = contenido.split()
    palabra_random = random.choice(partes)

    print(palabra_random)