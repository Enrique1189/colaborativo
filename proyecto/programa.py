import tkinter as tk
from gato import Gato
from aguila import Aguila
from leon import Leon
from tigre import Tigre
from lobo import Lobo

def menu_principal():
    root = tk.Tk()
    root.title("Menú de Animales")
    root.geometry("300x450")

    tk.Label(root, text="Selecciona un animal:", font=("Arial", 14)).pack(pady=20)

    botones = [
        ("Gato", Gato),
        ("Águila", Aguila),
        ("León", Leon),
        ("Tigre", Tigre),
        ("Lobo", Lobo)
    ]

    for texto, clase in botones:
        tk.Button(root, text=texto, width=20, command=clase).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    menu_principal()
