import pickle

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

vehiculo = Vehiculo("Toyota", "Corolla")

with open("vehiculo.bin", "wb") as archivo:
    pickle.dump(vehiculo, archivo)

with open("vehiculo.bin", "rb") as archivo:
    vehiculo_cargado = pickle.load(archivo)

print("Marca:", vehiculo_cargado.marca)
print("Modelo:", vehiculo_cargado.modelo)
