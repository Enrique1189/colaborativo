import random

class Volado:
    """
    Una clase que representa el lanzamiento de una moneda (un 'volado').
    Solo tiene dos 'caras': 'Cara' y 'Cruz'.
    """
    CARA = "Cara"
    CRUZ = "Cruz"

    def __init__(self):
        """
        Inicializa el volado.
        """
        self.num_resultados = 2
        print("💰 ¡Se ha creado una moneda lista para ser lanzada!")

    def tirar(self):
        """
        Simula una única tirada del volado.
        :return: El resultado ('Cara' o 'Cruz').
        """
        resultado_numerico = random.randint(0, 1)

        if resultado_numerico == 0:
            return self.CARA
        else:
            return self.CRUZ

    def __str__(self):
        """Representación de cadena de la clase."""
        return "Soy una moneda de 2 lados ('Cara' y 'Cruz'). ¡Lánzame!"

print("\n" + "="*30)
print("--- Creando el Volado (Moneda) ---")
mi_volado = Volado()

print("\n--- Haciendo un Lanzamiento Único ---")
lanzamiento_1 = mi_volado.tirar()
print(f"Resultado del lanzamiento 1: {lanzamiento_1}")

lanzamiento_2 = mi_volado.tirar()
print(f"Resultado del lanzamiento 2: {lanzamiento_2}")

print("="*30)