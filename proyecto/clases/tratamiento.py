class Tratamiento:
    def _init_(self, nombre, descripcion, duracion, costo, mascota):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.costo = costo
        self.mascota = mascota

    def _str_(self):
        return f"{self.nombre} - {self.mascota.nombre} (${self.costo})"