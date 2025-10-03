import tkinter as tk
from clases.perro import Perro


def crear_perro():
    nombre = entry_nombre.get()
    raza = entry_raza.get()
    edad = entry_edad.get()
    color = entry_color.get()
    peso = entry_peso.get()

    if not (nombre and raza and edad and color and peso):
        label_resultado.config(text="⚠️ Todos los campos son obligatorios")
        return

    try:
        edad = int(edad)
        peso = float(peso)
    except ValueError:
        label_resultado.config(text="⚠️ Edad debe ser entero y peso decimal")
        return

    perro = Perro(nombre, raza, edad, color, peso)
    label_resultado.config(text=str(perro))   # Mostrar en pantalla

# Ventana principal
root = tk.Tk()
root.title("Crear Perro")

# Entradas
tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Raza:").grid(row=1, column=0, padx=5, pady=5)
entry_raza = tk.Entry(root)
entry_raza.grid(row=1, column=1)

tk.Label(root, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
entry_edad = tk.Entry(root)
entry_edad.grid(row=2, column=1)

tk.Label(root, text="Color:").grid(row=3, column=0, padx=5, pady=5)
entry_color = tk.Entry(root)
entry_color.grid(row=3, column=1)

tk.Label(root, text="Peso (kg):").grid(row=4, column=0, padx=5, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=4, column=1)

# Botón
btn_crear = tk.Button(root, text="Crear Perro", command=crear_perro)
btn_crear.grid(row=5, column=0, columnspan=2, pady=10)

# Resultado
label_resultado = tk.Label(root, text="", fg="blue", justify="left")
label_resultado.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
