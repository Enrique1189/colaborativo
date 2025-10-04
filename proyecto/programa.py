#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s

import tkinter as tk
from tkinter import ttk, messagebox
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

def mostrar_interior():
    marca = interior_entries['marca'].get()
    tipo_asientos = interior_entries['tipo_asientos'].get()
    material = interior_entries['material'].get()
    color = interior_entries['color'].get()
    sistema_audio = interior_entries['sistema_de_audio'].get()

    if not (marca and tipo_asientos and material and color and sistema_audio):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos del interior.")
        return

    interior = InteriorAuto(marca, tipo_asientos, material, color, sistema_audio)
    info = interior.obtener_info()
    messagebox.showinfo("Información del Interior del Auto", info)

def mostrar_llanta():
    marca = llanta_entries['marca'].get()
    diametro = llanta_entries['diametro'].get()
    ancho = llanta_entries['ancho'].get()
    tipo = llanta_entries['tipo'].get()
    indice_carga = llanta_entries['indice_de_carga'].get()

    if not (marca and diametro and ancho and tipo and indice_carga):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos de la llanta.")
        return

    try:
        diametro = int(diametro)
        ancho = int(ancho)
        indice_carga = int(indice_carga)
    except ValueError:
        messagebox.showerror("Error de formato", "Diámetro, Ancho e Índice de carga deben ser números.")
        return

    llanta = Llanta(marca, diametro, ancho, tipo, indice_carga)
    info = llanta.obtener_info()
    messagebox.showinfo("Información de la Llanta", info)

def mostrar_velocidad():
    valor = velocidad_entries['valor'].get()
    unidad = velocidad_entries['unidad'].get()
    direccion = velocidad_entries['direccion'].get()
    tiempo = velocidad_entries['tiempo'].get()
    aceleracion = velocidad_entries['aceleracion'].get()

    if not (valor and unidad and direccion and tiempo and aceleracion):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos de velocidad.")
        return

    try:
        valor = float(valor)
        tiempo = float(tiempo)
        aceleracion = float(aceleracion)
    except ValueError:
        messagebox.showerror("Error de formato", "Valor, Tiempo y Aceleración deben ser números.")
        return

    velocidad = Velocidad(valor, unidad, direccion, tiempo, aceleracion)
    info = (
        f"Velocidad: {velocidad.valor} {velocidad.unidad}\n"
        f"Dirección: {velocidad.direccion}\n"
        f"Tiempo: {velocidad.tiempo} s\n"
        f"Aceleración: {velocidad.aceleracion} m/s²"
    )
    messagebox.showinfo("Información de Velocidad", info)

def mostrar_volante():
    material = volante_entries['material'].get()
    diametro = volante_entries['diametro'].get()
    color = volante_entries['color'].get()
    tipo = volante_entries['tipo'].get()
    peso = volante_entries['peso'].get()

    if not (material and diametro and color and tipo and peso):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos del volante.")
        return

    try:
        diametro = float(diametro)
        peso = float(peso)
    except ValueError:
        messagebox.showerror("Error de formato", "Diámetro y Peso deben ser números.")
        return

    volante = Volante(material, diametro, color, tipo, peso)
    info = volante.get_info()
    messagebox.showinfo("Información del Volante", info)

def mostrar_combustible():
    tipo = combustible_entries['tipo'].get()
    octanaje = combustible_entries['octanaje'].get()
    precio = combustible_entries['precio_por_litro'].get()
    proveedor = combustible_entries['proveedor'].get()
    origen = combustible_entries['origen'].get()

    if not (tipo and octanaje and precio and proveedor and origen):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos de combustible.")
        return

    try:
        octanaje = int(octanaje)
        precio = float(precio)
    except ValueError:
        messagebox.showerror("Error de formato", "Octanaje debe ser entero y precio debe ser número decimal.")
        return

    combustible = Combustible(tipo, octanaje, precio, proveedor, origen)
    info = combustible.obtener_info()
    messagebox.showinfo("Información de Combustible", info)

ventana = tk.Tk()
ventana.title("Registro de Componentes del Auto")
ventana.geometry("450x450")

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")

frame_interior = ttk.Frame(notebook)
notebook.add(frame_interior, text="Interior Auto")

interior_labels = ["Marca del Auto:", "Tipo de Asientos:", "Material:", "Color:", "Sistema de Audio:"]
interior_entries = {}

for label_text in interior_labels:
    label = ttk.Label(frame_interior, text=label_text)
    label.pack(pady=3)
    entry = ttk.Entry(frame_interior)
    entry.pack(pady=3, fill='x', padx=20)
    key = label_text.split(":")[0].lower().replace(" ", "_")
    interior_entries[key] = entry

btn_interior = ttk.Button(frame_interior, text="Mostrar información", command=mostrar_interior)
btn_interior.pack(pady=15)

frame_llanta = ttk.Frame(notebook)
notebook.add(frame_llanta, text="Llanta")

llanta_labels = ["Marca:", "Diámetro (pulgadas):", "Ancho (mm):", "Tipo:", "Índice de carga:"]
llanta_entries = {}

for label_text in llanta_labels:
    label = ttk.Label(frame_llanta, text=label_text)
    label.pack(pady=3)
    entry = ttk.Entry(frame_llanta)
    entry.pack(pady=3, fill='x', padx=20)
    key = label_text.split(":")[0].lower().replace(" ", "_").replace("í", "i").replace("í", "i").replace("í", "i")
    if "indice" in key:
        key = "indice_de_carga"
    llanta_entries[key] = entry

btn_llanta = ttk.Button(frame_llanta, text="Mostrar información", command=mostrar_llanta)
btn_llanta.pack(pady=15)

frame_velocidad = ttk.Frame(notebook)
notebook.add(frame_velocidad, text="Velocidad")

velocidad_labels = ["Valor:", "Unidad:", "Dirección:", "Tiempo (s):", "Aceleración (m/s²):"]
velocidad_entries = {}

for label_text in velocidad_labels:
    label = ttk.Label(frame_velocidad, text=label_text)
    label.pack(pady=3)
    entry = ttk.Entry(frame_velocidad)
    entry.pack(pady=3, fill='x', padx=20)
    key = label_text.split(":")[0].lower().replace(" ", "_").replace("(", "").replace(")", "").replace("²", "2")
    velocidad_entries[key] = entry

btn_velocidad = ttk.Button(frame_velocidad, text="Mostrar información", command=mostrar_velocidad)
btn_velocidad.pack(pady=15)

frame_volante = ttk.Frame(notebook)
notebook.add(frame_volante, text="Volante")

volante_labels = ["Material:", "Diámetro (cm):", "Color:", "Tipo:", "Peso (g):"]
volante_entries = {}

for label_text in volante_labels:
    label = ttk.Label(frame_volante, text=label_text)
    label.pack(pady=3)
    entry = ttk.Entry(frame_volante)
    entry.pack(pady=3, fill='x', padx=20)
    key = label_text.split(":")[0].lower().replace(" ", "_").replace("(", "").replace(")", "").replace("²", "2")
    volante_entries[key] = entry

btn_volante = ttk.Button(frame_volante, text="Mostrar información", command=mostrar_volante)
btn_volante.pack(pady=15)

frame_combustible = ttk.Frame(notebook)
notebook.add(frame_combustible, text="Combustible")

combustible_labels = ["Tipo:", "Octanaje:", "Precio por litro:", "Proveedor:", "Origen:"]
combustible_entries = {}

for label_text in combustible_labels:
    label = ttk.Label(frame_combustible, text=label_text)
    label.grid(row=combustible_labels.index(label_text), column=0, sticky="w", padx=10, pady=5)
    entry = ttk.Entry(frame_combustible)
    entry.grid(row=combustible_labels.index(label_text), column=1, padx=10, pady=5, sticky="ew")
    key = label_text.split(":")[0].lower().replace(" ", "_")
    combustible_entries[key] = entry

frame_combustible.columnconfigure(1, weight=1)

btn_combustible = ttk.Button(frame_combustible, text="Mostrar información", command=mostrar_combustible)
btn_combustible.grid(row=len(combustible_labels), column=0, columnspan=2, pady=15)

ventana.mainloop()
