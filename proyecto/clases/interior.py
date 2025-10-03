import tkinter as tk
from tkinter import messagebox

class InteriorAuto:
    def __init__(self, marca, tipo_asientos, material, color, sistema_audio):
        self.marca = marca
        self.tipo_asientos = tipo_asientos
        self.material = material
        self.color = color
        self.sistema_audio = sistema_audio

    def obtener_info(self):
        return (
            f"Marca: {self.marca}\n"
            f"Tipo de Asientos: {self.tipo_asientos}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Sistema de Audio: {self.sistema_audio}"
        )

def mostrar_interior():
    marca = entry_marca.get()
    tipo_asientos = entry_tipo_asientos.get()
    material = entry_material.get()
    color = entry_color.get()
    sistema_audio = entry_sistema_audio.get()

    if not (marca and tipo_asientos and material and color and sistema_audio):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
        return

    interior = InteriorAuto(marca, tipo_asientos, material, color, sistema_audio)
    info = interior.obtener_info()
    messagebox.showinfo("Información del Interior del Auto", info)

ventana = tk.Tk()
ventana.title("Registro de Interior de Auto")
ventana.geometry("350x300")

tk.Label(ventana, text="Marca del Auto:").pack()
entry_marca = tk.Entry(ventana)
entry_marca.pack()

tk.Label(ventana, text="Tipo de Asientos:").pack()
entry_tipo_asientos = tk.Entry(ventana)
entry_tipo_asientos.pack()

tk.Label(ventana, text="Material:").pack()
entry_material = tk.Entry(ventana)
entry_material.pack()

tk.Label(ventana, text="Color:").pack()
entry_color = tk.Entry(ventana)
entry_color.pack()

tk.Label(ventana, text="Sistema de Audio:").pack()
entry_sistema_audio = tk.Entry(ventana)
entry_sistema_audio.pack()

tk.Button(ventana, text="Mostrar información", command=mostrar_interior).pack(pady=10)

ventana.mainloop()
