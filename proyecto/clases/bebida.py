class Bebida:
    def __init__(self, nombre, tipo, tamaño, temperatura, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.precio = precio
    
    def mostrar(self):
        return f"Bebida: {self.nombre}"
        f"Tipo: {self.tipo}" 
        f"Tamaño: {self.tamaño}"
        f"Temperatura: {self.temperatura}"
        f"Precio: ${self.precio}"
    
    def prepara(self):
        return f"Preparado tu {self.nombre}, {self.temperatura} en tamaño {self.tamaño}... ¡TU {self.nombre} ESTA LISTO!"
    
    def tomar(self):
        return f"Estas tomando {self.nombre}...¡Disfuta!"
    
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje/100)
        self.precio -= descuento
        return f"Se aplico un {porcentaje}% de descuento. Nuevo precio: ${self.precio: .2f}"