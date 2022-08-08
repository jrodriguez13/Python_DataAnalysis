import sqlite3

conexion = sqlite3.connect('SQLITE3\ejemplo.db')

# Creacion del cursor
cursor = conexion.cursor()

# Inserción de registros
cursor.execute(
    "INSERT INTO estudiantes VALUES ('cjrodriguez.ar@gmail.com','Programacion','Javier',36)")
conexion.commit()

conexion.close()
