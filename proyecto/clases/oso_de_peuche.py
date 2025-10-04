class OsoDePeluche:
    def __init__(self, color, tamaño, marca, material, es_trasladable):
        self.color = color
        self.tamaño = tamaño
        self.marca = marca
        self.material = material
        self.es_trasladable = es_trasladable

    def abrazar(self):
        return f"¡Abraza al adorable oso de peluche de {self.color} y {self.tamaño} tamaño!."

    def lavar(self):
        return f"El oso de peluche {self.marca} ha sido lavado con cuidado."

    def __str__(self):
        trasladable = "sí" if self.es_trasladable else "no"
        return (f"Oso de Peluche - Marca: {self.marca}, Color: {self.color}, Tamaño: {self.tamaño}, "
                f"Material: {self.material}, Trasladable: {trasladable}")
    
# Creando una instancia de OsoDePeluche
oso = OsoDePeluche("marrón", "grande", "TeddyBear", "algodón", True)

# Mostrando la información y acciones del oso
print(oso)
print(oso.abrazar())
print(oso.lavar())
