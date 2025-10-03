import tkinter as tk


class Velocidad:
    def __init__(self, valor, unidad, direccion, tiempo, aceleracion):
        self.valor = valor
        self.unidad = unidad
        self.direccion = direccion
        self.tiempo = tiempo
        self.aceleracion = aceleracion

def mostrar_info():
    info_label.config(text=(
        f"Velocidad: {mi_velocidad.valor} {mi_velocidad.unidad}\n"
        f"Dirección: {mi_velocidad.direccion}\n"
        f"Tiempo: {mi_velocidad.tiempo} s\n"
        f"Aceleración: {mi_velocidad.aceleracion} m/s²"
    ))

mi_velocidad = Velocidad(60, "km/h", "Norte", 10, 2)

ventana = tk.Tk()
ventana.title("Información de Velocidad")
ventana.geometry("400x250")
ventana.config(bg="#f0f0f0")

titulo_label = tk.Label(ventana, text="Datos de la Velocidad", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo_label.pack(pady=10)

mostrar_btn = tk.Button(ventana, text="Mostrar Información", font=("Arial", 12), bg="#4CAF50", fg="white", command=mostrar_info)
mostrar_btn.pack(pady=10)

info_label = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f0f0", justify="left")
info_label.pack(pady=10)

ventana.mainloop()
