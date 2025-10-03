class Avioncito:
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad

    def despegar(self):
        return f"El avión {self.modelo} está despegando."

    def aterrizar(self):
        return f"El avión {self.modelo} está aterrizando."



    def __str__(self):
        return f"Avión Modelo: {self.modelo}, Capacidad: {self.capacidad} pasajeros"