class aguila:
    def __init__(self, nombre, edad, envergadura, velocidad, habitat):
        self.nombre = nombre            
        self.edad = edad               
        self.envergadura = envergadura  
        self.velocidad = velocidad
        self.habitat = habitat        

    def mostrar_info(self):
        return (
            f"Águila: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Envergadura: {self.envergadura} cm\n"
            f"Velocidad máxima: {self.velocidad} km/h\n"
            f"Hábitat: {self.habitat}"
        )
