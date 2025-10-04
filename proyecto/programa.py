import tkinter as tk
from tkinter import messagebox

class Combustible:
    def __init__(self, tipo, octanaje, precio_por_litro, proveedor, origen):
        self.tipo = tipo
        self.octanaje = octanaje
        self.precio_por_litro = precio_por_litro
        self.proveedor = proveedor
        self.origen = origen

    def obtener_info(self):
        return (
            f"Tipo: {self.tipo}\n"
            f"Octanaje: {self.octanaje}\n"
            f"Precio por litro: ${self.precio_por_litro:.2f}\n"
            f"Proveedor: {self.proveedor}\n"
            f"Origen: {self.origen}"
        )

class InteriorAuto:
    def __init__(self, marca, tipo_asientos, material, color, sistema_audio):
        self.marca = marca
        self.tipo_asientos = tipo_asientos
        self.material = material
        self.color = color
        self.sistema_audio = sistema_audio

    def obtener_info(self):
        return (
            f"Marca: {self.marca}\n"
            f"Tipo de Asientos: {self.tipo_asientos}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Sistema de Audio: {self.sistema_audio}"
        )

class Llanta:
    def __init__(self, marca, diametro, ancho, tipo, indice_carga):
        self.marca = marca
        self.diametro = diametro
        self.ancho = ancho
        self.tipo = tipo
        self.indice_carga = indice_carga

    def obtener_info(self):
        return (
            f"Marca: {self.marca}\n"
            f"Diámetro: {self.diametro} pulgadas\n"
            f"Ancho: {self.ancho} mm\n"
            f"Tipo: {self.tipo}\n"
            f"Índice de carga: {self.indice_carga}"
        )

class Velocidad:
    def __init__(self, valor, unidad, direccion, tiempo, aceleracion):
        self.valor = valor
        self.unidad = unidad
        self.direccion = direccion
        self.tiempo = tiempo
        self.aceleracion = aceleracion

    def obtener_info(self):
        return (
            f"Velocidad: {self.valor} {self.unidad}\n"
            f"Dirección: {self.direccion}\n"
            f"Tiempo: {self.tiempo} s\n"
            f"Aceleración: {self.aceleracion} m/s²"
        )

class Volante:
    def __init__(self, material, diametro, color, tipo, peso):
        self.material = material
        self.diametro = diametro
        self.color = color
        self.tipo = tipo
        self.peso = peso

    def obtener_info(self):
        return (
            f"Material: {self.material}\n"
            f"Diámetro: {self.diametro} cm\n"
            f"Color: {self.color}\n"
            f"Tipo: {self.tipo}\n"
            f"Peso: {self.peso} g"
        )

def ventana_combustible(root):
    w = tk.Toplevel(root)
    w.title("Registro de Combustible")
    w.geometry("340x340")

    campos = ["Tipo", "Octanaje", "Precio por litro", "Proveedor", "Origen"]
    entradas = {}

    for campo in campos:
        tk.Label(w, text=f"{campo}:").pack(anchor="w", padx=10, pady=(8,0))
        e = tk.Entry(w)
        e.pack(fill="x", padx=10)
        entradas[campo] = e

    def mostrar_info():
        tipo = entradas["Tipo"].get()
        octanaje = entradas["Octanaje"].get()
        precio = entradas["Precio por litro"].get()
        proveedor = entradas["Proveedor"].get()
        origen = entradas["Origen"].get()

        if not (tipo and octanaje and precio and proveedor and origen):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.", parent=w)
            return

        try:
            octanaje = int(octanaje)
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "Octanaje debe ser número entero y precio un número decimal.", parent=w)
            return

        c = Combustible(tipo, octanaje, precio, proveedor, origen)
        messagebox.showinfo("Información del Combustible", c.obtener_info(), parent=w)

    tk.Button(w, text="Mostrar información", command=mostrar_info).pack(pady=15)

def ventana_interior(root):
    w = tk.Toplevel(root)
    w.title("Registro de Interior")
    w.geometry("340x340")

    campos = ["Marca", "Tipo de Asientos", "Material", "Color", "Sistema de Audio"]
    entradas = {}

    for campo in campos:
        tk.Label(w, text=f"{campo}:").pack(anchor="w", padx=10, pady=(8,0))
        e = tk.Entry(w)
        e.pack(fill="x", padx=10)
        entradas[campo] = e

    def mostrar_info():
        valores = [entradas[c].get() for c in campos]
        if not all(valores):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.", parent=w)
            return
        interior = InteriorAuto(*valores)
        messagebox.showinfo("Información del Interior", interior.obtener_info(), parent=w)

    tk.Button(w, text="Mostrar información", command=mostrar_info).pack(pady=15)

def ventana_llantas(root):
    w = tk.Toplevel(root)
    w.title("Registro de Llantas")
    w.geometry("340x340")

    campos = ["Marca", "Diámetro", "Ancho", "Tipo", "Índice de carga"]
    entradas = {}

    for campo in campos:
        tk.Label(w, text=f"{campo}:").pack(anchor="w", padx=10, pady=(8,0))
        e = tk.Entry(w)
        e.pack(fill="x", padx=10)
        entradas[campo] = e

    def mostrar_info():
        marca = entradas["Marca"].get()
        diametro = entradas["Diámetro"].get()
        ancho = entradas["Ancho"].get()
        tipo = entradas["Tipo"].get()
        indice = entradas["Índice de carga"].get()

        if not (marca and diametro and ancho and tipo and indice):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.", parent=w)
            return

        try:
            diametro = int(diametro)
            ancho = int(ancho)
            indice = int(indice)
        except ValueError:
            messagebox.showerror("Error", "Diámetro, Ancho e Índice deben ser números.", parent=w)
            return

        llanta = Llanta(marca, diametro, ancho, tipo, indice)
        messagebox.showinfo("Información de la Llanta", llanta.obtener_info(), parent=w)

    tk.Button(w, text="Mostrar información", command=mostrar_info).pack(pady=15)

def ventana_velocidad(root):
    w = tk.Toplevel(root)
    w.title("Registro de Velocidad")
    w.geometry("340x360")

    campos = ["Valor", "Unidad", "Dirección", "Tiempo", "Aceleración"]
    entradas = {}

    for campo in campos:
        tk.Label(w, text=f"{campo}:").pack(anchor="w", padx=10, pady=(8,0))
        e = tk.Entry(w)
        e.pack(fill="x", padx=10)
        entradas[campo] = e

    def mostrar_info():
        valor = entradas["Valor"].get()
        unidad = entradas["Unidad"].get()
        direccion = entradas["Dirección"].get()
        tiempo = entradas["Tiempo"].get()
        aceleracion = entradas["Aceleración"].get()

        if not (valor and unidad and direccion and tiempo and aceleracion):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.", parent=w)
            return

        try:
            valor = float(valor)
            tiempo = float(tiempo)
            aceleracion = float(aceleracion)
        except ValueError:
            messagebox.showerror("Error", "Valor, Tiempo y Aceleración deben ser números.", parent=w)
            return

        v = Velocidad(valor, unidad, direccion, tiempo, aceleracion)
        messagebox.showinfo("Información de la Velocidad", v.obtener_info(), parent=w)

    tk.Button(w, text="Mostrar información", command=mostrar_info).pack(pady=15)

def ventana_volante(root):
    w = tk.Toplevel(root)
    w.title("Registro de Volante")
    w.geometry("340x340")

    campos = ["Material", "Diámetro", "Color", "Tipo", "Peso"]
    entradas = {}

    for campo in campos:
        tk.Label(w, text=f"{campo}:").pack(anchor="w", padx=10, pady=(8,0))
        e = tk.Entry(w)
        e.pack(fill="x", padx=10)
        entradas[campo] = e

    def mostrar_info():
        material = entradas["Material"].get()
        diametro = entradas["Diámetro"].get()
        color = entradas["Color"].get()
        tipo = entradas["Tipo"].get()
        peso = entradas["Peso"].get()

        if not (material and diametro and color and tipo and peso):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.", parent=w)
            return

        try:
            diametro = float(diametro)
            peso = float(peso)
        except ValueError:
            messagebox.showerror("Error", "Diámetro y Peso deben ser números.", parent=w)
            return

        vol = Volante(material, diametro, color, tipo, peso)
        messagebox.showinfo("Información del Volante", vol.obtener_info(), parent=w)

    tk.Button(w, text="Mostrar información", command=mostrar_info).pack(pady=15)

root = tk.Tk()
root.title("Proyecto - Componentes del Auto")
root.geometry("400x420")

tk.Label(root, text="Selecciona un componente", font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(root, text="Combustible", width=25, command=lambda: ventana_combustible(root)).pack(pady=8)
tk.Button(root, text="Interior del Auto", width=25, command=lambda: ventana_interior(root)).pack(pady=8)
tk.Button(root, text="Llantas", width=25, command=lambda: ventana_llantas(root)).pack(pady=8)
tk.Button(root, text="Velocidad", width=25, command=lambda: ventana_velocidad(root)).pack(pady=8)
tk.Button(root, text="Volante", width=25, command=lambda: ventana_volante(root)).pack(pady=8)

root.mainloop()
