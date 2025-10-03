class Ratita:
    def __init__(self, nombre="", peso=0.0, edad=0, sintomas="", actividad="Media"):
        """
        Clase que representa los datos de una ratita paciente.
        Los valores por defecto son neutros y pueden ser actualizados después.
        """
        self.nombre = nombre
        self.peso = peso  # en gramos
        self.edad = edad  # en meses
        self.sintomas = sintomas
        self.actividad = actividad

    def actualizar_datos(self, nombre, peso, edad, sintomas, actividad):
        """
        Permite actualizar todos los atributos de la ratita.
        """
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.sintomas = sintomas
        self.actividad = actividad

    def obtener_datos(self):
        """
        Devuelve un diccionario con los datos actuales de la ratita.
        """
        return {
            "nombre": self.nombre,
            "peso": self.peso,
            "edad": self.edad,
            "sintomas": self.sintomas,
            "actividad": self.actividad
        }
