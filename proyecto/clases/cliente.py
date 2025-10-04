class Cliente:
    def __init__(self, nombre, telefono, direccion, correo, mascota):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.mascota = mascota

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"
