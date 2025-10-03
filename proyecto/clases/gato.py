
class Gato:
    def __init__(self, nombre, edad, color, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.raza = raza
        self.peso = peso

    def __str__(self):
        return (
            f"🐱 Información del Gato:\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Color: {self.color}\n"
            f"Raza: {self.raza}\n"
            f"Peso: {self.peso} kg"
        )
