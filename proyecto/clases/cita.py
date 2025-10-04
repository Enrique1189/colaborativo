class Cita:
    def __init__(self, fecha, hora, mascota, veterinario, motivo):
        self.fecha = fecha
        self.hora = hora
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.motivo} ({self.mascota.nombre})"