import tkinter as tk
from clases.perro import Perro
from clases.gato import Gato

def crear_animal(tipo):
    datos = { 
        "nombre": entry_nombre.get(),
        "raza": entry_raza.get(),
        "edad": entry_edad.get(),
        "color": entry_color.get(),
        "peso": entry_peso.get()
    }

    if not all(datos.values()):
        label_resultado.config(text="⚠️ Todos los campos son obligatorios", fg="red")
        return

    try:
        datos["edad"] = int(datos["edad"])
        datos["peso"] = float(datos["peso"])
    except ValueError:
        label_resultado.config(text="⚠️ Edad debe ser entero y peso decimal", fg="red")
        return

    if tipo == "perro":
        animal = Perro(datos["nombre"], datos["raza"], datos["edad"], datos["color"], datos["peso"])
        color = "green"
    else:
        animal = Gato(datos["nombre"], datos["edad"], datos["color"], datos["raza"], datos["peso"])
        color = "blue"

    label_resultado.config(text=str(animal), fg=color)

root = tk.Tk()
root.title("Crear Animal")
root.geometry("350x300")

campos = ["Nombre", "Raza", "Edad", "Color", "Peso (kg)"]
entradas = []

for i, campo in enumerate(campos):
    tk.Label(root, text=campo + ":").grid(row=i, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entradas.append(entry)

entry_nombre, entry_raza, entry_edad, entry_color, entry_peso = entradas

tk.Button(root, text="Crear Perro", command=lambda: crear_animal("perro")).grid(row=5, column=0, pady=10)
tk.Button(root, text="Crear Gato", command=lambda: crear_animal("gato")).grid(row=5, column=1, pady=10)

label_resultado = tk.Label(root, text="", fg="black", justify="left")
label_resultado.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
