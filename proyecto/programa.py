#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s

import tkinter as tk
from tkinter import ttk


class Avion:
    def __init__(self, cargamento, capacidad, tamaño, modelo, color):
        self.cargamento = cargamento
        self.capacidad = capacidad
        self.tamaño = tamaño
        self.modelo = modelo
        self.color = color
    
    def mostrar_info(self):
        return (
            f"--- Información de avión ---\n"
            f"Cargamento: {self.cargamento}\n"
            f"Capacidad: {self.capacidad}\n"
            f"Tamaño: {self.tamaño}\n"
            f"Modelo: {self.modelo}\n"
            f"Color: {self.color}\n"
        )


class Pastel:
    def __init__(self, tamaño, sabor, decoración, capas, tipo_glaseado, color):
        self.tamaño = tamaño
        self.sabor = sabor
        self.decoración = decoración
        self.capas = capas
        self.tipo_glaseado = tipo_glaseado
        self.color = color
    
    def mostrar_info(self):
        return (
            f"--- Información del Pastel ---\n"
            f"Tamaño: {self.tamaño}\n"
            f"Sabor: {self.sabor}\n"
            f"Decoración: {self.decoración}\n"
            f"Capas: {self.capas}\n"
            f"Tipo de glaseado: {self.tipo_glaseado}\n"
            f"Color: {self.color}\n"
        )


class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} | Color: {self.color} | Velocidad: {self.velocidad} km/h"


def mostrar_avion(avion):
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, avion.mostrar_info())
    text_area.config(state="disabled")


def mostrar_pastel_especifico():
    pastel_especial = Pastel(
        tamaño="Mediano",
        sabor="Chocolate",
        decoración="Frutas",
        capas=3,
        tipo_glaseado="Vainilla",
        color="Café"
    )
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, pastel_especial.mostrar_info())
    text_area.config(state="disabled")


def mostrar_info_coche(coche, etiqueta):
    etiqueta.config(text=coche.mostrar_info())


def acelerar_coche(coche, etiqueta):
    coche.acelerar(10)
    mostrar_info_coche(coche, etiqueta)


def frenar_coche(coche, etiqueta):
    coche.frenar(10)
    mostrar_info_coche(coche, etiqueta)


Avion_American_Airlines = Avion(
    "Personas y maletas",
    "Entre 150 y 180 personas y más de 100 kg de equipaje",
    "Su tamaño ronda los 38m",
    "Airbus A320",
    "En su mayoría blancos con azul"
)

mi_coche_rojo = Coche("Lamborghini", "Huracán", "Rojo")
coche_amigo = Coche("Honda", "Civic", "Azul")

ventana = tk.Tk()
ventana.title("Avión, Pastel y Coches")
ventana.geometry("900x700")
ventana.configure(bg="#2c3e50")

frame_aviones = tk.Frame(ventana, bg="#34495e", padx=20, pady=10)
frame_aviones.pack(fill="x", padx=10, pady=10)

tk.Label(
    frame_aviones, text="Información del Avión",
    font=("Helvetica", 16, "bold"), fg="white", bg="#34495e"
).pack(pady=5)

ttk.Button(
    frame_aviones, text="Mostrar Avión",
    command=lambda: mostrar_avion(Avion_American_Airlines)
).pack(pady=10)

frame_pasteles = tk.Frame(ventana, bg="#34495e", padx=20, pady=10)
frame_pasteles.pack(fill="x", padx=10, pady=10)

tk.Label(
    frame_pasteles, text="Mostrar Pastel Específico",
    font=("Helvetica", 16, "bold"), fg="white", bg="#34495e"
).pack(pady=5)

tk.Button(frame_pasteles, text="Ver Pastel", command=mostrar_pastel_especifico).pack(pady=10)

frame_coches = tk.Frame(ventana, bg="#34495e", padx=20, pady=10)
frame_coches.pack(fill="x", padx=10, pady=10)

tk.Label(
    frame_coches, text="Coches",
    font=("Helvetica", 16, "bold"), fg="white", bg="#34495e"
).pack(pady=5)

etiqueta1 = tk.Label(frame_coches, text=mi_coche_rojo.mostrar_info(), font=("Arial", 10), bg="#34495e", fg="white")
etiqueta1.pack(pady=5)

tk.Button(frame_coches, text="Acelerar coche rojo", command=lambda: acelerar_coche(mi_coche_rojo, etiqueta1)).pack()
tk.Button(frame_coches, text="Frenar coche rojo", command=lambda: frenar_coche(mi_coche_rojo, etiqueta1)).pack()

etiqueta2 = tk.Label(frame_coches, text=coche_amigo.mostrar_info(), font=("Arial", 10), bg="#34495e", fg="white")
etiqueta2.pack(pady=5)

tk.Button(frame_coches, text="Acelerar coche azul", command=lambda: acelerar_coche(coche_amigo, etiqueta2)).pack()
tk.Button(frame_coches, text="Frenar coche azul", command=lambda: frenar_coche(coche_amigo, etiqueta2)).pack()

text_frame = tk.Frame(ventana)
text_frame.pack(pady=20, padx=20, fill="both", expand=True)

text_area = tk.Text(
    text_frame, wrap="word", font=("Consolas", 12),
    bg="#ecf0f1", fg="#2c3e50", relief="flat", bd=2
)
text_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(text_frame, command=text_area.yview)
scrollbar.pack(side="right", fill="y")

text_area.config(yscrollcommand=scrollbar.set)
text_area.insert("1.0", "Da clic en un botón para mostrar información.")
text_area.config(state="disabled")

ventana.mainloop()
