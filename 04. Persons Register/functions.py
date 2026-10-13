usuarios = []

def registrar_usuario():
    nombre = input("Nombre completo: ")
    edad = input("Edad: ")
    correo = input("Correo Electronico: ")
    rol = input("Rol: ")
    contrasena = input("Cree una contrasena: ")

    usuario = usuarios [
        nombre : nombre,
        edad : edad,
        correo : correo,
        rol : rol,
        contrasena : contrasena
    ]

    usuarios.append(usuario)

def iniciar_sesion():
    correo = input("Ingrese el correo registrado: ")
    contrasena = input("Ingrese la contrasena: ")

    for i in usuarios:
        if i[correo] == correo:
            print("Correo encontrado.")
            if i[contrasena] == contrasena:
                print(f"Contrasena correcta, bienvenido {i.nombre}.")
            else:
                print("Acceso deneago. Contrasena incorrecta.")
        else:
            print("Correo no encontrado.")

def mostrar_lista(lista):
    print(lista.list)

def buscar_lista(lista):
    nombre = input("Pon el nombre de la persona a buscar: ")
    for i in usuarios:
        if i[nombre] == nombre:
            print("----USUARIO ENCONTRADO----")
            print("Nombre: i{nombre}")
            print("Edad: i{edad}")
            print("Correo: i{correo}")
            print("Rol: i{rol}")
        else:
            print("Persona NO encontrada en la base.")