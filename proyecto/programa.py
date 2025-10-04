#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

from clases.gato import Gato
from clases.hamster import Hamster
from clases.pajaro import Pajaro
from clases.perro import Perro
from clases.ratita import Ratita

def actualizar_campos(event=None):
    for widget in campos_frame.winfo_children():
        widget.destroy()

    animal = combo_animal.get()

    global entradas 
    entradas = {}

    if animal == "Gato":
        etiquetas = ["Nombre", "Edad (años)", "Peso (kg)", "Castrado (sí/no)", "Síntomas"]
    elif animal == "Hamster":
        etiquetas = ["Nombre", "Raza", "Peso (kg)", "Altura (cm)", "Síntomas"]
    elif animal == "Pájaro":
        etiquetas = ["Nombre", "Tipo", "Peso (kg)", "Altura (cm)", "Síntomas"]
    elif animal == "Perro":
        etiquetas = ["Nombre", "Raza", "Peso (kg)", "Altura (cm)", "Síntomas (separar con coma)"]
    elif animal == "Ratita":
        etiquetas = ["Nombre", "Peso (gramos)", "Edad (meses)", "Síntomas", "Actividad"]
    else:
        etiquetas = []

    for i, etiqueta in enumerate(etiquetas):
        lbl = ttk.Label(campos_frame, text=etiqueta)
        lbl.grid(row=i, column=0, sticky="w", pady=2)
        ent = ttk.Entry(campos_frame, width=30)
        ent.grid(row=i, column=1, pady=2)
        entradas[etiqueta] = ent

def mostrar_info():
    salida.delete("1.0", tk.END)

    animal = combo_animal.get()
    try:
        if animal == "Gato":
            nombre = entradas["Nombre"].get()
            edad = int(entradas["Edad (años)"].get())
            peso = float(entradas["Peso (kg)"].get())
            castrado = entradas["Castrado (sí/no)"].get().strip().lower() == "sí"
            sintomas = entradas["Síntomas"].get()

            mascota = Gato(nombre, edad, peso, castrado, sintomas)

            salida.insert(tk.END, f"Gato: {mascota.nombre}\n")
            for e in mascota.evaluar_salud():
                salida.insert(tk.END, f"- {e}\n")

        elif animal == "Hamster":
            nombre = entradas["Nombre"].get()
            raza = entradas["Raza"].get()
            peso = float(entradas["Peso (kg)"].get())
            altura = float(entradas["Altura (cm)"].get())
            sintomas = entradas["Síntomas"].get()

            mascota = Hamster(nombre, raza, peso, altura, sintomas)

            salida.insert(tk.END, f"Hamster: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Raza: {mascota.raza}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} kg\n")
            salida.insert(tk.END, f"- Altura: {mascota.altura} cm\n")
            salida.insert(tk.END, f"- Síntomas: {mascota.sintomas}\n")

        elif animal == "Pájaro":
            nombre = entradas["Nombre"].get()
            tipo = entradas["Tipo"].get()
            peso = float(entradas["Peso (kg)"].get())
            altura = float(entradas["Altura (cm)"].get())
            sintomas = entradas["Síntomas"].get()

            mascota = Pajaro(nombre, tipo, peso, altura, sintomas)

            salida.insert(tk.END, f"Pájaro: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Tipo: {mascota.tipo}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} kg\n")
            salida.insert(tk.END, f"- Altura: {mascota.altura} cm\n")
            salida.insert(tk.END, f"- Síntomas: {mascota.sintomas}\n")

        elif animal == "Perro":
            nombre = entradas["Nombre"].get()
            raza = entradas["Raza"].get()
            peso = float(entradas["Peso (kg)"].get())
            altura = float(entradas["Altura (cm)"].get())
            sintomas = [s.strip() for s in entradas["Síntomas (separar con coma)"].get().split(",")]

            mascota = Perro(nombre, raza, peso, altura, sintomas)

            salida.insert(tk.END, f"Perro: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Raza: {mascota.raza}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} kg\n")
            salida.insert(tk.END, f"- Altura: {mascota.altura} cm\n")
            salida.insert(tk.END, f"- Síntomas: {', '.join(mascota.sintomas)}\n")
            for e in mascota.evaluar_salud():
                salida.insert(tk.END, f"- {e}\n")

        elif animal == "Ratita":
            nombre = entradas["Nombre"].get()
            peso = int(entradas["Peso (gramos)"].get())
            edad = int(entradas["Edad (meses)"].get())
            sintomas = entradas["Síntomas"].get()
            actividad = entradas["Actividad"].get()

            mascota = Ratita(nombre, peso, edad, sintomas, actividad)

            salida.insert(tk.END, f"Ratita: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} gramos\n")
            salida.insert(tk.END, f"- Edad: {mascota.edad} meses\n")
            salida.insert(tk.END, f"- Síntomas: {mascota.sintomas}\n")
            salida.insert(tk.END, f"- Actividad: {mascota.actividad}\n")
            for r in mascota.evaluar_salud():
                salida.insert(tk.END, f"- {r}\n")

        else:
            salida.insert(tk.END, "Por favor, selecciona un animal válido.\n")

    except ValueError as ve:
        messagebox.showerror("Error de entrada", f"Por favor, verifica los datos ingresados.\n{ve}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

root = tk.Tk()
root.title("Evaluación de Salud de Mascotas")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Selecciona el animal:").grid(row=0, column=0, sticky="w")
combo_animal = ttk.Combobox(frame, values=["Gato", "Hamster", "Pájaro", "Perro", "Ratita"], state="readonly")
combo_animal.grid(row=0, column=1)
combo_animal.bind("<<ComboboxSelected>>", actualizar_campos)

campos_frame = ttk.Frame(frame)
campos_frame.grid(row=1, column=0, columnspan=2, pady=10)

boton = ttk.Button(frame, text="Mostrar Evaluación", command=mostrar_info)
boton.grid(row=2, column=0, columnspan=2, pady=5)

salida = scrolledtext.ScrolledText(frame, width=60, height=25)
salida.grid(row=3, column=0, columnspan=2)

root.mainloop()