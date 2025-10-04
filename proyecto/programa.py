#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
<<<<<<< HEAD
elif animal == "Ratita":
            nombre = entradas["Nombre"].get()
            peso = int(entradas["Peso (gramos)"].get())
            edad = int(entradas["Edad (meses)"].get())
            sintomas = entradas["Síntomas"].get()
            actividad = entradas["Actividad"].get()

            mascota = Ratita(nombre, peso, edad, sintomas, actividad)

            salida.insert(tk.END, f"Ratita: {mascota.nombre}\n")
            salida.insert(tk.END, f"- Peso: {mascota.peso} gramos\n")
            salida.insert(tk.END, f"- Edad: {mascota.edad} meses\n")
            salida.insert(tk.END, f"- Síntomas: {mascota.sintomas}\n")
            salida.insert(tk.END, f"- Actividad: {mascota.actividad}\n")
            for r in mascota.evaluar_salud():
                salida.insert(tk.END, f"- {r}\n")

        else:
            salida.insert(tk.END, "Por favor, selecciona un animal válido.\n")

    except ValueError as ve:
        messagebox.showerror("Error de entrada", f"Por favor, verifica los datos ingresados.\n{ve}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
=======

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
>>>>>>> bd1ecda7de574f2bd0ae31ac43dd543a37077d5d
