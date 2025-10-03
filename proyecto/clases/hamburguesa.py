class Hamburguesa:
    def __init__(self,nombre, tamaño, pan, carne, aderezos, queso, complementos):
        self.nombre = nombre
        self.tamaño = tamaño
        self.pan = pan
        self.carne = carne
        self.aderezos = aderezos
        self.queso = queso
        self.complementos = complementos
        self.precio = 0
        
    def comer():
        print(f"El cliente está comiendo una deliciosa hambuerguesa de {self.nombre}")