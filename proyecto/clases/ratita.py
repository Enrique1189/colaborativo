# proyecto/clases/ratita.py

class Ratita:
    def __init__(self, nombre, peso, edad, sintomas, actividad):
        self.nombre = nombre
        self.peso = peso  # gramos
        self.edad = edad  # meses
        self.sintomas = sintomas
        self.actividad = actividad  # "Alta", "Media", "Baja"

    def evaluar_salud(self):
        resultado = []
        if self.peso < 150:
            resultado.append("⚠️ Peso bajo para una ratita.")
        if "estornudo" in self.sintomas.lower() or "moco" in self.sintomas.lower():
            resultado.append("🔬 Posible infección respiratoria.")
        if self.actividad.lower() == "baja":
            resultado.append("⚠️ Actividad baja, puede estar enferma.")
        if not resultado:
            resultado.append("✅ Ratita en buen estado general.")
        return resultado
