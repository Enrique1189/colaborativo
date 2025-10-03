class Helado:
    def __init__(self, sabor, precio, tamaño, presentacion, tipo_liquido):
        self.sabor = sabor               
        self.precio = precio              
        self.tamaño = tamaño              
        self.presentacion = presentacion  
        self.tipo_liquido = tipo_liquido  
        self.topping = None               

    def elegir_sabor(self, nuevo_sabor):
        self.sabor = nuevo_sabor
        print(f"Sabor elegido: {self.sabor}")

    def elegir_presentacion(self, nueva_presentacion):
        self.presentacion = nueva_presentacion
        print(f"Presentación elegida: {self.presentacion}")

    def elegir_topping(self, nuevo_topping):
        self.topping = nuevo_topping
        print(f"Topping agregado: {self.topping}")

    def calcular_precio_final(self):
        precio_final = self.precio

        # variación del precio dependiendo del tamaño
        if self.tamaño == "mediano":
            precio_final += 10
        elif self.tamaño == "grande":
            precio_final += 20

        # ajuste para presentación
        if self.presentacion == "cono":
            precio_final += 5

        # ajuste de topping
        if self.topping:
            precio_final += 7

        print(f"Precio final: ${precio_final}")
        return precio_final

    def vender(self):
        print(f"Vendiendo helado de {self.sabor} en {self.presentacion} con topping {self.topping if self.topping else 'sin topping'}.")
        precio = self.calcular_precio_final()
        print(f"Helado vendido por ${precio}.")


mi_helado = Helado("vainilla", 50, "pequeño", "vasito", "leche")
mi_helado.elegir_sabor("chocolate")
mi_helado.elegir_presentacion("cono")
mi_helado.elegir_topping("chispas de chocolate")
mi_helado.vender()
