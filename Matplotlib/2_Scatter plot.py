# %%
import numpy as np
import matplotlib.pyplot as plt

x1 = [3, 5, 7]
y1 = [3, 5, 9]

x2 = [1, 2, 3, 4]
y2 = [2, 3, 2, 3]

x3 = [8, 7, 2, 5, 4]
y3 = [6, 8, 7, 8, 7]

plt.scatter(x1, y1)

plt.scatter(x2, y2, marker='v', color='r')

plt.scatter(x3, y3, marker='^', color='m')

plt.title('Ejemplo de Scatter Plot')

plt.show()

plt.savefig(r'out\scatterplot.png')
# %%
