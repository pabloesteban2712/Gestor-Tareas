#GESTOR DE TAREAS CON INTERFAZ

import tkinter as tk
from tkinter import messagebox
import json

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")  # Tamaño de la ventana

# Lista global de tareas
tareas = []

# Función para añadir una tarea
def anadir_tarea():
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()
    prioridad = prioridad_var.get()

    if not nombre or not descripcion:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre y la descripción de la tarea.")
        return
    
    # Diccionario de la tarea con ':' en lugar de '='
    tarea = {
        "nombre": nombre,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }

    tareas.append(tarea)
    actualizar_lista()
    entry_nombre.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para actualizar la lista de tareas mostrada en el frame
def actualizar_lista():
    for tarea_widget in frame_tareas.winfo_children():
        tarea_widget.destroy()

    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        tarea_texto = f"{i + 1}. {tarea['nombre']} - {tarea['prioridad']} ({estado})"
        label_tarea = tk.Label(frame_tareas, text=tarea_texto, anchor="w", justify="left")
        label_tarea.pack(fill="x")

# Función para borrar una tarea
def borrar_tarea():
    try:
        index = int(entry_borrar.get()) - 1
        if 0 <= index < len(tareas):
            tareas.pop(index)
            actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Índice de tarea inválido.")
    except ValueError:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un número válido.")

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        index = int(entry_completada.get()) - 1
        if 0 <= index < len(tareas):
            tareas[index]["completada"] = True
            actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Índice de tarea inválido.")
    except ValueError:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un número válido.")

# Campos de entrada para nombre y descripción de la tarea
entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack(pady=5)
entry_nombre.insert(0, "Nombre de la tarea")

entry_descripcion = tk.Entry(root, width=40)
entry_descripcion.pack(pady=5)
entry_descripcion.insert(0, "Descripción de la tarea")

# Menú desplegable para elegir la prioridad
prioridad_var = tk.StringVar()
prioridad_var.set("Alta")  # Valor por defecto
prioridad_menu = tk.OptionMenu(root, prioridad_var, "Alta", "Media", "Baja")
prioridad_menu.pack(pady=5)

# Botón para añadir tarea
btn_anadir = tk.Button(root, text="Añadir tarea", command=anadir_tarea)
btn_anadir.pack(pady=10)

# Campo para ingresar el índice de la tarea a borrar
entry_borrar = tk.Entry(root, width=20)
entry_borrar.pack(pady=5)
entry_borrar.insert(0, "Número de tarea a borrar")

btn_borrar = tk.Button(root, text="Borrar tarea", command=borrar_tarea)
btn_borrar.pack(pady=5)

# Campo para ingresar el índice de la tarea a marcar como completada
entry_completada = tk.Entry(root, width=20)
entry_completada.pack(pady=5)
entry_completada.insert(0, "Número de tarea completada")

btn_completada = tk.Button(root, text="Marcar como completada", command=marcar_completada)
btn_completada.pack(pady=5)

# Frame para mostrar la lista de tareas
frame_tareas = tk.Frame(root, relief="groove", borderwidth=2)
frame_tareas.pack(pady=10, fill="both", expand=True)

# Iniciar el loop de la aplicación
root.mainloop()
