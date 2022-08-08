import sqlite3

conexion = sqlite3.connect('SQLITE3\ejemplo.db')

# Creacion del cursor
cursor = conexion.cursor()

usuarios = [
    ('juan.perez@gmail.com', 'Gestion', 'Juan', 39),
    ('fer.mino@gmail.com', 'Administracion', 'Fernando', 29),
    ('hugo.almada@hotmail.com', 'Chef', 'Hugo', 43)
]

# Inserción de registros
cursor.executemany(
    "INSERT INTO estudiantes VALUES (?,?,?,?)", usuarios)
conexion.commit()

conexion.close()
