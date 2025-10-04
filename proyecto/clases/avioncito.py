#5 atributos y 3 métodos
class AvioncitoDeJuguete:
    def __init__(self, color, tamaño, material, marca, modelo):
        self.color = color
        self.tamaño = tamaño
        self.material = material
        self.marca = marca
        self.modelo = modelo

    def volar(self):
        return f"El avioncito {self.marca} está volando."

    def aterrizar(self):
        return f"El avioncito {self.marca} ha aterrizado."

    def mostrar_info(self):
        return (f"Avioncito de juguete - Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Color: {self.color}, Tamaño: {self.tamaño}, Material: {self.material}")
        
        
# Ejemplo de uso
avioncito1 = AvioncitoDeJuguete("Rojo", "Pequeño", "Plástico", "ToyAir", "X100")
print(avioncito1.mostrar_info())
print(avioncito1.volar())
print(avioncito1.aterrizar())
    