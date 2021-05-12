import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

x, y = np.loadtxt('epc9dat.txt', delimiter='   ', usecols=(0, 1), unpack=True)

fig, ax = plt.subplots(3,1)


ax[0].plot(x)
ax[0].set_ylabel('X')

ax[1].plot(y)
ax[1].set_ylabel('Y')

ax[2].scatter(x,y, s = 0.3)
ax[2].set_ylabel('Y')
ax[2].set_xlabel('X')


plt.show()