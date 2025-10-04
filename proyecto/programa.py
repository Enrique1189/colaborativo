#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas

elif animal == "Hamster":
            nombre = entradas["Nombre"].get()
            raza = entradas["Raza"].get()
            peso = float(entradas["Peso (kg)"].get())
            altura = float(entradas["Altura (cm)"].get())
            sintomas = entradas["Síntomas"].get()

            mascota = Hamster(nombre, raza, peso, altura, sintomas)

            salida.insert(tk.END, f"Hamster: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Raza: {mascota.raza}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} kg\n")
            salida.insert(tk.END, f"- Altura: {mascota.altura} cm\n")
            salida.insert(tk.END, f"- Síntomas: {mascota.sintomas}\n")

        elif animal == "Pájaro":
            nombre = entradas["Nombre"].get()
            tipo = entradas["Tipo"].get()
            peso = float(entradas["Peso (kg)"].get())
            altura = float(entradas["Altura (cm)"].get())
            sintomas = entradas["Síntomas"].get()

            mascota = Pajaro(nombre, tipo, peso, altura, sintomas)

            salida.insert(tk.END, f"Pájaro: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Tipo: {mascota.tipo}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} kg\n")
            salida.insert(tk.END, f"- Altura: {mascota.altura} cm\n")
            salida.insert(tk.END, f"- Síntomas: {mascota.sintomas}\n")

        elif animal == "Perro":
            nombre = entradas["Nombre"].get()
            raza = entradas["Raza"].get()
            peso = float(entradas["Peso (kg)"].get())
            altura = float(entradas["Altura (cm)"].get())
            sintomas = [s.strip() for s in entradas["Síntomas (separar con coma)"].get().split(",")]

            mascota = Perro(nombre, raza, peso, altura, sintomas)

            salida.insert(tk.END, f"Perro: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Raza: {mascota.raza}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} kg\n")
            salida.insert(tk.END, f"- Altura: {mascota.altura} cm\n")
            salida.insert(tk.END, f"- Síntomas: {', '.join(mascota.sintomas)}\n")
            for e in mascota.evaluar_salud():
                salida.insert(tk.END, f"- {e}\n")
