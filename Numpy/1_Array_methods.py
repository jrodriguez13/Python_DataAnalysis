import numpy as np
from pandas import array

arreglo = np.array([0, 1, 2, 3, 4, 5])

print(arreglo, type(arreglo))

notas = [10, 9, 6, 4, 8]

ar_notas = np.array(notas, dtype=float)

print(notas, type(ar_notas[0]))

ar_notas_todas = np.array(([1, 2, 4, 7, 9], ar_notas))

# ndim devuelve la cantidad de dimensiones del array
# shape devuelve la cantidad de elementos de un array, en el ejemplo son 2 filas y 5 columnas
print(ar_notas_todas, ar_notas_todas.ndim, ar_notas_todas.shape)

# el metodo zeros genera un array de x filas e y columnas con todos ceros
arr = np.zeros((2, 4), dtype=float)
print(arr)

# el metodo zeros genera un array de x filas e y columnas con todos unos
arr2 = np.ones((5, 5), dtype=float)
print(arr2)

# el metodo identity genra una matriz de identidad
# Una matriz identidad o unidad de orden n es una matriz cuadrada donde
# todos sus elementos son ceros (0) menos los elementos de la diagonal principal que son unos (1).
arr3 = np.identity((4), dtype=float)
print(arr3)

# el metodo arange genera un array con los N elementos informados por argumento
arr4 = np.arange(1, 9)
print(arr4)
