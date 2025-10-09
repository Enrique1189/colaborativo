##Clase ejemplo a desarrollar
import tkinter as tk

class Celular:
    def __init__(self, marca, costo, vida):
        self.marca = marca
        self.costo = costo 
        self.tiempo_vida = vida
    def get_info(self):
        return f"Marca: {self.marca}\nCosto: {self.costo}\nTiempo de vida útil: {self.tiempo_vida}"

cel1 = Celular("sansung_galaxy", "1500 pesos", "20 años")
cel2 = Celular("oppo", "20 dolares", "1 año")
cel3 = Celular("wawey", "1 peso boliviano XD", "1 microsegundo")
cel4 = Celular("nokia", "5 pesos", "durara mas que tu XD")
cel5 = Celular("ipone", "10,000     ,000 de pesos", "cuando lo saques de la caja")

celulares = [cel1, cel2, cel3, cel4, cel5]

root = tk.Tk()
root.title("Información de Celulares")

label_info = tk.Label(root, text="Selecciona un celular para ver su información", font=("Arial", 12), justify="left")
label_info.pack(pady=10)

def mostrar_info(index):
    info = celulares[index].get_info()
    label_info.config(text=info)

for i, cel in enumerate(celulares):
    btn = tk.Button(root, text=cel.marca, command=lambda i=i: mostrar_info(i))
    btn.pack(pady=5)

root.mainloop()


