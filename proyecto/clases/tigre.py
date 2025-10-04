
class Animal:
    def __init__(self, nombre, especie, edad, peso_kg, talla_cm, color_pelaje):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso_kg = peso_kg
        self.talla_cm = talla_cm
        self.color_pelaje = color_pelaje

    def mostrar_info(self):
        print(f" {self.nombre} ({self.especie})")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso_kg} kg")
        print(f"Talla: {self.talla_cm} cm")
        print(f"Color del pelaje: {self.color_pelaje}\n")