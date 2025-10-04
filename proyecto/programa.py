#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
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