class gato:
    def __init__(self, nombre, color, edad, raza, sonido):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.raza = raza
        self.sonido = sonido

    def mostrar_datos(self):
        # Mostrar los valores guardados
        texto = (
            f"Nombre: {self.nombre}\n"
            f"Color: {self.color}\n"
            f"Edad: {self.edad} años\n"
            f"Raza: {self.raza}\n"
            f"Sonido: {self.sonido}"
        )