import numpy as np
from pandas import array

# arr = np.arange(1,9)
# print(arr)

# #shape transforma el array del 1 al 8 en dos array de 1 a 4 y de 5 a 8
# arr.shape = (2,4)
# print(arr)

# suma el array, creando un array nuevo con cada elemento sumado entre si
# 1+1=2 2+2=4 etc
arr = np.arange(1, 9)
arr_sum = arr + arr
print(arr_sum)

# resta el array, creando un array nuevo con cada elemento restado
# entre si (por ende se generan un array de ceros)
# 1-1=0 2-2=0 etc
arr = np.arange(1, 9)
arr_sub = arr - arr
print(arr_sub)

# multiplica el array, creando un array nuevo con cada elemento multiplicado entre si
# 1*1=1 2*2=4 3*3=9 4*4=16 etc
arr = np.arange(1, 9)
arr_mul = arr * arr
print(arr_mul)

# se realiza exponenciacion del array, creando un array nuevo con cada elemento
# elevado a la potencia del mismo
# 1**1=1 2**2=4 3**3=27 etc
arr = np.arange(1, 9)
arr_pot = arr ** arr
print(arr_pot)

# divide el array, creando un array nuevo con cada elemento dividido entre si (array de unos)
# 1/1=1 2/2=1 3/3=1 4/4=1 etc
arr = np.arange(1, 9)
arr_div = arr / arr
print(arr_div)

# El metodo dot devuelve el producto escalar de dos array
a = np.array([1, 2, 3], float)
b = np.array([0, 1, 1], float)

print(np.dot(b, a))

# dot puede usarse tambien para realizar el producto escalar de dos matrices, aunque no es recomendable
# para multiplicar matrices se utiliza '@'
m1 = np.array([[5, 2], [4, 8]], float)
m2 = np.array([[2, 4], [5, 3]], float)

print(np.dot(m1, m2))

print(m1@m2)

# determinante de una matriz
# El determinante de una matriz cuadrada —matriz con el mismo número de filas que de
# columnas— se obtiene de restar la multiplicación de los elementos de la diagonal principal
# de la matriz y la multiplicación de los elementos de la diagonal secundaria de la misma matriz.

m3 = np.array([[8, 5], [3, 4]], float)

print(np.linalg.det(m3))


# ---------------** FUNCIONES UNARIAS **-------------

# sqrt devuelve la riz cuadrada de cada elemento de un array
arr = np.array([2, 4, 9], float)

print(np.sqrt(arr))

# exp eleva el numero de Euler al exponente de cada valor del array
# e**2 e**4 e**9

print(np.exp(arr))

# log eleva cada valor del array al logaritmo natural

print(np.log(arr))

# seno, coseno y tangente

print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))

# promedio

print(np.mean(arr))

# variacion estandar

print(np.std(arr))

# varianza

print(np.var(arr))

# ---------------** FUNCIONES BINARIAS **-------------

# sqrt devuelve la riz cuadrada de cada elemento de un array
arr_1 = np.array([5, 36, 17, 18, 9], float)
arr_2 = np.array([8, 24, 17, 19, 9], float)

# Suma los elementos de los dos array
print(np.add(arr_1, arr_2))

# Resta los elementos de los dos array
print(np.subtract(arr_1, arr_2))

# Multiplica los elementos de los dos array
print(np.multiply(arr_1, arr_2))

# Divide los elementos de los dos array
print(np.divide(arr_1, arr_2))

# Devuelve un booleano si los dos arrays son iguales (TRUE-FALSE)
print(np.array_equal(arr_1, arr_2))

# Devuelve un array eligiendo el menor entre cada elemento de los array
print(np.fmin(arr_1, arr_2))

# Devuelve un array eligiendo el mayor entre cada elemento de los array
print(np.fmax(arr_1, arr_2))

# ----------------- ** AGREGAR O QUITAR VALORES ** ------------------------

# genera un array siendo el primer argumento el desde, el segundo el hasta
# y el tercero cuandos nros se saltea
arr_x = np.arange(0, 20, 2)
print(arr_x)

# genera un array con numeros aleatorios
arr_x = np.random.rand(4, 3)
print(arr_x)

# genera un array con numeros aleatorios ENTEROS
# recibe como parametro el limite y el tamaño
arr_x = np.random.randint(10, size=(2, 3))
print(arr_x)

# genera un arreglo con el mismo valor para todos los elementos
arr_x = np.full((3, 3), 6)
print(arr_x)

# agrega elementos al final del array
arr_z = np.arange(0, 20, 2)
arr_z = np.append(arr_z, [12, 13, 14, 51])
print(arr_z)

# inserta elementos desde una posicion del array indicada por parametro
arr_w = np.arange(0, 20, 2)
arr_w = np.insert(arr_w, 2, [25, 69])
print(arr_w)

# elimina elementos desde una posicion del array indicada por parametro
print(arr_z)
arr_z = np.delete(arr_z, 1, axis=0)
print(arr_z)


# ------------------ ** TRANSFORMAR DATOS ** -----------------------

# transformar el tipo de dato del array
arr_ent = np.random.randint(100, size=(3, 4))
arr_ent.astype(float)
print(arr_ent)

# ordena el array horizontalmente
arr_ent.sort()
print(arr_ent)

# ordena el array verticalmente
arr_ent.sort(axis=0)
print(arr_ent)

# modificar las dimensiones de un array (deben ser la misma cantidad de elementos)
arr_dim = arr_ent.reshape(6, 2)
print(arr_dim)

# crea un array unidimensional desde la matriz original
arr_plano = arr_ent.flatten()
print(arr_plano)

# genera una lista desde un array
lista_arr = arr_plano.tolist()
print(lista_arr)

# separar un array en varios
arrays = np.split(arr_ent, 3)
print(arrays)

# matriz transpuesta (filas pasan a ser columnas)
print(arr_ent)
t_arr = arr_ent.T
print(t_arr)
