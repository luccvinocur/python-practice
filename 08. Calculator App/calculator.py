print("====== CALCULADORA ======")
print("Selecciona tu opcion: \n 1. Sumar \n 2. Restar \n 3. Dividir \n 4. Multiplicar")

while True:
    opcion = int(input("Selecciona tu opcion: "))    

    numero_uno = int(input("Pon un numero: "))
    numero_dos = int(input("Pon un numero: "))
    if opcion == 1:
        print(numero_uno + numero_dos)
    elif opcion == 2:
        print(numero_uno - numero_dos)
    elif opcion == 3:
        print(numero_uno / numero_dos)
    else:
        print(numero_uno * numero_dos)