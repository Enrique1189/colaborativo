class pizza:
    def __init__(self, tamaño, masa, salsa, ingredientes, precio):
        self.tamaño = tamaño
        self.masa = masa
        self.salsa = salsa
        self.ingredientes = ingredientes
        self.precio = precio

    def mostrar_detalles(self):
        print("Tamaño: ", self.tamaño)
        print("Masa: ", self.masa)
        print("Salsa: ", self.salsa)                          
        print("Ingredientes", self.ingredientes)
        print("Precio: ", self.precio)

    def agregar_ingredientes(self):
        print("Se agrego un ingrediente a la pizza.")

    def calcular_precio(self):
        print("El precio de la pizza es: ", self.precio)

    def hornear(self):
        print("La pizza se esta horneando...")