#Imprimir edad por pantalla de 3 diferentes formas, por dias, meses y anos

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

meses = edad * 12
dias = edad * 365

print(f"{nombre} tiene {edad} anos, o {meses} meses o {dias} dias.")