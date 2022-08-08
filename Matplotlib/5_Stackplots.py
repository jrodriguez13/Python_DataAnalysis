# %%
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

etiquetas = ["Sector privado", "Sector público", "Sector informal"]

fig, panel = plt.subplots()

panel.stackplot(x, y1, y2, y3,
                labels=etiquetas,
                colors=['r', 'g', 'b'])

panel.legend(loc='upper left')

panel.set_title('Gráfico apilado')

plt.show()
# %%
