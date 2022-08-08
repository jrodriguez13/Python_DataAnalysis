# %%
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

x1 = [1, 3, 4, 5, 6, 7, 9]
y1 = [4, 7, 7, 4, 7, 8, 3]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 2, 6, 2]

plt.bar(x1, y1, label="Barra azul", color='b')

plt.bar(x2, y2, label="Barra verde", color='g')

plt.plot()

plt.xlabel("Nº barras")

plt.ylabel("Altura barras")

plt.title("Ejemplo de gráfico de barras")

plt.legend('best')

plt.show()

# %%
