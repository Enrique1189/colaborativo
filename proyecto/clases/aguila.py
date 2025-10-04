class Aguila:
    def __init__(self, nombre, edad, envergadura, velocidad, habitat):
        self.nombre = nombre            
        self.edad = edad               
        self.envergadura = envergadura  
        self.velocidad = velocidad
        self.habitat = habitat        

    def mostrar_info(self):
        print(f"Águila: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Envergadura: {self.envergadura} cm")
        print(f"Velocidad máxima: {self.velocidad} km/h")
        print(f"Hábitat: {self.habitat}")


aguila1 = Aguila("Águila Real", 5, 220, 160, "Montañas")
aguila1.mostrar_info()