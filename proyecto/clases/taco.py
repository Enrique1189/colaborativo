##Clase ejemplo a desarrollar
# Definir la clase Taco con 5 características y 5 funciones
class Taco:
    def __init__(self, tipo, salsa, tamaño, tortilla, picante):
        # 5 características (atributos)
        self.tipo = tipo                # Tipo de carne o relleno (ej: pastor, asada)
        self.salsa = salsa              # Tipo de salsa (ej: verde, roja)
        self.tamaño = tamaño            # Tamaño del taco (ej: pequeño, grande)
        self.tortilla = tortilla        # Tipo de tortilla (maíz o harina)
        self.picante = picante          # Nivel de picante 
        self.ingredientes = [tipo]      # Ingredientes adicionales, inicia con el tipo
        
    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
        print(f"Se agregó {ingrediente} al taco.")

    def cambiar_salsa(self, nueva_salsa):
        print(f"Cambiando la salsa de {self.salsa} a {nueva_salsa}.")
        self.salsa = nueva_salsa

    def cambiar_tamaño(self, nuevo_tamaño):
        print(f"Cambiando el tamaño de {self.tamaño} a {nuevo_tamaño}.")
        self.tamaño = nuevo_tamaño

    def toggle_picante(self):
        self.picante = not self.picante
        estado = "picante" if self.picante else "sin picante"
        print(f"El taco ahora está {estado}.")

    def mostrar_info(self):
        print("------ INFORMACIÓN DEL TACO ------")
        print(f"Tipo: {self.tipo}")
        print(f"Salsa: {self.salsa}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Tortilla: {self.tortilla}")
        print(f"Picante: {'Sí' if self.picante else 'No'}")
        print(f"Ingredientes: {', '.join(self.ingredientes)}")
        print("----------------------------------")


mi_taco = Taco("pastor", "verde", "normal", "maíz", True)

mi_taco.mostrar_info()
mi_taco.agregar_ingrediente("cebolla")
mi_taco.agregar_ingrediente("cilantro")
mi_taco.cambiar_salsa("roja")
mi_taco.cambiar_tamaño("grande")
mi_taco.toggle_picante()
mi_taco.mostrar_info()
