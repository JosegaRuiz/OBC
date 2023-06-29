paises_input = input("Ingrese una lista de países separados por comas: ")
paises_lista = paises_input.split(",")
paises_set = set(paises_lista)
paises_ordenados = sorted(list(paises_set))

print("Países ordenados alfabéticamente:")
print(", ".join(paises_ordenados))
