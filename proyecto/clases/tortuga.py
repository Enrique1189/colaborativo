
class Tortuga:
    def __init__(self, nombre, edad, especie, peso, color_caparazon):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.peso = peso
        self.color_caparazon = color_caparazon

    def __str__(self):
        return (
            f"🐢 Información de la Tortuga:\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Especie: {self.especie}\n"
            f"Peso: {self.peso} kg\n"
            f"Color del caparazón: {self.color_caparazon}"
        )
