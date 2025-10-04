class Veterinario:
    def __init__(self, nombre, especialidad, telefono, correo, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo
        self.experiencia = experiencia

    def __str__(self):
        return f"Dr. {self.nombre} ({self.especialidad})"