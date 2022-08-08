import sqlite3

conexion = sqlite3.connect('SQLITE3\ejemplo.db')

# Creacion del cursor
cursor = conexion.cursor()

# Seleccion de registros
cursor.execute(
    "SELECT * from estudiantes")

usuarios = cursor.fetchone()
print(usuarios)

conexion.close()
