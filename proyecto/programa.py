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

class Celular:
    def __init__(self, marca, costo, vida):
        self.marca = marca
        self.costo = costo 
        self.tiempo_vida = vida

    def get_info(self):
        return f"--- Información de Celular ---\nMarca: {self.marca}\nCosto: {self.costo}\nVida útil: {self.tiempo_vida}"


Avion_American = Avion(
    "Personas y maletas",
    "Entre 150 y 180 personas y más de 100 kg de equipaje",
    "38m",
    "Airbus A320",
    "Blanco con azul"
)

pastel_especial = Pastel("Mediano", "Chocolate", "Frutas", 3, "Vainilla", "Café")

coche1 = Coche("Lamborghini", "Huracán", "Rojo")
coche2 = Coche("Honda", "Civic", "Azul")

celulares = [
    Celular("sansung_galaxy", "1500 pesos", "20 años"),
    Celular("oppo", "20 dólares", "1 año"),
    Celular("wawey", "1 peso boliviano XD", "1 microsegundo"),
    Celular("nokia", "5 pesos", "durará más que tú XD"),
    Celular("ipone", "10,000,000 de pesos", "cuando lo saques de la caja")
]


def mostrar_avion(avion):
    actualizar_text_area(avion.mostrar_info())

def mostrar_pastel():
    actualizar_text_area(pastel_especial.mostrar_info())

def mostrar_info_coche(coche, etiqueta):
    etiqueta.config(text=coche.mostrar_info())

def acelerar_coche(coche, etiqueta):
    coche.acelerar(10)
    mostrar_info_coche(coche, etiqueta)

def frenar_coche(coche, etiqueta):
    coche.frenar(10)
    mostrar_info_coche(coche, etiqueta)

def mostrar_info_celular(index):
    info = celulares[index].get_info()
    actualizar_text_area(info)

def actualizar_text_area(texto):
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, texto)
    text_area.config(state="disabled")


ventana = tk.Tk()
ventana.title("Información Unificada")
ventana.geometry("900x800")
ventana.configure(bg="#2c3e50")

frame_avion = tk.LabelFrame(ventana, text="Avión", fg="white", bg="#34495e", font=("Helvetica", 14, "bold"))
frame_avion.pack(fill="x", padx=10, pady=10)

ttk.Button(frame_avion, text="Mostrar Avión", command=lambda: mostrar_avion(Avion_American)).pack(pady=10)

frame_pastel = tk.LabelFrame(ventana, text="Pastel", fg="white", bg="#34495e", font=("Helvetica", 14, "bold"))
frame_pastel.pack(fill="x", padx=10, pady=10)

ttk.Button(frame_pastel, text="Mostrar Pastel Especial", command=mostrar_pastel).pack(pady=10)

frame_coches = tk.LabelFrame(ventana, text="Coches", fg="white", bg="#34495e", font=("Helvetica", 14, "bold"))
frame_coches.pack(fill="x", padx=10, pady=10)

etiqueta1 = tk.Label(frame_coches, text=coche1.mostrar_info(), font=("Arial", 10), bg="#34495e", fg="white")
etiqueta1.pack(pady=5)

ttk.Button(frame_coches, text="Acelerar coche rojo", command=lambda: acelerar_coche(coche1, etiqueta1)).pack()
ttk.Button(frame_coches, text="Frenar coche rojo", command=lambda: frenar_coche(coche1, etiqueta1)).pack()

etiqueta2 = tk.Label(frame_coches, text=coche2.mostrar_info(), font=("Arial", 10), bg="#34495e", fg="white")
etiqueta2.pack(pady=5)

ttk.Button(frame_coches, text="Acelerar coche azul", command=lambda: acelerar_coche(coche2, etiqueta2)).pack()
ttk.Button(frame_coches, text="Frenar coche azul", command=lambda: frenar_coche(coche2, etiqueta2)).pack()

frame_celulares = tk.LabelFrame(ventana, text="Celulares", fg="white", bg="#34495e", font=("Helvetica", 14, "bold"))
frame_celulares.pack(fill="x", padx=10, pady=10)

for i, cel in enumerate(celulares):
    ttk.Button(frame_celulares, text=cel.marca, command=lambda i=i: mostrar_info_celular(i)).pack(pady=5)

text_frame = tk.Frame(ventana)
text_frame.pack(pady=20, padx=20, fill="both", expand=True)

text_area = tk.Text(text_frame, wrap="word", font=("Consolas", 12), bg="#ecf0f1", fg="#2c3e50")
text_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(text_frame, command=text_area.yview)
scrollbar.pack(side="right", fill="y")

text_area.config(yscrollcommand=scrollbar.set)
text_area.insert("1.0", "Haz clic en un botón para mostrar información.")
text_area.config(state="disabled")

ventana.mainloop()
