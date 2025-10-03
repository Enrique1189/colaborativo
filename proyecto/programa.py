#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s
import tkinter as tk

class Taco:
    def __init__(self, tipo, salsa, tamaño, tortilla, picante):
        self.tipo = tipo
        self.salsa = salsa
        self.tamaño = tamaño
        self.tortilla = tortilla
        self.picante = picante
        self.ingredientes = [tipo]

    def mostrar_info(self):
        info = f"""
        ------ INFORMACIÓN DEL TACO ------
        Tipo: {self.tipo}
        Salsa: {self.salsa}
        Tamaño: {self.tamaño}
        Tortilla: {self.tortilla}
        Picante: {"Sí" if self.picante else "No"}
        Ingredientes: {", ".join(self.ingredientes)}
        ----------------------------------
        """
        return info

ventana = tk.Tk()
ventana.title("Taco App")
ventana.geometry("400x400")
ventana.configure(bg="#FFF5E1")

mi_taco = Taco("pastor", "verde", "normal", "maíz", True)
resultado = tk.StringVar()

def mostrar_taco():
    resultado.set(mi_taco.mostrar_info())

boton_taco = tk.Button(
    ventana,
    text="Tacos",
    command=mostrar_taco,
    font=("Arial", 10),
    bg="#FADADD",
    activebackground="#F8C8DC",
    width=10,
    height=1
)
boton_taco.place(relx=0.5, rely=0.3, anchor="center")

tk.Label(
    ventana,
    textvariable=resultado,
    bg="#FFF5E1",
    justify="left",
    font=("Courier", 10)
).place(relx=0.5, rely=0.6, anchor="center")

ventana.mainloop()
