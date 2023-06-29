class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
    
    def resultado_aprobado(self):
        if self.nota >= 5:
            print("¡Felicidades! El alumno ha aprobado.")
        else:
            print("El alumno no ha aprobado.")

alumno1 = Alumno("Antonio", 8.5)
alumno1.imprimir_informacion()
alumno1.resultado_aprobado()
