#------------------------------------------------#
#    ANALISIS DE DATOS EN BASE A UN CSV QUE      #
#  CONTIENE INFORMACIÓN DE ACCIONES DE DOW JONES #
#------------------------------------------------#
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# leo el CSV

df_crudo = pd.read_csv(r'dow_jones_index.data')
print(df_crudo)

# El parámetro _converters_ de la función `pd.read_csv()`
# nos permite aplicar una operación en las columnas.

columnas = ['accion', 'fecha', 'precio']

df = pd.read_csv(r'dow_jones_index.data',
                 usecols=[1, 2, 6],
                 header=0,
                 names=columnas,
                 parse_dates=['fecha'],
                 converters={'precio':
                             lambda x:
                             float(x.replace('$', ''))
                             }
                 )

print(df)

# Qué período en el tiempo representan los datos?
# Los datos pertenecen al año 2011

print(df.fecha.dt.year.value_counts())

# Meses con información - nro de mes

print(df.fecha.dt.month.value_counts())

# Meses con información - nombre del mes

print(df.fecha.dt.month_name().value_counts())

# Los datos se distribuyen desde Enero a Junio del 2011: _Primer semestre del año.
# En el mes de Abril hay 30 registros más que en el resto de los meses: _¿Por qué?.

df['mes'] = df.fecha.dt.month_name()

filtro1 = df['mes'] == 'April'

filtro2 = df['mes'] == 'May'

# En Abril las acciones cotizaron 5 veces porque el mes tuvo 5 semanas.

print(df[filtro1].groupby('accion')['mes'].value_counts())

print(df[filtro2].groupby('accion')['mes'].value_counts())

# ¿Cuáles acciones en promedio tuvieron la mayor y la menor cotización?

# En promedio IBM tuvo el mayor precio: 163,10 USD
# En promedio BAC tuvo el menor precio: 13,05 USD

print(df.groupby('accion').agg({'precio': [np.mean, np.std]}))

print(df.groupby('accion').agg({'precio': [np.mean, np.std]}).sort_values(
    [('precio', 'mean')], ascending=False))

# ¿Cuáles acciones tuvieron la mayor y menor variación de precio?

# CAT es la acción más volátil, con una desviación tipica de 6,22 USD
# AA es la acción más consistente, con una desviación típica de 0,77 USD

print(df.groupby('accion').agg({'precio': [np.mean, np.std]}).sort_values(
    [('precio', 'std')], ascending=False))


# Ya que conocemos la acción más volátil, podemos preguntarnos si el precio de
# esta acción tiene correlación con el precio de otras acciones.

# Deseamos estudiar una o varias acciones particulares pero el conjunto de
# datos no presenta un formato conveniente para esto.

# La función `df.pivot_table()` nos genera un nuevo `DataFrame` reorganizado
# con la forma que deseemos.

df_nuevo = df.pivot_table(index='fecha',
                          columns='accion',
                          values='precio')
print(df_nuevo)

# Ahora podemos centrarnos en estudiar el comportamiento en el tiempo de cada acción.

fig, (pan1, pan2) = plt.subplots(2, 1, sharex=True, constrained_layout=True)

pan1.plot(df_nuevo.index, df_nuevo.CAT,
          color='blue',
          marker='o',
          linestyle='solid',
          label='CAT')


pan2.plot(df_nuevo.index, df_nuevo.AA,
          color='orange',
          marker='v',
          linestyle='solid',
          label='AA')


for pan in fig.get_axes():
    pan.set(xlabel='Fecha',
            ylabel='Dólares americanos.',
            title='Precio de la acción (al cierre).')

print(pan1.legend())
print(pan2.legend())

# Los precios de ambas acciones presentan un comportamiento alcista hasta
# Abril -con un ligero declive en las primeras semanas de Marzo-,
# a partir de ahí el precio baja hasta la última semana de Junio.

# ¿Existe alguna correlación entre los precios de CAT y el resto de las acciones?

df_nuevo.corr()
df_nuevo.corr().loc['CAT']
df_nuevo.corr().loc['CAT'][df_nuevo.corr().loc['CAT'] > 0.8]

corr_pos = df_nuevo.corr().loc['CAT'][df_nuevo.corr(
).loc['CAT'] > 0.8].sort_values(ascending=False)
print(corr_pos)

# Las acciones DD, VZ, CVX, MMM, XOM presentan una fuerte correlación positiva con CAT.


valores = corr_pos[1:5]

plt.bar(valores.index, valores.values, color='forestgreen')

plt.plot()

plt.xlabel("Acciones")

plt.ylabel("Coeficiente de correlación.")

plt.title('Correlación entre CAT y el resto.')

plt.show()

corr_neg = df_nuevo.corr().loc['CAT'][df_nuevo.corr(
).loc['CAT'] < 0].sort_values(ascending=True)
corr_neg

valores = corr_neg[1:5]

plt.bar(valores.index, valores.values, color='brown')

plt.plot()

plt.xlabel("Acciones")

plt.ylabel("Coeficiente de correlación.")

plt.title('Correlación entre CAT y el resto.')

plt.show()

# Ninguna acción presenta una correlación negativa significante con CAT.

# %%
