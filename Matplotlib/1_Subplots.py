# %%
from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

fig, panel = plt.subplots()

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

panel.plot(x, y)

# Crea la figura con dos paneles horizontales
fig, (pan_1, pan_2) = plt.subplots(2, 1)

# Figura 1
x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)

pan_1.plot(x1, y1)

# Figura 2
x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)

pan_2.plot(x2, y2)

# Guardar la figura
plt.savefig(r'out\sin_cos.png')

# -----------------------------------

# Crea la figura con dos paneles verticales
fig, (pan_1, pan_2) = plt.subplots(1, 2, constrained_layout=True)

# Figura 1
x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)

pan_1.plot(x1, y1)

# Figura 2
x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)

pan_2.plot(x2, y2)

# Guardar la figura
plt.savefig(r'out\sin_cos_vertical.png')

# -----------------------------------

# Crear multipanel
fig, ((pan_1, pan_2), (pan_3, pan_4)) = plt.subplots(
    2, 2, constrained_layout=True)

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

pan_1.plot(x, y)

pan_2.plot(x, y**2)

pan_3.plot(x, -y)

pan_4.plot(x, -y**2)

for ax in fig.get_axes():
    ax.set(xlabel='x-label', ylabel='y-label')

plt.savefig(r'out\multipanel.png')

# *---------------------

# ShareX y ShareY indica que los paneles comparten eje
fig, (pan_1, pan_2) = plt.subplots(2, sharex=True)

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

pan_1.plot(x, y, 'tab:orange')

pan_2.plot(x + 1, -y, 'green')

# ***************

fig, paneles = plt.subplots(2, 2, sharex='col', sharey='row')

(pan_1, pan_2), (pan_3, pan_4) = paneles

pan_1.plot(x, y)

pan_2.plot(x, y**2, 'tab:orange')

pan_3.plot(x + 1, -y, 'tab:green')

pan_4.plot(x + 2, -y**2, 'tab:red')

# twinx permite graficar dos funciones en un mismo pañel

fig, pan_1 = plt.subplots(1, 1)

pan_2 = pan_1.twinx()


x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)

pan_1.plot(x1, y1, 'y')


x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)

pan_2.plot(x2, y2, 'r')


plt.savefig('out\sin_cos_2.png')

# ************ COLORES Y ESTILOS

# estilo de línea

fig, pan_1 = plt.subplots(1, 1)

x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)


pan_1.plot(x1, y1, linestyle='--', color='g')

plt.savefig('out\styles1.png')

# espaciado de puntos de la linea

fig, pan_1 = plt.subplots(1, 1)

x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)

pan_1.plot(x1, y1, linestyle='--', color='y', marker='o',
           markeredgecolor='y', markerfacecolor='r', label='Seno')

pan_1.legend(loc='best')

plt.savefig('out\styles2.png')

# Leyendas y etiquetas

fig, pan_1 = plt.subplots(1, 1)
pan_2 = pan_1.twinx()

x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)

funcion1 = pan_1.plot(x1, y1, color='b', marker='^', markeredgecolor='b', markerfacecolor='g',
                      label='Seno')

x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)

funcion2 = pan_2.plot(x2, y2, color='r', marker='o', markeredgecolor='r', markerfacecolor='y',
                      label='Coseno')

funciones = funcion1 + funcion2

labels = [f.get_label() for f in funciones]

plt.legend(funciones, labels, loc='best')

plt.savefig('out\legends1.png')

# Etiquetas de eje

fig, pan_1 = plt.subplots(1, 1)
pan_2 = pan_1.twinx()
x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)
funcion1 = pan_1.plot(x1, y1, color='b', marker='^', markeredgecolor='b', markerfacecolor='g',
                      label='Seno')
x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)
funcion2 = pan_2.plot(x2, y2, color='r', marker='o', markeredgecolor='r', markerfacecolor='y',
                      label='Coseno')
funciones = funcion1 + funcion2
labels = [f.get_label() for f in funciones]
plt.legend(funciones, labels, loc='best')


pan_1.set_xlabel('$x$')
pan_1.set_ylabel('$y_1$')
pan_2.set_ylabel('$y_2$')

plt.savefig('out\legends2.png')

# Agregar un titulo

fig, pan_1 = plt.subplots(1, 1)
pan_2 = pan_1.twinx()
x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)
funcion1 = pan_1.plot(x1, y1, color='b', marker='^', markeredgecolor='b', markerfacecolor='g',
                      label='Seno')
x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)
funcion2 = pan_2.plot(x2, y2, color='r', marker='o', markeredgecolor='r', markerfacecolor='y',
                      label='Coseno')
funciones = funcion1 + funcion2
labels = [f.get_label() for f in funciones]
plt.legend(funciones, labels, loc='best')

pan_1.set_xlabel('$x$')
pan_1.set_ylabel('$y_1$')
pan_2.set_ylabel('$y_2$')

plt.title('Seno y coseno')

plt.tight_layout()

plt.savefig('out\legends3.png')
# %%
