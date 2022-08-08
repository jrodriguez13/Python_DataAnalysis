from operator import index
import numpy as np
import pandas as pd
import datetime


# ---------- ** DATAFRAMES ** --------------

data = {
    'ciudades': ['Caracas', 'Guadalajara', 'La Habana', 'Cancun', 'Maracaibo'],
    'poblacion': [100000, 200000, 3400000, 45000, 560000],
    'infectados': [6000, 4000, 5000, 12000, 5000]
}

df = pd.DataFrame(data)
print(df)

# operaciones con data frames ***

d = [np.random.randint(50, size=10)]
print(d)

# transposicion
df = pd.DataFrame(d).T
print(df)

# añadir columna
df['experiencia'] = 5
print(df)

# agregar columna desde un ciclo
df['perdidas'] = [(i+2)*np.e for i in range(10)]
print(df)

# agregar columna desde una ya existente
df['multi'] = df['perdidas']*100
print(df)

# cambiar nombre a columnas
df.columns = ['codigo_id', 'años_exp', 'eficiencia', 'eficiencia_agregada']
print(df)

# modificar valores de columnas
df['eficiencia'] = df['eficiencia'] / 200
print(df)

# eliminar una columna
del df['eficiencia']
print(df)

# Modificar el indice

i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df.index = i

print(df)

# ******** INDEXACION Y FILTRADO *********

df = pd.DataFrame(
    np.random.randint(low=0, high=10, size=(10, 2)),
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    columns=["Cod_empleado", "Calificacion"]
)

print(df)

# loc selecciona un registro

print(df.loc['a'])
print(df.loc['a': 'g'])

# fechas

fechas_inicio = pd.date_range(start='24/4/2020', end='24/5/2020', freq='D')
fechas_inicio

fechas_fin = pd.date_range(start='24/5/2020', end='24/6/2020', freq='D')
fechas_fin

lista_equis = []

for i in range(15):
    lista_equis.append(np.random.randint(2))


df = pd.DataFrame()

df['Inicio_campaña'] = fechas_inicio[:15]
df['Fin_campaña'] = fechas_fin[:15]
df['Target'] = lista_equis
df['Día de inicio'] = df['Inicio_campaña'].dt.day
df['Mes de inicio'] = df['Inicio_campaña'].dt.month
df['Año de inicio'] = df['Inicio_campaña'].dt.year
df['Hora_inicio'] = df['Inicio_campaña'].dt.hour
df['Minuto_inicio'] = df['Inicio_campaña'].dt.minute
df['Segundo_inicio'] = df['Inicio_campaña'].dt.second
df['Nombre del día de inicio'] = df['Inicio_campaña'].dt.weekday
df['Semana del año de inicio'] = df['Inicio_campaña'].dt.isocalendar().week
df['Duración'] = df['Fin_campaña']-df['Inicio_campaña']

print(df)

# Manejo de datos ausentes (null)

df = pd.DataFrame({
    'VarA': ['aa', None, 'cc'],
    'VarB': [20, 30, None],
    'VarC': [1234, 3456, 6789]
},
    index=['Caso1', 'Caso2', 'Caso3']
)

print(pd.isnull(df))
