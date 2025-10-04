class Leon:
    def __init__(self, nombre, edad, peso, habitat, color_melena):
        self.nombre = nombre         
        self.edad = edad              
        self.peso = peso            
        self.habitat = habitat        
        self.color_melena = color_melena  

    def obtener_info(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Peso: {self.peso} kg\n"
            f"Hábitat: {self.habitat}\n"
            f"Color de melena: {self.color_melena}"
        )
