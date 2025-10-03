import tkinter as tk
from tkinter import messagebox

class Llanta:
    def __init__(self, marca, diametro, ancho, tipo, indice_carga):
        self.marca = marca
        self.diametro = diametro
        self.ancho = ancho
        self.tipo = tipo
        self.indice_carga = indice_carga

    def obtener_info(self):
        return (
            f"Marca: {self.marca}\n"
            f"Diámetro: {self.diametro} pulgadas\n"
            f"Ancho: {self.ancho} mm\n"
            f"Tipo: {self.tipo}\n"
            f"Índice de carga: {self.indice_carga}"
        )

def mostrar_llanta():
    marca = entry_marca.get()
    diametro = entry_diametro.get()
    ancho = entry_ancho.get()
    tipo = entry_tipo.get()
    indice_carga = entry_indice_carga.get()

    if not (marca and diametro and ancho and tipo and indice_carga):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
        return

    try:
        diametro = int(diametro)
        ancho = int(ancho)
        indice_carga = int(indice_carga)
    except ValueError:
        messagebox.showerror("Error de formato", "Diámetro, Ancho e Índice de carga deben ser números.")
        return

    llanta = Llanta(marca, diametro, ancho, tipo, indice_carga)
    info = llanta.obtener_info()
    messagebox.showinfo("Información de la Llanta", info)

ventana = tk.Tk()
ventana.title("Registro de Llantas")
ventana.geometry("300x300")

tk.Label(ventana, text="Marca:").pack()
entry_marca = tk.Entry(ventana)
entry_marca.pack()

tk.Label(ventana, text="Diámetro (pulgadas):").pack()
entry_diametro = tk.Entry(ventana)
entry_diametro.pack()

tk.Label(ventana, text="Ancho (mm):").pack()
entry_ancho = tk.Entry(ventana)
entry_ancho.pack()

tk.Label(ventana, text="Tipo:").pack()
entry_tipo = tk.Entry(ventana)
entry_tipo.pack()

tk.Label(ventana, text="Índice de carga:").pack()
entry_indice_carga = tk.Entry(ventana)
entry_indice_carga.pack()

tk.Button(ventana, text="Mostrar información", command=mostrar_llanta).pack(pady=10)

ventana.mainloop()
