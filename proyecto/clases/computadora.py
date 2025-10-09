##Clase ejemplo a desarrollar

import tkinter as tk

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
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Procesador: {self.procesador}\n"
            f"RAM: {self.ram}\n"
            f"Disco: {self.disco}\n"
            f"Precio: ${self.precio}"
        )

computadoras = [
    Computadora("Dell", "Inspiron 15", "Intel i5", "8GB", "512GB SSD", 15000),
    Computadora("HP", "Pavilion", "Intel i7", "16GB", "1TB SSD", 22000),
    Computadora("Lenovo", "ThinkPad X1", "Intel i9", "32GB", "1TB SSD", 35000),
    Computadora("Apple", "MacBook Air", "M1", "8GB", "256GB SSD", 25000),
    Computadora("Asus", "ROG Strix", "Ryzen 9", "32GB", "2TB SSD", 40000)
]

ventana = tk.Tk()
ventana.title("Catálogo de Computadoras")
ventana.geometry("400x350")

etiqueta = tk.Label(ventana, text="Presiona un botón para ver los detalles:", font=("Arial", 12))
etiqueta.pack(pady=10)

detalles = tk.Label(ventana, text="", font=("Arial", 10), justify="left")
detalles.pack(pady=10)

def mostrar_detalles(computadora):
    detalles.config(text=computadora.descripcion())

for c in computadoras:
    boton = tk.Button(ventana, text=f"{c.marca} {c.modelo}",
                      command=lambda comp=c: mostrar_detalles(comp))
    boton.pack(pady=5, fill="x")

ventana.mainloop()
