#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
import tkinter as tk

from clases.bebida import Bebida
from clases.helado import Helado
from clases.taco import Taco
from clases.hamburguesa import Hamburguesa
from clases.pizza import Pizza

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Clases - Solo Botones")
ventana.geometry("700x500")

# Área de texto para mostrar resultados
texto_resultado = tk.Text(ventana, height=22, width=85)
texto_resultado.place(x=10, y=130)

# Funciones para mostrar objetos fijos y su info

def mostrar_bebida():
    bebida = Bebida("Coca-Cola", "Refresco", "Grande", "Fría", 25.0)
    texto = (
        f"{bebida.mostrar()}\n"
        f"Preparación: {bebida.prepara()}\n"
        f"Toma: {bebida.tomar()}\n"
        f"{bebida.aplicar_descuento(10)}\n"
    )
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, texto)

def mostrar_helado():
    helado = Helado("Chocolate", 50, "Mediano", "Cono", "Leche")
    helado.elegir_topping("Chispas de chocolate")
    precio_final = helado.calcular_precio_final()
    texto = (
        f"Sabor: {helado.sabor}\n"
        f"Precio base: ${helado.precio}\n"
        f"Tamaño: {helado.tamaño}\n"
        f"Presentación: {helado.presentacion}\n"
        f"Tipo de líquido: {helado.tipo_liquido}\n"
        f"Topping: {helado.topping}\n"
        f"Precio final calculado: ${precio_final}\n"
    )
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, texto)

def mostrar_taco():
    taco = Taco("Pastor", "Verde", "Pequeño", "Maíz", "Sí")
    taco.agregar_ingrediente("Cebolla")
    taco.agregar_ingrediente("Cilantro")
    ingredientes = ", ".join(taco.ingredientes)
    texto = (
        f"Tipo: {taco.tipo}\n"
        f"Salsa: {taco.salsa}\n"
        f"Tamaño: {taco.tamaño}\n"
        f"Tortilla: {taco.tortilla}\n"
        f"Picante: {taco.picante}\n"
        f"Ingredientes: {ingredientes}\n"
    )
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, texto)

def mostrar_hamburguesa():
    hamburguesa = Hamburguesa(
        nombre="Clásica",
        tamaño="Grande",
        pan="Ajonjolí",
        carne="Res",
        aderezos="Mayonesa, Ketchup",
        queso="Cheddar",
        complementos="Lechuga, Tomate",
        cantidad=4
    )
    texto = (
        f"Nombre: {hamburguesa.nombre}\n"
        f"Tamaño: {hamburguesa.tamaño}\n"
        f"Pan: {hamburguesa.pan}\n"
        f"Carne: {hamburguesa.carne}\n"
        f"Aderezos: {hamburguesa.aderezos}\n"
        f"Queso: {hamburguesa.queso}\n"
        f"Complementos: {hamburguesa.complementos}\n"
        f"Cantidad: {hamburguesa.cantidad}\n"
        f"{hamburguesa.preparar()}\n"
        f"{hamburguesa.descuento()}\n"
        f"{hamburguesa.vender()}\n"
        f"{hamburguesa.comer()}\n"
    )
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, texto)

def mostrar_pizza():
    pizza_obj = Pizza(
        tamaño="Mediana",
        masa="Delgada",
        salsa="Tomate",
        ingredientes=["Queso", "Pepperoni", "Champiñones"],
        precio=150.0
    )
    ingredientes_str = ", ".join(pizza_obj.ingredientes)
    texto = (
        f"Tamaño: {pizza_obj.tamaño}\n"
        f"Masa: {pizza_obj.masa}\n"
        f"Salsa: {pizza_obj.salsa}\n"
        f"Ingredientes: {ingredientes_str}\n"
        f"Precio: ${pizza_obj.precio}\n"
        f"Acciones:\n"
        f" - Agregar ingrediente: Se agrego un ingrediente a la pizza.\n"
        f" - Calcular precio: El precio de la pizza es: {pizza_obj.precio}\n"
        f" - Hornear: La pizza se esta horneando...\n"
    )
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, texto)

# Crear botones
tk.Button(ventana, text="Mostrar Bebida", command=mostrar_bebida).place(x=30, y=50, width=120)
tk.Button(ventana, text="Mostrar Helado", command=mostrar_helado).place(x=170, y=50, width=120)
tk.Button(ventana, text="Mostrar Taco", command=mostrar_taco).place(x=310, y=50, width=120)
tk.Button(ventana, text="Mostrar Hamburguesa", command=mostrar_hamburguesa).place(x=450, y=50, width=130)
tk.Button(ventana, text="Mostrar Pizza", command=mostrar_pizza).place(x=600, y=50, width=90)

ventana.mainloop()
