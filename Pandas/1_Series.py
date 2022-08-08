from operator import index
import numpy as np
import pandas as pd

serie = pd.Series([1979, 1980, 1981, 1982])
print(serie)
print(serie.index)
print(serie.values)

# asignar un index

serie = pd.Series([1979, 1980, 1981, 1982], index=[
                  'roberto', 'hernan', 'juan', 'javier'])
print(serie)

# serie a partir de un diccionario
dicc1 = {'Cuadrado de {}'.format(i): i*i for i in range(11)}
print(dicc1)

serie_dic = pd.Series(dicc1)
print(serie_dic)

