#Random numbre Generator

import random

rango = int(input("Hasta que número quieres que se pueda generar?: "))
numero = random.randint(1, rango)
print(numero)