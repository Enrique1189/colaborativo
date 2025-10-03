import tkinter as tk

class Combustible:
    def __init__(self, tipo, octanaje, precio_por_litro, proveedor, origen):
        self.tipo = tipo
        self.octanaje = octanaje
        self.precio_por_litro = precio_por_litro
        self.proveedor = proveedor
        self.origen = origen

class App(tk.Tk):
    def __init__(self, combustible):
        super().__init__()
        self.title("Información de Combustible")
        self.geometry("300x200")
        self.combustible = combustible
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text="Tipo:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(self, text=self.combustible.tipo).grid(row=0, column=1, sticky="w")
        
        tk.Label(self, text="Octanaje:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Label(self, text=str(self.combustible.octanaje)).grid(row=1, column=1, sticky="w")
        
        tk.Label(self, text="Precio por litro:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Label(self, text=f"${self.combustible.precio_por_litro:.2f}").grid(row=2, column=1, sticky="w")
        
        tk.Label(self, text="Proveedor:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Label(self, text=self.combustible.proveedor).grid(row=3, column=1, sticky="w")
        
        tk.Label(self, text="Origen:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        tk.Label(self, text=self.combustible.origen).grid(row=4, column=1, sticky="w")

if __name__ == "__main__":
    combustible = Combustible("Gasolina", 95, 1.25, "Repsol", "España")
    app = App(combustible)
    app.mainloop()
