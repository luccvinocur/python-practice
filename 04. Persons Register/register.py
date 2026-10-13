#Idea de crear un gestor de empleados
#La persona puede registrarse, iniciar sesion, ver usuarios, buscar usuarios y salir

#Si la persona no es jefe no puede ver la lista completa de usuarios
#Implementar un archivo CSV en el que se base todo el guardado de documentación -> Mas tarde

import functions as fnc

while True:
    print("---- MENU DE OPCIONES ----\n1. Registrarse\n2. Iniciar Sesión\n3. Ver usuarios (Solo si es jefe)\n4. Buscar usuario\n5. Salir del SISTEMA")
    opcion = int(input("Seleccione la opción que desea: "))

    if opcion == 1:
        fnc.registrar_usuario()
    elif opcion == 2:
        fnc.iniciar_sesion()
    elif opcion == 3:
        fnc.mostrar_lista(fnc.usuarios)
    elif opcion == 4:
        fnc.buscar_lista(fnc.usuarios)
    elif opcion == 5:
        break
    else:
        print("NO SELECCIONASTE NINGUNA OPCIÓN")

