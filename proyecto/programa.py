import tkinter as tk
from clases.perro import Perro
from clases.gato import Gato
from clases.tortuga import Tortuga

def crear_animal(tipo):
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    extra1 = entry_extra1.get()
    peso = entry_peso.get()
    extra2 = entry_extra2.get()

    if not all([nombre, edad, extra1, peso, extra2]):
        label_resultado.config(text="⚠️ Todos los campos son obligatorios", fg="red")
        return

    try:
        edad = int(edad)
        peso = float(peso)
    except ValueError:
        label_resultado.config(text="⚠️ Edad debe ser entero y peso decimal", fg="red")
        return

    if tipo == "perro":
        animal = Perro(nombre, extra1, edad, extra2, peso)
        color = "green"
    elif tipo == "gato":
        animal = Gato(nombre, edad, extra1, extra2, peso)
        color = "blue"
    elif tipo == "tortuga":
        animal = Tortuga(nombre, edad, extra1, peso, extra2)
        color = "brown"
    else:
        label_resultado.config(text="Tipo de animal no válido", fg="red")
        return

    label_resultado.config(text=str(animal), fg=color)

def actualizar_labels(tipo):
    if tipo == "perro":
        label_extra1.config(text="Raza:")
        label_extra2.config(text="Color:")
        btn_crear.config(command=lambda: crear_animal("perro"))
    elif tipo == "gato":
        label_extra1.config(text="Color:")
        label_extra2.config(text="Raza:")
        btn_crear.config(command=lambda: crear_animal("gato"))
    elif tipo == "tortuga":
        label_extra1.config(text="Especie:")
        label_extra2.config(text="Color caparazón:")
        btn_crear.config(command=lambda: crear_animal("tortuga"))

# Interfaz
root = tk.Tk()
root.title("Crear Animal")
root.geometry("400x400")

# Entradas comunes
tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Edad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1)

label_extra1 = tk.Label(root, text="Extra1:")
label_extra1.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_extra1 = tk.Entry(root)
entry_extra1.grid(row=2, column=1)

tk.Label(root, text="Peso (kg):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_peso = tk.Entry(root)
entry_peso.grid(row=3, column=1)

label_extra2 = tk.Label(root, text="Extra2:")
label_extra2.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_extra2 = tk.Entry(root)
entry_extra2.grid(row=4, column=1)

# Selector de tipo de animal
frame_botones = tk.Frame(root)
frame_botones.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(frame_botones, text="🐶 Perro", command=lambda: actualizar_labels("perro")).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="🐱 Gato", command=lambda: actualizar_labels("gato")).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="🐢 Tortuga", command=lambda: actualizar_labels("tortuga")).grid(row=0, column=2, padx=5)

# Botón Crear
btn_crear = tk.Button(root, text="Crear Animal", state="normal")
btn_crear.grid(row=6, column=0, columnspan=2, pady=10)

# Resultado
label_resultado = tk.Label(root, text="", fg="black", justify="left", wraplength=350)
label_resultado.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
