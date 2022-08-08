# %%
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

y = 5 + np.random.randn(100)

x = [e for e in range(len(y))]

plt.bar(x, y)

plt.title("Datos en crudo")
plt.show()

# ********************

plt.hist(y, bins=20)

plt.title("Histograma")
plt.show()

# ********************

plt.hist(y, cumulative=True, bins=20)

plt.title("Histograma acumulado")
plt.show()
# %%
