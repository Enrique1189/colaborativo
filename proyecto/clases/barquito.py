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
    
barco = BarquitoDeJuguete("azul", "PlayFun", "NautilusX", "mediano", True)

print(barco)
print(barco.encender())
print(barco.apagar())