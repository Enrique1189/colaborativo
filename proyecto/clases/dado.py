import random

class Dado:
    """
    Una clase que representa un dado con un número aleatorio de caras.
    """

    def __init__(self, caras_min=4, caras_max=20):
        """
        Inicializa el dado. El número de caras se elige aleatoriamente.
        :param caras_min: Mínimo número de caras que puede tener el dado.
        :param caras_max: Máximo número de caras que puede tener el dado.
        """
        self.num_caras = random.randint(caras_min, caras_max)
        print(f"🎲 ¡Se ha creado un dado de {self.num_caras} caras!")

    def tirar(self, veces=1):
        """
        Simula una o varias tiradas del dado.
        :param veces: Número de veces que se tira el dado (por defecto es 1).
        :return: El resultado de la última tirada si es una vez, o una lista de resultados.
        """
        if veces < 1:
            return []

        resultados = []
        for _ in range(veces):
            resultado = random.randint(1, self.num_caras)
            resultados.append(resultado)

        if veces == 1:
            return resultados[0]
        else:
            return resultados

    def __str__(self):
        """Representación de cadena de la clase."""
        return f"Soy un dado de {self.num_caras} caras. ¡Prueba a tirarme!"

print("--- Creando el Dado ---")
mi_dado_aleatorio = Dado()

print("\n--- Haciendo Tiradas ---")
tirada_simple = mi_dado_aleatorio.tirar()
print(f"El dado se ha tirado una vez, resultado: {tirada_simple}")

tiradas_multiples = mi_dado_aleatorio.tirar(veces=5)
print(f"El dado se ha tirado 5 veces, resultados: {tiradas_multiples}")