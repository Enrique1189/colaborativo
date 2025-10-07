import random

class GeneradorNombresAleatorios:
    
    def __init__(self):
       
        self.nombres_masculinos = [
            "Alejandro", "Luis", "Carlos", "David", "Miguel", "Javier",
            "Sergio", "Pedro", "Pablo", "Diego", "Hugo", "Lucas", "Martín"
        ]
        self.nombres_femeninos = [
            "Sofía", "María", "Ana", "Laura", "Valeria", "Isabel",
            "Elena", "Andrea", "Paula", "Lucía", "Carla", "Sara", "Julia"
        ]
        self.apellidos = [
            "García", "Rodríguez", "Martínez", "Fernández", "López",
            "González", "Pérez", "Sánchez", "Ramírez", "Torres", "Flores",
            "Rivera", "Díaz", "Morales", "Vargas", "Reyes", "Jiménez"
        ]
        self.prefijos = [
            "Gran ", "Antiguo ", "Noble ", "Veloz ", "Digno ", "Sabio "
        ]
        self.sufijos = [
            " el Magnífico", " el Silencioso", " de la Sombra",
            " Corazón de León", " el Justo", " del Valle"
        ]

    def _obtener_nombre_pila_aleatorio(self, genero=None):
        """
        Método interno para obtener un nombre de pila (primer nombre) aleatorio.
        Puede especificar el género o será aleatorio.
        """
        if genero == "masculino":
            return random.choice(self.nombres_masculinos)
        elif genero == "femenino":
            return random.choice(self.nombres_femeninos)
        else: 
            return random.choice(self._obtener_nombre_pila_aleatorio(genero="masculino") + \
                                  self._obtener_nombre_pila_aleatorio(genero="femenino"))

    def generar_nombre_simple(self, genero=None):
        """
        Genera un nombre simple con nombre de pila y un apellido.
        Ideal para listas básicas o visualización rápida.
        """
        nombre_pila = self._obtener_nombre_pila_aleatorio(genero)
        apellido = random.choice(self.apellidos)
        return f"{nombre_pila} {apellido}"

    def generar_nombre_completo(self, genero=None, doble_apellido=False):
        """
        Genera un nombre más completo, opcionalmente con dos apellidos.
        """
        nombre_pila = self._obtener_nombre_pila_aleatorio(genero)
        apellido1 = random.choice(self.apellidos)
        
        if doble_apellido:
            apellido2 = random.choice(self.apellidos)
       
            while apellido1 == apellido2:
                apellido2 = random.choice(self.apellidos)
            return f"{nombre_pila} {apellido1} {apellido2}"
        else:
            return f"{nombre_pila} {apellido1}"
            
    def generar_nombre_fantasia(self, genero=None, incluir_prefijo=True, incluir_sufijo=True):
        """
        Genera un nombre de fantasía o con un toque épico, añadiendo
        prefijos y/o sufijos a un nombre completo.
        Útil para personajes, nombres de juegos, etc.
        """
        nombre_base = self.generar_nombre_completo(genero)
        
        nombre_fantasia = nombre_base
        if incluir_prefijo and random.choice([True, False]): 
            nombre_fantasia = random.choice(self.prefijos) + nombre_fantasia
        
        if incluir_sufijo and random.choice([True, False]):
            nombre_fantasia += random.choice(self.sufijos)
            
        return nombre_fantasia
