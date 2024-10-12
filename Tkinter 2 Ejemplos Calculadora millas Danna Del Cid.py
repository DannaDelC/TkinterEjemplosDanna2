import tkinter as tk

def convertir():
    try:
        millas = float(entry_millas.get())
        km = millas * 1.609344
        label_resultado.config(text=f"{millas} millas son {km:.2f} kilometros.")
    except ValueError:
        label_resultado.config(text="Por favor, introduce un número válido.")


root = tk.Tk()
root.title("Calculadora de Millas a Kilometros: ")
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label_instrucciones = tk.Label(frame, text="Introduce la cantidad de millas:")
label_instrucciones.grid(row=0, column=0, sticky="w")

entry_millas = tk.Entry(frame)
entry_millas.grid(row=0, column=1)

button_convertir = tk.Button(frame, text="Convertir", command=convertir)
button_convertir.grid(row=1, columnspan=2, pady=10)

label_resultado = tk.Label(frame, text="")
label_resultado.grid(row=2, columnspan=2)

root.mainloop()
