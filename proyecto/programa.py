#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s
import tkinter as tk

class Gato:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title(" GATO")
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


gato = Gato()
