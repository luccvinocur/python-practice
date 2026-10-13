import click

tareas = []

@click.group()
def cli():
    pass

@cli.command()
def add():
    print("Agregar una tarea")
    tarea = input("Escriba la tarea a realizar: ")
    if tarea in tareas:
        print("Esta tarea ya existe.")
    else:
        print("Tarea agregada exitosamente. ")
        tareas.append(tarea)

@cli.command()
def tasks():
    print("Mostrar tareas")
    print(tareas)

@cli.command()
def done():
    print("Eliminar una tarea")
    print(tareas)
    tarea = input("Escribe la tarea que quieres eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea removida exitosamente.")
    else:
        print("Tarea no encontrada.")

if __name__ == "__main__":
    cli()