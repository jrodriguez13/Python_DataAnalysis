# %%
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

y1 = np.random.normal(100, 10, 200)
y2 = np.random.normal(80, 30, 200)
y3 = np.random.normal(90, 20, 200)
y4 = np.random.normal(70, 25, 200)


data_to_plot = [y1, y2, y3, y4]

fig, panel = plt.subplots()

panel.set_xticklabels(['Grupo_1', 'Grupo_2', 'Grupo_3', 'Grupo_4'])

panel.boxplot(data_to_plot, patch_artist=True)

plt.title('Ejemplo de Boxplot')
# %%
