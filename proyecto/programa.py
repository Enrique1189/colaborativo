import tkinter as tk
from tkinter import messagebox

class AnimalGUI:
    def __init__(self, titulo, campos, sonido_label):
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        self.ventana.geometry("500x600")

        self.campos = campos
        self.sonido_label = sonido_label

        self.crear_caracteristicas()

        btn_guardar = tk.Button(self.ventana, text="Guardar", command=self.guardar_datos, bg="green", fg="white")
        btn_guardar.pack(pady=10)

        btn_mostrar = tk.Button(self.ventana, text="Mostrar", command=self.mostrar_datos, bg="blue", fg="white")
        btn_mostrar.pack(pady=5)

        self.resultado = tk.Label(self.ventana, text="", font=("Arial", 10), justify="left")
        self.resultado.pack(pady=10)

    def crear_caracteristicas(self):
        self.entradas = {}
        for campo in self.campos:
            tk.Label(self.ventana, text=f"{campo}:", font=("Arial", 11)).pack()
            entrada = tk.Entry(self.ventana)
            entrada.pack()
            self.entradas[campo.lower().replace(" ", "_")] = entrada

    def guardar_datos(self):
        for campo in self.entradas:
            setattr(self, campo, self.entradas[campo].get())

    def mostrar_datos(self):
        texto = ""
        for campo in self.campos:
            clave = campo.lower().replace(" ", "_")
            valor = getattr(self, clave, "")
            if campo.lower() == self.sonido_label.lower():
                texto += f"{campo}: {valor}\n"
            elif "edad" in campo.lower():
                texto += f"{campo}: {valor} años\n"
            elif "velocidad" in campo.lower():
                texto += f"{campo}: {valor} km/h\n"
            else:
                texto += f"{campo}: {valor}\n"
        self.resultado.config(text=texto)

class Gato(AnimalGUI):
    def __init__(self):
        super().__init__("GATO", ["Nombre", "Color", "Edad", "Raza", "Sonido"], "Sonido")

class Aguila(AnimalGUI):
    def __init__(self):
        super().__init__("ÁGUILA", ["Nombre", "Color de Plumaje", "Edad", "Envergadura", "Sonido"], "Sonido")

class Leon(AnimalGUI):
    def __init__(self):
        super().__init__("LEÓN", ["Nombre", "Color de Pelaje", "Edad", "Tamaño", "Rugido"], "Rugido")

class Tigre(AnimalGUI):
    def __init__(self):
        super().__init__("TIGRE", ["Nombre", "Color de Pelaje", "Edad", "Tamaño", "Rugido"], "Rugido")

class Lobo(AnimalGUI):
    def __init__(self):
        super().__init__("LOBO", ["Nombre", "Edad", "Color de Pelaje", "Tamaño", "Velocidad", "Aullido"], "Aullido")

def menu_principal():
    root = tk.Tk()
    root.title("Menú de Animales")
    root.geometry("300x450")

    tk.Label(root, text="Selecciona un animal:", font=("Arial", 14)).pack(pady=20)

    botones = [
        ("Gato", Gato),
        ("Águila", Aguila),
        ("León", Leon),
        ("Tigre", Tigre),
        ("Lobo", Lobo)
    ]

    for texto, clase in botones:
        tk.Button(root, text=texto, width=20, command=clase).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    menu_principal()
