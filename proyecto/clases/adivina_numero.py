import random

print("¡Adivina el número del 1 al 10!")

# Genera un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
intento = 0
adivinanza = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Escribe tu número: "))
    intento += 1

    if adivinanza < numero_secreto:
        print("Demasiado bajo, intenta con un número más grande.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto, intenta con un número más pequeño.")
    else:
        print(f"¡Correcto! El número era {numero_secreto}.")
        print(f"Lo lograste en {intento} intentos.")