import tkinter as tk
from tkinter import ttk, messagebox
import random

class Dado:
    def __init__(self, caras_min=4, caras_max=20):
        self.num_caras = random.randint(caras_min, caras_max)

    def tirar(self):
        return random.randint(1, self.num_caras)

class Volado:
    CARA = "Cara"
    CRUZ = "Cruz"

    def tirar(self):
        return random.choice([self.CARA, self.CRUZ])

class GeneradorNombresAleatorios:
    def __init__(self):
        self.nombres_masculinos = ["Alejandro", "Luis", "Carlos", "David", "Miguel"]
        self.nombres_femeninos = ["Sofía", "María", "Ana", "Laura", "Valeria"]
        self.apellidos = ["García", "Rodríguez", "Martínez", "Fernández", "López"]
        self.prefijos = ["Gran ", "Noble ", "Sabio "]
        self.sufijos = [" el Magnífico", " Corazón de León", " el Justo"]

    def _obtener_nombre_pila_aleatorio(self, genero=None):
        if genero == "masculino":
            return random.choice(self.nombres_masculinos)
        elif genero == "femenino":
            return random.choice(self.nombres_femeninos)
        else: 
            return random.choice(self.nombres_masculinos + self.nombres_femeninos)

    def generar_nombre_fantasia(self, genero=None, incluir_prefijo=True, incluir_sufijo=True):
        nombre_base = self._obtener_nombre_pila_aleatorio(genero) + " " + random.choice(self.apellidos)
        
        nombre_fantasia = nombre_base
        if incluir_prefijo and random.choice([True, False]): 
            nombre_fantasia = random.choice(self.prefijos) + nombre_fantasia
        
        if incluir_sufijo and random.choice([True, False]):
            nombre_fantasia += random.choice(self.sufijos)
            
        return nombre_fantasia

class AppJuegos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Juegos y Utilidades (Tkinter)")
        self.geometry("450x350")

        self.dado = Dado()
        self.volado = Volado()
        self.generador_nombres = GeneradorNombresAleatorios()
        
        self.numero_secreto = random.randint(1, 10)
        self.intentos = 0
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        self.crear_pestana_adivina()
        self.crear_pestana_azar()
        self.crear_pestana_nombres()

    def crear_pestana_adivina(self):
        frame_adivina = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame_adivina, text="1. Adivina")

        tk.Label(frame_adivina, text="Adivina el Número (1-10)", font=("Arial", 14, "bold")).pack(pady=5)
        
        self.adivina_mensaje = tk.StringVar(value="Ingresa tu número:")
        tk.Label(frame_adivina, textvariable=self.adivina_mensaje).pack(pady=5)

        self.adivina_entry = tk.Entry(frame_adivina, width=10, justify='center')
        self.adivina_entry.pack(pady=5)
        self.adivina_entry.bind('<Return>', lambda event: self.verificar_adivinanza())

        self.adivina_btn = tk.Button(frame_adivina, text="¡Adivinar!", command=self.verificar_adivinanza)
        self.adivina_btn.pack(pady=10)

        tk.Button(frame_adivina, text="Reiniciar Juego", command=self.reiniciar_adivinanza).pack(pady=5)

    def verificar_adivinanza(self):
        try:
            adivinanza = int(self.adivina_entry.get())
            self.adivina_entry.delete(0, tk.END)
            self.intentos += 1

            if not 1 <= adivinanza <= 10:
                self.adivina_mensaje.set("⚠️ Rango no válido. El número es entre 1 y 10.")
            elif adivinanza < self.numero_secreto:
                self.adivina_mensaje.set(f"⬇️ Intento {self.intentos}: Demasiado bajo.")
            elif adivinanza > self.numero_secreto:
                self.adivina_mensaje.set(f"⬆️ Intento {self.intentos}: Demasiado alto.")
            else:
                self.adivina_mensaje.set(f"🎉 ¡Correcto! Era {self.numero_secreto}. Lo lograste en {self.intentos} intentos.")
                self.adivina_btn.config(state=tk.DISABLED)
                self.adivina_entry.config(state=tk.DISABLED)
                messagebox.showinfo("Ganaste", f"¡Felicidades! Lo lograste en {self.intentos} intentos.")

        except ValueError:
            self.adivina_mensaje.set("⚠️ Ingresa solo números enteros.")
            self.adivina_entry.delete(0, tk.END)

    def reiniciar_adivinanza(self):
        self.numero_secreto = random.randint(1, 10)
        self.intentos = 0
        self.adivina_mensaje.set("¡Adivina el nuevo número del 1 al 10!")
        self.adivina_btn.config(state=tk.NORMAL)
        self.adivina_entry.config(state=tk.NORMAL)

    def crear_pestana_azar(self):
        frame_azar = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame_azar, text="2. Azar")
        
        tk.Label(frame_azar, text=f"Dado de {self.dado.num_caras} Caras", font=("Arial", 12, "bold")).pack(pady=5)
        
        self.dado_resultado = tk.StringVar(value="Presiona 'Tirar Dado'")
        tk.Label(frame_azar, textvariable=self.dado_resultado, font=("Arial", 20)).pack(pady=5)
        
        tk.Button(frame_azar, text="Tirar Dado 🎲", command=self.tirar_dado).pack(pady=10)

        ttk.Separator(frame_azar, orient='horizontal').pack(fill='x', pady=10)

        tk.Label(frame_azar, text="Lanzamiento de Moneda (Volado)", font=("Arial", 12, "bold")).pack(pady=5)
        
        self.volado_resultado = tk.StringVar(value="Presiona 'Lanzar Moneda'")
        tk.Label(frame_azar, textvariable=self.volado_resultado, font=("Arial", 20)).pack(pady=5)
        
        tk.Button(frame_azar, text="Lanzar Moneda 💰", command=self.tirar_volado).pack(pady=10)

    def tirar_dado(self):
        resultado = self.dado.tirar()
        self.dado_resultado.set(f"Resultado: {resultado}")

    def tirar_volado(self):
        resultado = self.volado.tirar()
        self.volado_resultado.set(f"Resultado: {resultado}")

    def crear_pestana_nombres(self):
        frame_nombres = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame_nombres, text="3. Nombres")

        tk.Label(frame_nombres, text="Generador de Nombres de Fantasía", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.nombre_resultado = tk.StringVar(value="Presiona el botón para generar un nombre épico.")
        tk.Label(frame_nombres, textvariable=self.nombre_resultado, font=("Arial", 12, "italic"), wraplength=400).pack(pady=10)

        tk.Button(frame_nombres, text="Generar Nombre Épico 🧙‍♂️", command=self.generar_nombre).pack(pady=10)

    def generar_nombre(self):
        nombre = self.generador_nombres.generar_nombre_fantasia(incluir_prefijo=True, incluir_sufijo=True)
        self.nombre_resultado.set(nombre)

if __name__ == "__main__":
    app = AppJuegos()
    app.mainloop()