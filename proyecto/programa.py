#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
<<<<<<< HEAD
#Debera generar su rama por equipo.
import tkinter as tk
from tkinter import ttk, scrolledtext

from clases.gato import Gato
from clases.hamster import Hamster
from clases.pajaro import Pajaro
from clases.perro import Perro
from clases.ratita import Ratita

def mostrar_info():
    salida.delete("1.0", tk.END)

    gato = Gato("Misu", 3, 4.5, False, "vómito y letárgico")
    hamster = Hamster("Chispa", "Sirio", 0.2, 10, "activo")
    pajaro = Pajaro("Piolín", "Canario", 0.03, 12, "pico roto")
    perro = Perro("Max", "Labrador", 20, 55, "no come")
    ratita = Ratita("Rati", 140, 6, "estornudo y moco", "baja")

    salida.insert(tk.END, f"Gato: {gato.nombre}\n")
    for e in gato.evaluar_salud():
        salida.insert(tk.END, f"- {e}\n")
    salida.insert(tk.END, "\n")

    salida.insert(tk.END, f"Hamster: {hamster.nombre}\n")
    salida.insert(tk.END, f"- Raza: {hamster.raza}\n")
    salida.insert(tk.END, f"- Peso: {hamster.peso} kg\n")
    salida.insert(tk.END, f"- Altura: {hamster.altura} cm\n")
    salida.insert(tk.END, f"- Síntomas: {hamster.sintomas}\n\n")

    salida.insert(tk.END, f"Pájaro: {pajaro.nombre}\n")
    salida.insert(tk.END, f"- Tipo: {pajaro.tipo}\n")
    salida.insert(tk.END, f"- Peso: {pajaro.peso} kg\n")
    salida.insert(tk.END, f"- Altura: {pajaro.altura} cm\n")
    salida.insert(tk.END, f"- Síntomas: {pajaro.sintomas}\n\n")

    salida.insert(tk.END, f"Perro: {perro.nombre}\n")
    salida.insert(tk.END, f"- Raza: {perro.raza}\n")
    salida.insert(tk.END, f"- Peso: {perro.peso} kg\n")
    salida.insert(tk.END, f"- Altura: {perro.altura} cm\n")
    salida.insert(tk.END, f"- Síntomas: {perro.sintomas}\n\n")

    salida.insert(tk.END, f"Ratita: {ratita.nombre}\n")
    salida.insert(tk.END, f"- Peso: {ratita.peso} gramos\n")
    salida.insert(tk.END, f"- Edad: {ratita.edad} meses\n")
    salida.insert(tk.END, f"- Síntomas: {ratita.sintomas}\n")
    salida.insert(tk.END, f"- Actividad: {ratita.actividad}\n")
    for r in ratita.evaluar_salud():
        salida.insert(tk.END, f"- {r}\n")

root = tk.Tk()
root.title("Evaluación de Salud de Mascotas")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

boton = ttk.Button(frame, text="Mostrar Evaluación", command=mostrar_info)
boton.grid(row=0, column=0, pady=5)

salida = scrolledtext.ScrolledText(frame, width=60, height=25)
salida.grid(row=1, column=0)

root.mainloop()
=======
#Debera generar su rama por equipo.s
>>>>>>> 5334bddad523baac1eb4babaee07dfd29af54742
