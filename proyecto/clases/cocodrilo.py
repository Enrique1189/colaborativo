# clases/cocodrilo.py

class Cocodrilo:
    def __init__(self, nombre, edad, especie, longitud, peso):
        self.nombre = nombre          
        self.edad = edad             
        self.especie = especie       
        self.longitud = longitud     
        self.peso = peso              

    def __str__(self):
        return (
            f"🐊 Información del Cocodrilo:\n"
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Especie: {self.especie}\n"
            f"Longitud: {self.longitud} m\n"
            f"Peso: {self.peso} kg"
        )
