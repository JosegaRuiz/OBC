from functools import reduce

# Función para filtrar los elementos impares
def filtrar_impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))

# Función para realizar la suma de los elementos
def sumar_elementos(lista):
    return reduce(lambda x, y: x + y, lista)

# Lista de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener los elementos impares
impares = filtrar_impares(numeros)

# Realizar la suma de los elementos impares
suma_impares = sumar_elementos(impares)

# Mostrar el resultado por consola
print("Elementos impares:", impares)
print("Suma de elementos impares:", suma_impares)
