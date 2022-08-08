import sqlite3

conexion = sqlite3.connect('SQLITE3\ejemplo.db')

# Creacion del cursor
cursor = conexion.cursor()

# Creacion de tabla Estudiantes
cursor.execute(
    "CREATE TABLE estudiantes (email VARCHAR(100), carrera VARCHAR(100), nombre VARCHAR(100), edad INTEGER)")

conexion.close()
