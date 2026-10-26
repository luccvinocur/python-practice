import random

opciones = ["piedra","papel","tijera"]
seleccion_opcion = random.choice(opciones)

usuario_opcion = input("Selecciona tu opcion (Piedra, Papel o Tijera)").capitalize()

if seleccion_opcion == "piedra":
    print("La IA selecciono: PIEDRA")
    if usuario_opcion == "Piedra":
        print("Tu seleccionaste: PIEDRA")
        print("EMPATE")
    elif usuario_opcion == "Papel":
        print("Tu seleccionaste: PAPEL")
        print("GANASTE")
    elif usuario_opcion == "Tijera":
        print("Tu seleccionaste: TIJERA")
        print("PERDISTE")
    else:
        print("Opcion Invalida")
elif seleccion_opcion == "papel":
    print("La IA selecciono: PAPEL")
    if usuario_opcion == "Piedra":
        print("Tu seleccionaste: PIEDRA")
        print("PERDISTE")
    elif usuario_opcion == "Papel":
        print("Tu seleccionaste: PAPEL")
        print("EMPATE")
    elif usuario_opcion == "Tijera":
        print("Tu seleccionaste: TIJERA")
        print("GANASTE")
    else:
        print("Opcion Invalida")
else:
    print("La IA selecciono: TIJERA")
    if usuario_opcion == "Piedra":
        print("Tu seleccionaste: PIEDRA")
        print("GANASTE")
    elif usuario_opcion == "Papel":
        print("Tu seleccionaste: PAPEL")
        print("PERDISTE")
    elif usuario_opcion == "Tijera":
        print("Tu seleccionaste: TIJERA")
        print("EMPATE")
    else:
        print("Opcion Invalida")