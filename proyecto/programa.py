#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s
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

class Gato:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("GATO")
        self.ventana.geometry("500x600")

        self.crear_caracteristicas()

        btn_guardar = tk.Button(self.ventana, text="Guardar", command=self.guardar_datos, bg="green", fg="white")
        btn_guardar.pack(pady=10)

        btn_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_datos, bg="blue", fg="white")
        btn_mostrar.pack(pady=5)

        self.resultado = tk.Label(self.ventana, text="", font=("Arial", 10), justify="left")
        self.resultado.pack(pady=10)

        self.ventana.mainloop()

    def crear_caracteristicas(self):
        self.entradas = {}

        campos = ["Nombre", "Color", "Edad", "Raza", "Sonido"]
        for campo in campos:
            tk.Label(self.ventana, text=f"{campo}:", font=("Arial", 11)).pack()
            entrada = tk.Entry(self.ventana)
            entrada.pack()
            self.entradas[campo.lower()] = entrada  

    def guardar_datos(self):
        self.nombre = self.entradas["nombre"].get()
        self.color = self.entradas["color"].get()
        self.edad = self.entradas["edad"].get()
        self.raza = self.entradas["raza"].get()
        self.sonido = self.entradas["sonido"].get()

    def mostrar_datos(self):
        texto = (
            f"Nombre: {self.nombre}\n"
            f"Color: {self.color}\n"
            f"Edad: {self.edad} años\n"
            f"Raza: {self.raza}\n"
            f"Sonido: {self.sonido}"
        )
        self.resultado.config(text=texto)

class Aguila:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("ÁGUILA")
        self.ventana.geometry("500x600")

        self.crear_caracteristicas()

        btn_guardar = tk.Button(self.ventana, text="Guardar", command=self.guardar_datos, bg="green", fg="white")
        btn_guardar.pack(pady=10)

        btn_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_datos, bg="blue", fg="white")
        btn_mostrar.pack(pady=5)

        self.resultado = tk.Label(self.ventana, text="", font=("Arial", 10), justify="left")
        self.resultado.pack(pady=10)

        self.ventana.mainloop()

    def crear_caracteristicas(self):
        self.entradas = {}

        campos = ["Nombre", "Color de Plumaje", "Edad", "Envergadura", "Sonido"]
        for campo in campos:
            tk.Label(self.ventana, text=f"{campo}:", font=("Arial", 11)).pack()
            entrada = tk.Entry(self.ventana)
            entrada.pack()
            self.entradas[campo.lower().replace(" ", "_")] = entrada  

    def guardar_datos(self):
        self.nombre = self.entradas["nombre"].get()
        self.color_plumaje = self.entradas["color_de_plumaje"].get()
        self.edad = self.entradas["edad"].get()
        self.envergadura = self.entradas["envergadura"].get()
        self.sonido = self.entradas["sonido"].get()

    def mostrar_datos(self):
        texto = (
            f"Nombre: {self.nombre}\n"
            f"Color de Plumaje: {self.color_plumaje}\n"
            f"Edad: {self.edad} años\n"
            f"Envergadura: {self.envergadura} metros\n"
            f"Sonido: {self.sonido}"
        )
        self.resultado.config(text=texto)
class Leon:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("LEÓN")
        self.ventana.geometry("500x600")

        self.crear_caracteristicas()

        btn_guardar = tk.Button(self.ventana, text="Guardar", command=self.guardar_datos, bg="green", fg="white")
        btn_guardar.pack(pady=10)

        btn_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_datos, bg="blue", fg="white")
        btn_mostrar.pack(pady=5)

        self.resultado = tk.Label(self.ventana, text="", font=("Arial", 10), justify="left")
        self.resultado.pack(pady=10)

        self.ventana.mainloop()

    def crear_caracteristicas(self):
        self.entradas = {}

        campos = ["Nombre", "Color de Pelaje", "Edad", "Tamaño", "Rugido"]
        for campo in campos:
            tk.Label(self.ventana, text=f"{campo}:", font=("Arial", 11)).pack()
            entrada = tk.Entry(self.ventana)
            entrada.pack()
            self.entradas[campo.lower().replace(" ", "_")] = entrada  

    def guardar_datos(self):
        self.nombre = self.entradas["nombre"].get()
        self.color_pelaje = self.entradas["color_de_pelaje"].get()
        self.edad = self.entradas["edad"].get()
        self.tamaño = self.entradas["tamaño"].get()
        self.rugido = self.entradas["rugido"].get()

    def mostrar_datos(self):
        texto = (
            f"Nombre: {self.nombre}\n"
            f"Color de Pelaje: {self.color_pelaje}\n"
            f"Edad: {self.edad} años\n"
            f"Tamaño: {self.tamaño}\n"
            f"Rugido: {self.rugido}"
        )
        self.resultado.config(text=texto)

class Tigre:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("TIGRE")
        self.ventana.geometry("500x600")

        self.crear_caracteristicas()

        btn_guardar = tk.Button(self.ventana, text="Guardar", command=self.guardar_datos, bg="green", fg="white")
        btn_guardar.pack(pady=10)

        btn_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_datos, bg="blue", fg="white")
        btn_mostrar.pack(pady=5)

        self.resultado = tk.Label(self.ventana, text="", font=("Arial", 10), justify="left")
        self.resultado.pack(pady=10)

        self.ventana.mainloop()

    def crear_caracteristicas(self):
        self.entradas = {}

        campos = ["Nombre", "Color de Pelaje", "Edad", "Tamaño", "Rugido"]
        for campo in campos:
            tk.Label(self.ventana, text=f"{campo}:", font=("Arial", 11)).pack()
            entrada = tk.Entry(self.ventana)
            entrada.pack()
            self.entradas[campo.lower().replace(" ", "_")] = entrada  

    def guardar_datos(self):
        self.nombre = self.entradas["nombre"].get()
        self.color_pelaje = self.entradas["color_de_pelaje"].get()
        self.edad = self.entradas["edad"].get()
        self.tamaño = self.entradas["tamaño"].get()
        self.rugido = self.entradas["rugido"].get()

    def mostrar_datos(self):
        texto = (
            f"Nombre: {self.nombre}\n"
            f"Color de Pelaje: {self.color_pelaje}\n"
            f"Edad: {self.edad} años\n"
            f"Tamaño: {self.tamaño}\n"
            f"Rugido: {self.rugido}"
        )
        self.resultado.config(text=texto)
