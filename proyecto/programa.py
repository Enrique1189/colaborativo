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


Avion_American_Airlines = Avion(
    "Personas y maletas",
    "Entre 150 y 180 personas y más de 100 kg de equipaje",
    "Su tamaño ronda los 38m",
    "Airbus A320",
    "En su mayoría blancos con azul"
)

Avion_United_Airlines = Avion(
    "Personas y maletas",
    "Entre 150 y 180 personas y más de 100 kg de equipaje",
    "Longitud aprox. 39.5m, envergadura 35.8m, altura de cola 12.5m",
    "Boeing 737",
    "En su mayoría blancos con azul"
)


root = tk.Tk()
root.title("Información de Aviones")
root.geometry("500x400")
root.configure(bg="#2c3e50") 


title_label = tk.Label(
    root, text="Aviones", 
    font=("Helvetica", 20, "bold"), fg="white", bg="#2c3e50"
)
title_label.pack(pady=15)


button_frame = tk.Frame(root, bg="#34495e")
button_frame.pack(pady=10, fill="x", padx=20)


style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Arial", 12), padding=10, foreground="#34495e")
style.map("TButton",
    foreground=[('active', '#2980b9')],
    background=[('active', '#ecf0f1')]
)


text_frame = tk.Frame(root)
text_frame.pack(pady=20, padx=20, fill="both", expand=True)

text_area = tk.Text(
    text_frame, wrap="word", font=("Consolas", 12), bg="#ecf0f1", fg="#2c3e50", relief="flat", bd=2
)
text_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(text_frame, command=text_area.yview)
scrollbar.pack(side="right", fill="y")

text_area.config(yscrollcommand=scrollbar.set)
text_area.insert("1.0", "Selecciona un avión para mostrar su información.")
text_area.config(state="disabled")

def mostrar_avion(avion):
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, avion.mostrar_info())
    text_area.config(state="disabled")


btn_american = ttk.Button(button_frame, text="Avión American Airlines", command=lambda: mostrar_avion(Avion_American_Airlines))
btn_american.pack(side="left", expand=True, padx=10)

btn_united = ttk.Button(button_frame, text="Avión United Airlines", command=lambda: mostrar_avion(Avion_United_Airlines))
btn_united.pack(side="left", expand=True, padx=10)

root.mainloop()
