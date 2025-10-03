class CarroDeJuguete:
    def __init__(self, color, marca, modelo, tamaño, tiene_control_remoto):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño 
        self.tiene_control_remoto = tiene_control_remoto

    def encender(self):
        return f"El carro de juguete {self.modelo} está encendido."

    def apagar(self):
        return f"El carro de juguete {self.modelo} está apagado."

    def __str__(self):
        control = "sí" if self.tiene_control_remoto else "no"
        return (f"Carro de Juguete - Modelo: {self.modelo}, Marca: {self.marca}, Color: {self.color}, "
                f"Tamaño: {self.tamaño}, Control remoto: {control}")