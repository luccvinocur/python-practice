import random
import string

letras = ""
cantidad = int(input("Ingrese la cantidad de caracteres que quiere que tenga su contrasena: "))

abec = (input("Incluir letras (True | False): ")).capitalize()
numeros = (input("Incluir numeros (True | False): ").capitalize())
simbolos = (input("Incluir simbolos (True | False): ").capitalize())

if abec == "True":
    mayusculas = (input("Usar mayusculas (True | False): ").capitalize())
    minusculas = (input("Usar minusculas (True | False): ").capitalize())
    if mayusculas == "True":
        letras = string.ascii_uppercase
    if minusculas == "True":
        letras += string.ascii_lowercase
if numeros == "True":
    letras = letras + string.digits

if simbolos == "True":
    letras = letras + string.punctuation

if letras == "":
    print("El programa se detiene porque el usuario no indico que tipo de contrasena desea.")
else:
    contrasena = ""
    for i in range(0, cantidad):
        letra = random.choice(letras)
        contrasena = contrasena + letra
    print(contrasena)    





