import tkinter as tk

def mostrar_seleccion():
    seleccion = lista.curselection()
    if seleccion:
        indice = seleccion[0]
        elemento = lista.get(indice)
        etiqueta.config(text="Elemento seleccionado: " + elemento)
    else:
        etiqueta.config(text="Ningún elemento seleccionado")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz sencilla")

# Crear la lista de elementos seleccionables
elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
lista = tk.Listbox(ventana, selectmode=tk.SINGLE)
for elemento in elementos:
    lista.insert(tk.END, elemento)
lista.pack()

# Crear el label para mostrar la selección
etiqueta = tk.Label(ventana, text="Ningún elemento seleccionado")
etiqueta.pack()

# Crear el botón para mostrar la selección
boton_mostrar = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
boton_mostrar.pack()

# Iniciar la ventana
ventana.mainloop()
