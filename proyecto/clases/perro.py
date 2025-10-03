class Perro:
    def __init__(self, nombre, raza, edad, color, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Raza: {self.raza}\n"
                f"Edad: {self.edad} años\n"
                f"Color: {self.color}\n"
                f"Peso: {self.peso} kg")
