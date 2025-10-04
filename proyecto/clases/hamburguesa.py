class Hamburguesa:
    def __init__(self,nombre, tamaño, pan, carne, aderezos, queso, complementos, cantidad):
        self.cantidad = cantidad
        self.nombre = nombre
        self.tamaño = tamaño
        self.pan = pan
        self.carne = carne
        self.aderezos = aderezos
        self.queso = queso
        self.complementos = complementos
        self.precio = 0
        self.dinero = 100
        self.propina = 0
        
    def comer(self):
        return (f"El {self.nombre} está comiendo una deliciosa hambuerguesa!")
        
    def vender(self):
        return (f"La orden de {self.nombre} está lista!\n"
                f"Dinero en la caja: ${self.dinero: .2f} | Propina {self.propina: .2f}")
        
    def descuento(self):
        if self.cantidad >= 3:
            self.precio  -= self.precio - (self.precio * 0.15)
            return (f"Felicidades! Tienes un 15% de descuento por tu gran compra!\n "
                    f"Costo original: {self.precio: .2f} | Costo con descuento: {self.precio: .2f}")
        else:
            pass
    
    def preparar(self):
        return (f"La orden de {self.nombre} se está preparando... :D")
    
    
#datos del cliente