import sqlite3
import csv

conexion = sqlite3.connect('SQLITE3\ejemplo.db')

# Creacion del cursor
cursor = conexion.cursor()

archivo = open('SQLITE3\datos_db.txt')

filas = csv.reader(archivo)

# Inserción de registros
cursor.executemany(
    "INSERT INTO estudiantes VALUES (?,?,?,?)", filas)

# Seleccion de registros
cursor.execute(
    "SELECT * from estudiantes")
print(cursor.fetchall())

conexion.commit()

conexion.close()
