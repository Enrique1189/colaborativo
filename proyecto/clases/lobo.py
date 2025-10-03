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
        return (
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Color de pelaje: {self.color_pelaje}\n"
            f"Tamaño: {self.tamaño}\n"
            f"Velocidad: {self.velocidad} km/h"
        )
