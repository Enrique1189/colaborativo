import tkinter as tk
from tkinter import messagebox

# Clase BarquitoDeJuguete
class BarquitoDeJuguete:
    def __init__(self, color, marca, modelo, tamaño, flota_en_agua):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño
        self.flota_en_agua = flota_en_agua

    def encender(self):
        return f"El barquito de juguete {self.modelo} está encendido y listo para navegar."

    def apagar(self):
        return f"El barquito de juguete {self.modelo} ha sido apagado."

    def __str__(self):
        flota = "sí" if self.flota_en_agua else "no"
        return (f"Barquito de Juguete - Modelo: {self.modelo}, Marca: {self.marca}, Color: {self.color}, "
                f"Tamaño: {self.tamaño}, Flota en agua: {flota}")

# Clase LegoDeJuguete
class LegoDeJuguete:
    def __init__(self, color, marca, num_piezas, tema, es_compatible_con_otros_sets):
        self.color = color
        self.marca = marca
        self.num_piezas = num_piezas
        self.tema = tema
        self.es_compatible_con_otros_sets = es_compatible_con_otros_sets

    def armar(self):
        return f"El set de Lego {self.tema} está siendo armado. ¡Cuidado con las piezas!"

    def desarmar(self):
        return f"El set de Lego {self.tema} ha sido desarmado."

    def __str__(self):
        compatible = "sí" if self.es_compatible_con_otros_sets else "no"
        return (f"Lego de Juguete - Tema: {self.tema}, Marca: {self.marca}, Color: {self.color}, "
                f"Número de piezas: {self.num_piezas}, Compatible con otros sets: {compatible}")

# Clase OsoDePeluche
class OsoDePeluche:
    def __init__(self, color, tamaño, marca, material, es_trasladable):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.es_trasladable = es_trasladable

    def abrazar(self):
        return f"¡Abraza al adorable oso de peluche de {self.color} y {self.tamaño} tamaño!"

    def lavar(self):
        return f"El oso de peluche {self.marca} ha sido lavado con cuidado."

    def __str__(self):
        trasladable = "sí" if self.es_trasladable else "no"
        return (f"Oso de Peluche - Marca: {self.marca}, Color: {self.color}, Tamaño: {self.tamaño}, "
                f"Material: {self.material}, Trasladable: {trasladable}")

# Clase CarroDeJuguete
class CarroDeJuguete:
    def __init__(self, color, marca, modelo, tamaño, tiene_control_remoto):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño
        self.tiene_control_remoto = tiene_control_remoto

    def encender(self):
        return f"El carro de juguete {self.modelo} está encendido."

    def apagar(self):
        return f"El carro de juguete {self.modelo} está apagado."

    def __str__(self):
        control = "sí" if self.tiene_control_remoto else "no"
        return (f"Carro de Juguete - Modelo: {self.modelo}, Marca: {self.marca}, Color: {self.color}, "
                f"Tamaño: {self.tamaño}, Control remoto: {control}")

# Clase Avioncito
class Avioncito:
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad

    def despegar(self):
        return f"El avión {self.modelo} está despegando."

    def aterrizar(self):
        return f"El avión {self.modelo} está aterrizando."

    def __str__(self):
        return f"Avión Modelo: {self.modelo}, Capacidad: {self.capacidad} pasajeros"

# Función para mostrar información del juguete seleccionado
def mostrar_informacion(juguete):
    messagebox.showinfo("Información del Juguete", str(juguete))

# Función para realizar la acción del juguete
def realizar_accion(juguete, accion):
    if accion == "encender":
        messagebox.showinfo("Acción", juguete.encender())
    elif accion == "apagar":
        messagebox.showinfo("Acción", juguete.apagar())
    elif accion == "abrazar":
        messagebox.showinfo("Acción", juguete.abrazar())
    elif accion == "lavar":
        messagebox.showinfo("Acción", juguete.lavar())
    elif accion == "armar":
        messagebox.showinfo("Acción", juguete.armar())
    elif accion == "desarmar":
        messagebox.showinfo("Acción", juguete.desarmar())
    elif accion == "despegar":
        messagebox.showinfo("Acción", juguete.despegar())
    elif accion == "aterrizar":
        messagebox.showinfo("Acción", juguete.aterrizar())

# Creando la ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Tienda de Juguetes")
ventana.geometry("500x600")

# Creando los juguetes
barco = BarquitoDeJuguete("azul", "PlayFun", "NautilusX", "mediano", True)
lego = LegoDeJuguete("rojo", "LEGO", 500, "Espacio", True)
oso = OsoDePeluche("marrón", "grande", "TeddyBear", "algodón", True)
carro = CarroDeJuguete("rojo", "HotWheels", "SpeedsterX", "pequeño", True)
avion = Avioncito("JetX1000", 200)

# Creando botones para cada juguete
boton_barco = tk.Button(ventana, text="Ver Barquito de Juguete", command=lambda: mostrar_informacion(barco))
boton_barco.pack(pady=10)

boton_lego = tk.Button(ventana, text="Ver Lego de Juguete", command=lambda: mostrar_informacion(lego))
boton_lego.pack(pady=10)

boton_oso = tk.Button(ventana, text="Ver Oso de Peluche", command=lambda: mostrar_informacion(oso))
boton_oso.pack(pady=10)

boton_carro = tk.Button(ventana, text="Ver Carro de Juguete", command=lambda: mostrar_informacion(carro))
boton_carro.pack(pady=10)

boton_avion = tk.Button(ventana, text="Ver Avioncito", command=lambda: mostrar_informacion(avion))
boton_avion.pack(pady=10)

# Añadiendo botones para realizar acciones con cada juguete
boton_encender_barco = tk.Button(ventana, text="Encender Barquito", command=lambda: realizar_accion(barco, "encender"))
boton_encender_barco.pack(pady=5)

boton_encender_carro = tk.Button(ventana, text="Encender Carro", command=lambda: realizar_accion(carro, "encender"))
boton_encender_carro.pack(pady=5)

boton_despegar_avion = tk.Button(ventana, text="Despegar Avión", command=lambda: realizar_accion(avion, "despegar"))
boton_despegar_avion.pack(pady=5)

# Iniciar la interfaz gráfica
ventana.mainloop()
