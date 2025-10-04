class LegoDeJuguete:
    def __init__(self, color, marca, num_piezas, tema, es_compatible_con_otros_sets):
        self.color = color
        self.marca = marca
        self.num_piezas = num_piezas
        self.tema = tema
        self.es_compatible_con_otros_sets = es_compatible_con_otros_sets

    def armar(self):
        return f"El set de Lego {self.tema} está siendo armado. ¡Cuidado con las piezas!"

    def desarmar(self):
        return f"El set de Lego {self.tema} ha sido desarmado."

    def __str__(self):
        compatible = "sí" if self.es_compatible_con_otros_sets else "no"
        return (f"Lego de Juguete - Tema: {self.tema}, Marca: {self.marca}, Color: {self.color}, "
                f"Número de piezas: {self.num_piezas}, Compatible con otros sets: {compatible}")
    
# Creando una instancia de LegoDeJuguete
lego = LegoDeJuguete("rojo", "LEGO", 500, "Espacio", True)

# Mostrando la información y acciones del Lego
print(lego)
print(lego.armar())
print(lego.desarmar())
