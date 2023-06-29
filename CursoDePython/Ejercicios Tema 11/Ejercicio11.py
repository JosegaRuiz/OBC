import sqlite3

# Crear la conexión a la base de datos
conexion = sqlite3.connect('alumnos.db')
cursor = conexion.cursor()

# Crear la tabla Alumnos
cursor.execute('''CREATE TABLE IF NOT EXISTS Alumnos
                  (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)''')

# Insertar datos en la tabla Alumnos
datos_alumnos = [
    (1, 'Juan', 'Pérez'),
    (2, 'María', 'García'),
    (3, 'Pedro', 'López'),
    (4, 'Ana', 'Martínez'),
    (5, 'Carlos', 'Rodríguez'),
    (6, 'Laura', 'Sánchez'),
    (7, 'David', 'Fernández'),
    (8, 'Sofía', 'Gómez')
]
cursor.executemany('INSERT INTO Alumnos VALUES (?, ?, ?)', datos_alumnos)

# Realizar búsqueda por nombre
nombre_buscar = 'María'
cursor.execute('SELECT * FROM Alumnos WHERE nombre=?', (nombre_buscar,))
resultado = cursor.fetchone()

# Mostrar los datos por consola
if resultado:
    id_alumno, nombre, apellido = resultado
    print(f'Datos del alumno con nombre "{nombre_buscar}":')
    print(f'ID: {id_alumno}')
    print(f'Nombre: {nombre}')
    print(f'Apellido: {apellido}')
else:
    print(f'No se encontró ningún alumno con nombre "{nombre_buscar}".')

# Cerrar la conexión a la base de datos
conexion.close()
