class Mascota:
    def __init__(self, nombre, especie, raza, edad, dueño):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueño = dueño

    def __str__(self):
        return f"{self.nombre} ({self.especie}, {self.raza}) - {self.edad} años"
