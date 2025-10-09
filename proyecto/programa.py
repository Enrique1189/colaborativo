import tkinter as tk
from aguila import Aguila
from gato import Gato
from leon import Leon
from tigre import Tigre
from lobo import Lobo



def mostrar_ventana(titulo, texto):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("400x300")
    label = tk.Label(ventana, text=texto, font=("Arial", 12), justify="left")
    label.pack(padx=10, pady=10)

def mostrar_aguila():
    aguila1 = Aguila("Águila Real", 5, 220, 160, "Montañas")
    mostrar_ventana("Águila", aguila1.mostrar_info())

def mostrar_gato():
    gato1 = Gato("Michi", "Blanco", 3, "Siames", "Miau")
    mostrar_ventana("Gato", gato1.mostrar_datos())

def mostrar_leon():
    leon1 = Leon("Simba", 5, 190, "Sabana", "Dorado")
    mostrar_ventana("León", leon1.obtener_info())

def mostrar_tigre():
    tigre1 = Tigre("Rajah", "Bengala", 6, 220, 110, "Naranja con rayas negras")
    mostrar_ventana("Tigre", tigre1.mostrar_info())

def mostrar_lobo():
    lobo1 = Lobo("Fang", 4, "Gris", "Mediano", 50)
    mostrar_ventana("Lobo", lobo1.describir())

def menu_principal():
    root = tk.Tk()
    root.title("Menú de Animales")
    root.geometry("300x300")

    tk.Label(root, text="Selecciona un animal:", font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="Águila", width=20, command=mostrar_aguila).pack(pady=5)
    tk.Button(root, text="Gato", width=20, command=mostrar_gato).pack(pady=5)
    tk.Button(root, text="León", width=20, command=mostrar_leon).pack(pady=5)
    tk.Button(root, text="Tigre", width=20, command=mostrar_tigre).pack(pady=5)
    tk.Button(root, text="Lobo", width=20, command=mostrar_lobo).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    menu_principal()


def mostrar_ventana(titulo, texto):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("400x300")
    label = tk.Label(ventana, text=texto, font=("Arial", 12), justify="left")
    label.pack(padx=10, pady=10)

def mostrar_aguila():
    aguila1 = Aguila("Águila Real", 5, 220, 160, "Montañas")
    mostrar_ventana("Águila", aguila1.mostrar_info())

def mostrar_gato():
    gato1 = Gato("Michi", "Blanco", 3, "Siames", "Miau")
    mostrar_ventana("Gato", gato1.mostrar_datos())

def mostrar_leon():
    leon1 = Leon("Simba", 5, 190, "Sabana", "Dorado")
    mostrar_ventana("León", leon1.obtener_info())

def mostrar_tigre():
    tigre1 = Tigre("Rajah", "Bengala", 6, 220, 110, "Naranja con rayas negras")
    mostrar_ventana("Tigre", tigre1.mostrar_info())

def mostrar_lobo():
    lobo1 = Lobo("Fang", 4, "Gris", "Mediano", 50)
    mostrar_ventana("Lobo", lobo1.describir())

def menu_principal():
    root = tk.Tk()
    root.title("Menú de Animales")
    root.geometry("300x300")

    tk.Label(root, text="Selecciona un animal:", font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="Águila", width=20, command=mostrar_aguila).pack(pady=5)
    tk.Button(root, text="Gato", width=20, command=mostrar_gato).pack(pady=5)
    tk.Button(root, text="León", width=20, command=mostrar_leon).pack(pady=5)
    tk.Button(root, text="Tigre", width=20, command=mostrar_tigre).pack(pady=5)
    tk.Button(root, text="Lobo", width=20, command=mostrar_lobo).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    menu_principal()
