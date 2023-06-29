# Crear un archivo de texto
archivo_txt = open("miarchivo.txt", "w")

# Abrir el archivo para escribir en él
with open("miarchivo.txt", "w") as archivo:
    # Escribir en el archivo
    archivo.write("Este es el contenido del archivo.")

# Abrir el archivo para leerlo
with open("miarchivo.txt", "r") as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()
    print(contenido)
