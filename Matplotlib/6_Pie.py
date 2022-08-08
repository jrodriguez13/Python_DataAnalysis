# %%
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

etiquetas = 'Financiero', 'Salud', 'Construcción'
sectores = [56, 66, 24]
colores = ['c', 'b', 'r']

plt.pie(sectores, labels=etiquetas, colors=colores,
        startangle=0,
        explode=(0, 0.2, 0),
        autopct='%1.2f%%',
        shadow=True
        )

plt.axis('equal')

plt.title('Ejemplo de pie chart')
plt.show()
# %%
