class Pastel:
    def __init__(self, tamaño, sabor, decoración, capas, tipo_glaseado, color):
        self.tamaño = tamaño         
        self.sabor = sabor            
        self.decoración = decoración  
        self.capas = capas            
        self.tipo_glaseado = tipo_glaseado 
        self.color = color           
    
    def preparar(self):
        print(f"Preparar el pastel {self.color} de {self.sabor}...")

    def decorar(self):
        print(f"Decorar el pastel con {self.decoración} y {self.capas} capas.")
    
    def aplicar_glasé(self):
        print(f"Añadir glaseado de {self.tipo_glaseado} al pastel.")
    
    def servir(self):
        print(f"Es un pastel {self.color} de tamaño {self.tamaño}, con {self.capas} capas y glaseado de {self.tipo_glaseado} está por servirse. ;)")

    def mostrar_info(self):
        info = (
            f"\nPastel Rosa:\n"
            f"Tamaño: {self.tamaño}\n"
            f"Sabor: {self.sabor}\n"
            f"Decoración: {self.decoración}\n"
            f"Capas: {self.capas}\n"
            f"Tipo de glaseado: {self.tipo_glaseado}\n"
            f"Color: {self.color}\n"
        )
        print(info)

def crear_pastel():
    tamaño = input("Ingresa el tamaño del pastel: ")
    sabor = input("Ingresa el sabor del pastel: ")
    decoración = input("Ingresa la decoración del pastel: ")
    capas = int(input("Ingresa el número de capas: "))
    tipo_glaseado = input("Ingresa el tipo de glaseado: ")
    color = input("Ingresa el color del pastel: ")

    pastel = Pastel(tamaño, sabor, decoración, capas, tipo_glaseado, color)

    pastel.preparar()
    pastel.decorar()
    pastel.aplicar_glasé()
    pastel.servir()
    pastel.mostrar_info()

crear_pastel()
