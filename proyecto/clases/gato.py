class Gato:
    def __init__(self, nombre, edad, peso, vacunado, sintomas):
        self.nombre = nombre                # str
        self.edad = edad                    # str o float
        self.peso = peso                    # str o float
        self.vacunado = vacunado            # bool
        self.sintomas = sintomas            # str

    def evaluar_salud(self):
        sintomas_bajos = self.sintomas.lower()
        evaluacion = []

        if "vómito" in sintomas_bajos or "diarrea" in sintomas_bajos:
            evaluacion.append("Posibles problemas gastrointestinales.")
        elif "no come" in sintomas_bajos or "letárgico" in sintomas_bajos:
            evaluacion.append("Síntomas de posible enfermedad grave.")
        else:
            evaluacion.append("Síntomas no parecen graves, observar al gato.")

        if not self.vacunado:
            evaluacion.append("El gato no está vacunado. Se recomienda vacunación.")

        return evaluacion
