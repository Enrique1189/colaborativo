#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s

# main.py

import tkinter as tk
from tkinter import messagebox

# Importa clases disponibles desde la carpeta 'clases'
from proyecto.clases.hhmj import Gato
# from clases.perro import Perro  ← Otros irán agregando aquí

# Función para manejar el formulario de Gato
def atender_gato():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    peso = entry_peso.get()
    vacunado = var_vacunado.get() == 1
    sintomas = entry_sintomas.get("1.0", tk.END)

    gato = Gato(nombre, edad, peso, vacunado, sintomas)
    resultado = gato.evaluar_salud()

    # Mostrar resultado en ventana
    messagebox.showinfo("Evaluación médica", "\n".join(resultado))

# Ventana principal
root = tk.Tk()
root.title("Clínica Veterinaria")
root.geometry("400x500")

# Título
tk.Label(root, text="Atención para Gato 🐱", font=("Arial", 16)).pack(pady=10)

# Campos de entrada
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=0, column=1)

tk.Label(frame, text="Edad:").grid(row=1, column=0, sticky="e")
entry_edad = tk.Entry(frame)
entry_edad.grid(row=1, column=1)

tk.Label(frame, text="Peso (kg):").grid(row=2, column=0, sticky="e")
entry_peso = tk.Entry(frame)
entry_peso.grid(row=2, column=1)

tk.Label(frame, text="¿Está vacunado?:").grid(row=3, column=0, sticky="e")
var_vacunado = tk.IntVar()
tk.Checkbutton(frame, text="Sí", variable=var_vacunado).grid(row=3, column=1, sticky="w")

tk.Label(root, text="Síntomas:").pack()
entry_sintomas = tk.Text(root, height=5, width=40)
entry_sintomas.pack()

# Botón para procesar
tk.Button(root, text="Evaluar Gato", command=atender_gato).pack(pady=20)

# 📌 Aquí otros compañeros pueden agregar botones o menús para otras clases
# Ejemplo: Evaluar Perro, Evaluar Conejo, etc.

root.mainloop()
