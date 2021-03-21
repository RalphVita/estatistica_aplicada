import numpy as np
import matplotlib.pyplot as plt

data = np.arange(-3, 4)
y = np.array([1/8, 3/8, 5/8, 7/8, 1.])
yn = np.insert(y, 0, 0)

fig, ax = plt.subplots()
ax.set_facecolor('white')

# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hlines.html
ax.hlines(y=yn, xmin=data[:-1], xmax=data[1:],
          color='b', zorder=1)

# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.vlines.html
ax.vlines(x=data[1:-1], ymin=yn[:-1], ymax=yn[1:], color='b',
          linestyle='dashed', zorder=1)

ax.scatter(data[1:-1], y, color='b', s=18, zorder=2)
ax.scatter(data[1:-1], yn[:-1], color='white', s=18, zorder=2,
           edgecolor='b')
ax.grid(False)
ax.set_xlim(data[0], data[-1])
ax.set_ylim([-0.005, 1.01])

ax.grid(which='major', alpha=0.3)
plt.ylabel('F(X)')
plt.xlabel('k')
ax.set_title('Função acumulada de probabilidade')

plt.show()