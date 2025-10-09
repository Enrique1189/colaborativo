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

class Computadora:
    def __init__(self, marca, modelo, procesador, ram, disco, precio):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = ram
        self.disco = disco
        self.precio = precio

    def descripcion(self):
        return (
            f"--- Información de Computadora ---\n"
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Procesador: {self.procesador}\n"
            f"RAM: {self.ram}\n"
            f"Disco: {self.disco}\n"
            f"Precio: {self.precio}\n"
        )


Avion_American = Avion(
    "Personas y maletas",
    "Entre 150 y 180 personas y más de 100 kg de equipaje",
    "38 m",
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

computadoras = [
    Computadora("Dell", "Inspiron 15", "Intel i5", "8GB", "512GB SSD", 15000),
    Computadora("HP", "Pavilion", "Intel i7", "16GB", "1TB SSD", 22000),
    Computadora("Lenovo", "ThinkPad X1", "Intel i9", "32GB", "1TB SSD", 35000),
    Computadora("Apple", "MacBook Air", "M1", "8GB", "256GB SSD", 25000),
    Computadora("Asus", "ROG Strix", "Ryzen 9", "32GB", "2TB SSD", 40000)
]

def actualizar_text_area(texto):
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, texto)
    text_area.config(state="disabled")

def mostrar_avion():
    actualizar_text_area(Avion_American.mostrar_info())

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

def mostrar_info_celular(idx):
    info = celulares[idx].get_info()
    actualizar_text_area(info)

def mostrar_info_computadora(idx):
    info = computadoras[idx].descripcion()
    actualizar_text_area(info)


ventana = tk.Tk()
ventana.title("Aplicación Unificada")
ventana.geometry("900x700")
ventana.configure(bg="#2c3e50")

notebook = ttk.Notebook(ventana, padding=0)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

tab_avion = ttk.Frame(notebook, padding=0)
notebook.add(tab_avion, text="Avión")

btn_avion = ttk.Button(tab_avion, text="Mostrar Avión", command=mostrar_avion)
btn_avion.pack(pady=2, ipadx=10, ipady=4)

tab_pastel = ttk.Frame(notebook, padding=0)
notebook.add(tab_pastel, text="Pastel")

btn_pastel = ttk.Button(tab_pastel, text="Mostrar Pastel", command=mostrar_pastel)
btn_pastel.pack(pady=2, ipadx=10, ipady=4)

tab_coches = ttk.Frame(notebook, padding=0)
notebook.add(tab_coches, text="Coches")

etq_c1 = tk.Label(tab_coches, text=coche1.mostrar_info(), font=("Arial", 10))
etq_c1.pack(pady=3)
ttk.Button(tab_coches, text="Acelerar coche rojo", command=lambda: acelerar_coche(coche1, etq_c1)).pack(pady=2, ipadx=10, ipady=4)
ttk.Button(tab_coches, text="Frenar coche rojo", command=lambda: frenar_coche(coche1, etq_c1)).pack(pady=2, ipadx=10, ipady=4)

etq_c2 = tk.Label(tab_coches, text=coche2.mostrar_info(), font=("Arial", 10))
etq_c2.pack(pady=3)
ttk.Button(tab_coches, text="Acelerar coche azul", command=lambda: acelerar_coche(coche2, etq_c2)).pack(pady=2, ipadx=10, ipady=4)
ttk.Button(tab_coches, text="Frenar coche azul", command=lambda: frenar_coche(coche2, etq_c2)).pack(pady=2, ipadx=10, ipady=4)

tab_celulares = ttk.Frame(notebook, padding=0)
notebook.add(tab_celulares, text="Celulares")

lbl_instr = tk.Label(tab_celulares, text="Selecciona un celular para ver su información:", font=("Arial", 10))
lbl_instr.pack(pady=3)
for i, cel in enumerate(celulares):
    ttk.Button(tab_celulares, text=cel.marca, command=lambda i=i: mostrar_info_celular(i)).pack(pady=2, ipadx=10, ipady=4, fill="x")

tab_computadoras = ttk.Frame(notebook, padding=0)
notebook.add(tab_computadoras, text="Computadoras")

lbl_inst_comp = tk.Label(tab_computadoras, text="Selecciona una computadora:", font=("Arial", 10), pady=3)
lbl_inst_comp.pack()
for i, comp in enumerate(computadoras):
    ttk.Button(tab_computadoras, text=f"{comp.marca} {comp.modelo}", command=lambda i=i: mostrar_info_computadora(i)).pack(pady=2, ipadx=10, ipady=4, fill="x")

frame_text = ttk.Frame(ventana, padding=0)
frame_text.pack(fill="both", expand=True, padx=10, pady=10)

text_area = tk.Text(frame_text, wrap="word", font=("Consolas", 12))
text_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_text, command=text_area.yview)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)

text_area.insert("1.0", "Selecciona una opción en las pestañas para mostrar información.")
text_area.config(state="disabled")

ventana.mainloop()
