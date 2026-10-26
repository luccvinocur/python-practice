import tkinter as tk
from tkinter import messagebox

def mostrar_alerta():
    """
    Muestra una alerta de advertencia usando Tkinter.
    """
    messagebox.showwarning("Advertencia", "El temporizador llego a su FIN!")

# Crear ventana principal oculta
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# Mostrar la alerta
mostrar_alerta()

# Cerrar la aplicación
root.destroy()
