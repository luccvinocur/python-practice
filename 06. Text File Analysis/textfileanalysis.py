with open("text.txt", "r") as f:
    texto = f.read()
    palabras = texto.split()
    print(f"Total de palabras: {len(palabras)}")