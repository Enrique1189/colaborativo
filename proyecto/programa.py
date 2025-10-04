#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s

import tkinter as tk
from tkinter import ttk, messagebox
from proyecto.mascota import Mascota

ventana = tk.Tk()
ventana.title("🐾 Veterinaria Moradita 🐾")
ventana.geometry("700x500")
ventana.config(bg="#d8b4fe")  
mascotas_registradas = []

def registrar_datos():
    nombre_mascota = entry_nombre.get()
    especie = entry_especie.get()
    raza = entry_raza.get()
    edad = entry_edad.get()
    dueño = entry_dueño.get()

    if not (nombre_mascota and especie and raza and edad and dueño):
        messagebox.showwarning("Todos los campos son obligatorios")
        return

    mascota = Mascota(nombre_mascota, especie, raza, edad, dueño)
    mascotas_registradas.append(mascota)

    tree.insert("", "end", values=(nombre_mascota, especie, raza, edad, dueño))

    contador_label.config(text=f"Mascotas registradas: {len(mascotas_registradas)}")

    entry_nombre.delete(0, tk.END)
    entry_especie.delete(0, tk.END)
    entry_raza.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_dueño.delete(0, tk.END)

tk.Label(ventana, text="Registro de Mascotas", bg="#d8b4fe", fg="#581c87", font=("Arial Rounded MT Bold", 18)).pack(pady=15)

frame = tk.Frame(ventana, bg="#f3e8ff", bd=3, relief="ridge")
frame.pack(pady=10, padx=40)

tk.Label(frame, text="Nombre:", bg="#f3e8ff").grid(row=0, column=0, sticky="e", pady=5, padx=5)
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=0, column=1)

tk.Label(frame, text="Especie:", bg="#f3e8ff").grid(row=1, column=0, sticky="e", pady=5, padx=5)
entry_especie = tk.Entry(frame)
entry_especie.grid(row=1, column=1)

tk.Label(frame, text="Raza:", bg="#f3e8ff").grid(row=2, column=0, sticky="e", pady=5, padx=5)
entry_raza = tk.Entry(frame)
entry_raza.grid(row=2, column=1)

tk.Label(frame, text="Edad:", bg="#f3e8ff").grid(row=3, column=0, sticky="e", pady=5, padx=5)
entry_edad = tk.Entry(frame)
entry_edad.grid(row=3, column=1)

tk.Label(frame, text="Dueño:", bg="#f3e8ff").grid(row=4, column=0, sticky="e", pady=5, padx=5)
entry_dueño = tk.Entry(frame)
entry_dueño.grid(row=4, column=1)

boton_registrar = ttk.Button(ventana, text="Registrar Mascota", command=registrar_datos)
boton_registrar.pack(pady=10)

tree = ttk.Treeview(ventana, columns=("Nombre", "Especie", "Raza", "Edad", "Dueño"), show="headings", height=8)
tree.pack(pady=10)

tree["columns"] = ("Nombre", "Especie", "Raza", "Edad", "Dueño")
for col in tree["columns"]:
    tree.heading(col, text=col)

contador_label = tk.Label(ventana, text="Mascotas registradas: 0", bg="#d8b4fe", fg="#581c87", font=("times new roman", 12, "bold"))
contador_label.pack(pady=5)

tk.Label(ventana, text="🐶💜 Clínica Veterinaria Moradita 💜🐱", bg="#d8b4fe", fg="#581c87", font=("times new roman", 10, "italic")).pack(side="bottom", pady=15)

ventana.mainloop()
