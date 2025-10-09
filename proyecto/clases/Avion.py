class Avion:

    def __init__(self, cargamento, capacidad, tamaño, modelo, color):
        self.cargamento=cargamento 
        self.capacidad=capacidad 
        self.tamaño=tamaño
        self.modelo=modelo
        self.color=color
    
   
    def mostrar_info(self):
        print(f"---Información de avion---")
        print(f"Cargamento: {self.cargamento}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color} \n")


Avion_American_Airlines = Avion ("Personas y maletas","Entre 150 y 180 personas y mas de 100 kg de equipaje","Su tamaño roda los 38m","Airbus A320","En su mayoria blancos")

print("\n--- AVION AMERICAN AIRLINES ---")
Avion_American_Airlines.mostrar_info()
