
usuarios = [
    {
        "nombre": "Juan Perez",
        "edad": 25,
        "correo": "juan@gmail.com",
        "rol": "Administrador",
        "contrasena": "Juan123"
    },
    {
        "nombre": "Maria Gonzalez",
        "edad": 30,
        "correo": "maria@gmail.com",
        "rol": "Usuario",
        "contrasena": "Maria456"
    },
    {
        "nombre": "Lucas Fernandez",
        "edad": 22,
        "correo": "lucas@gmail.com",
        "rol": "Editor",
        "contrasena": "Lucas789"
    },
    {
        "nombre": "Sofia Martinez",
        "edad": 28,
        "correo": "sofia@gmail.com",
        "rol": "Usuario",
        "contrasena": "Sofia123"
    },
    {
        "nombre": "Mateo Rodriguez",
        "edad": 35,
        "correo": "mateo@gmail.com",
        "rol": "Administrador",
        "contrasena": "Mateo456"
    },
    {
        "nombre": "Valentina Lopez",
        "edad": 24,
        "correo": "valentina@gmail.com",
        "rol": "Editor",
        "contrasena": "Vale789"
    },
    {
        "nombre": "Santiago Torres",
        "edad": 31,
        "correo": "santiago@gmail.com",
        "rol": "Usuario",
        "contrasena": "Santi123"
    },
    {
        "nombre": "Camila Ramirez",
        "edad": 27,
        "correo": "camila@gmail.com",
        "rol": "Editor",
        "contrasena": "Cami456"
    },
    {
        "nombre": "Benjamin Diaz",
        "edad": 21,
        "correo": "benjamin@gmail.com",
        "rol": "Usuario",
        "contrasena": "Benja789"
    },
    {
        "nombre": "Martina Silva",
        "edad": 29,
        "correo": "martina@gmail.com",
        "rol": "Administrador",
        "contrasena": "Martina123"
    }
]

def registrar_usuario():
    nombre = input("Nombre completo: ")
    edad = input("Edad: ")
    correo = input("Correo Electronico: ")
    rol = input("Rol: ")
    contrasena = input("Cree una contrasena: ")

    usuario = {
        nombre : nombre,
        edad : edad,
        correo : correo,
        rol : rol,
        contrasena : contrasena
    }

    usuarios.append(usuario)

def iniciar_sesion():
    correo = input("Ingrese el correo registrado: ")
    contrasena = input("Ingrese la contrasena: ")

    for i in usuarios:
        if i["correo"] == correo:
            print("Correo encontrado.")
            if i["contrasena"] == contrasena:
                print(f"Contrasena correcta, bienvenido {i["nombre"]}.")
            else:
                print("Acceso deneago. Contrasena incorrecta.")

            return
    print("Correo no encontrado.")

def mostrar_lista(lista):
    print(lista)

def buscar_lista(lista):
    nombre = input("Pon el nombre de la persona a buscar: ")
    for i in usuarios:
        if i["nombre"] == nombre:
            print("----USUARIO ENCONTRADO----")
            print("Nombre: " + i["nombre"])
            print(f"Edad: {i["edad"]}")
            print("Correo: " + i["correo"])
            print("Rol: " + i["rol"])
    return 

    print("Persona NO encontrada")

