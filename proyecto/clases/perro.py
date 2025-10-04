class Perro:
    def __init__(self, nombre, raza, peso, altura, sintomas=None):
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.altura = altura
        self.sintomas = sintomas if sintomas is not None else []

    def agregar_sintoma(self, sintoma):
        if sintoma not in self.sintomas:
            self.sintomas.append(sintoma)

    def tiene_sintoma(self, sintoma):
        return sintoma in self.sintomas

    def evaluar_salud(self):
        evaluacion = []

        sintomas_bajos = [s.lower() for s in self.sintomas]

        if "vómito" in sintomas_bajos or "diarrea" in sintomas_bajos:
            evaluacion.append("Posibles problemas gastrointestinales.")
        if "no come" in sintomas_bajos or "letárgico" in sintomas_bajos:
            evaluacion.append("Síntomas de posible enfermedad grave.")
        if not evaluacion:
            evaluacion.append("Síntomas no parecen graves, observar al perro.")

        return evaluacion
