#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s
# app.py
import tkinter as tk
from tkinter import messagebox

class Lobo:
    def __init__(self, nombre, edad, color_pelaje, tamaño, velocidad):
        self.nombre = nombre
        self.edad = edad
        self.color_pelaje = color_pelaje
        self.tamaño = tamaño
        self.velocidad = velocidad

    def aullar(self):
        return f"{self.nombre} aúlla fuertemente: ¡Auuuuu!"

    def describir(self):
        return (f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad} años\n"
                f"Color de pelaje: {self.color_pelaje}\n"
                f"Tamaño: {self.tamaño}\n"
                f"Velocidad: {self.velocidad} km/h")

lobo = Lobo("Akela", 7, "Gris oscuro", "Grande", 60.5)

def mostrar_info():
    texto_resultado.set(lobo.describir())

def aullar():
    messagebox.showinfo("Aullido", lobo.aullar())

ventana = tk.Tk()
ventana.title("Información del Lobo")
ventana.geometry("400x300")

tk.Label(ventana, text="Lobo predefinido", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(ventana, text="Mostrar Información", command=mostrar_info).pack(pady=5)
tk.Button(ventana, text="Aullar", command=aullar).pack(pady=5)

texto_resultado = tk.StringVar()
tk.Label(ventana, textvariable=texto_resultado, justify="left", wraplength=350).pack(pady=10)

ventana.mainloop()

