import re

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

sesion_iniciada = False
usuario_actual = None

def registrar_usuario():
    nombre = input("Nombre completo: ")
    edad = input("Edad: ")
    correo = input("Correo Electronico: ")
    patron_correo = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    while not re.match(patron_correo, correo):
        print("Correo inválido.")
        correo = input("Correo Electronico: ")
    rol = input("Rol: ").title()

    roles_validos = [
        "Administrador",
        "Supervisor",
        "Recursos Humanos",
        "Auditor",
        "Editor",
        "Operador",
        "Usuario",
        "Invitado"
    ]
    while rol not in roles_validos:
        print("El rol seleccionado NO existe.")
        rol = input("Rol: ").title()
    contrasena = input("Cree una contrasena (Entre 8 y 15 caracteres): ")
    while len(contrasena) < 8 or len(contrasena) > 15:
        print("Contrasena no VALIDA, asegurese que tenga entre 8 y 15 caracteres.")
        contrasena = input("Cree una contrasena (Entre 8 y 15 caracteres): ")

    usuario = {
        nombre : nombre,
        edad : edad,
        correo : correo,
        rol : rol,
        contrasena : contrasena
    }

    print("Usuario creado EXITOSAMENTE.")
    usuarios.append(usuario)

def iniciar_sesion():
    global sesion_iniciada
    global usuario_actual
    correo = input("Ingrese el correo registrado: ")
    contrasena = input("Ingrese la contrasena: ")

    for i in usuarios:
        if i["correo"] == correo:
            print("Correo encontrado.")
            if i["contrasena"] == contrasena:
                print(f"Contrasena correcta, bienvenido {i["nombre"]}.")
                sesion_iniciada = True
                usuario_actual = i
            else:
                print("Acceso deneago. Contrasena incorrecta.")
            
            return
    print("Correo no encontrado.")

def mostrar_lista(lista):
    if sesion_iniciada == False:
        print("Debes de iniciar sesión primero. ")
    else:
        if usuario_actual["rol"] in [
            "Administrador",
            "Supervisor",
            "Recursos Humanos",
            "Auditor"
        ]:
            for persona in usuarios:
                    print(f"\nNombre: {persona["nombre"]} | Edad: {persona["edad"]} | Correo: {persona["correo"]} | Rol: {persona["rol"]}\n")
        else:
            print("Acceso denegado")

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

