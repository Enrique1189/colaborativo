#Definir una clase de coche.
class Avion:
    #Es el método constructor __init__
    #Se ejecuta cada vez que creamos un objeto de la clase coche.

    def __init__(self, cargamento, capacidad, tamaño, modelo, color):
        self.cargamento=cargamento #atributo cargamento
        self.capacidad=capacidad #atributo capacidad
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
Avion_United_Airlines = Avion ("Personas y maletas","Entre 150 y 180 personas y mas de 100 kg de equipaje","longitud de aproximadamente 39.5 metros, una envergadura (distancia entre las puntas de las alas) de unos 35.8 metros y una altura de cola de alrededor de 12.5 metros","Boeing 737","En su mayoria blancos")


print("\n--- AVION AMERICAN AIRLINES ---")
Avion_American_Airlines.mostrar_info()

print("\n--- AVION UNITED AIRLINES ---")
Avion_United_Airlines.mostrar_info()