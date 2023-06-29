import tkinter as tk

def seleccionar_opcion():
    seleccion = seleccion_var.get()
    mensaje.config(text="Opción seleccionada: " + seleccion)

def reiniciar_seleccion():
    seleccion_var.set(None)
    mensaje.config(text="Opción seleccionada: ")

ventana = tk.Tk()
ventana.title("Lista de RadioButton")

seleccion_var = tk.StringVar()

opciones = ["Opción 1", "Opción 2", "Opción 3"]

for opcion in opciones:
    radio_btn = tk.Radiobutton(ventana, text=opcion, variable=seleccion_var, value=opcion)
    radio_btn.pack(anchor=tk.W)
seleccion_var.set(None)

boton_mostrar = tk.Button(ventana, text="Mostrar selección", command=seleccionar_opcion)
boton_mostrar.pack(anchor=tk.W)

boton_reiniciar = tk.Button(ventana, text="Reiniciar selección", command=reiniciar_seleccion)
boton_reiniciar.pack(anchor=tk.W)

mensaje = tk.Label(ventana, text="Opción seleccionada: ")
mensaje.pack(anchor=tk.W)

ventana.mainloop()
