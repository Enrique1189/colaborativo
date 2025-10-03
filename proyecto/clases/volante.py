import tkinter as tk

class Volante:
    def __init__(self, material, diametro, color, tipo, peso):
        self.material = material
        self.diametro = diametro
        self.color = color
        self.tipo = tipo
        self.peso = peso

    def get_info(self):
        return (
            f"Material: {self.material}\n"
            f"Diámetro: {self.diametro} cm\n"
            f"Color: {self.color}\n"
            f"Tipo: {self.tipo}\n"
            f"Peso: {self.peso} g"
        )

class VentanaVolante(tk.Tk):
    def __init__(self, volante):
        super().__init__()
        self.title("Información del Volante")
        self.geometry("300x200")
        
        self.label_info = tk.Label(self, text=volante.get_info(), justify="left", font=("Arial", 12))
        self.label_info.pack(padx=10, pady=10)

volante1 = Volante("Cuero", 35, "Negro", "Deportivo", 800)

app = VentanaVolante(volante1)
app.mainloop()
