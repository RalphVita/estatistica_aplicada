from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('epc9dat.txt', delimiter='   ', usecols=(0, 1), unpack=True)

fig, ax = plt.subplots(2, 1)

vB0 = []
vB1 = []

for i in range(100):
    #Pegar 100 indices aceatórios
    idx = np.random.choice(np.arange(len(x)), 100, replace=False)
    x_sample = x[idx]
    y_sample = y[idx]
    #B1 e B0
    b1, b0, r_value, p_value, std_err = stats.linregress(x_sample,y_sample)
    vB0.append(b0)
    vB1.append(b1)

print(vB0)
print(vB1)


ax[0].set_title('Histograma de β0')
ax[0].hist(vB0, density=True, bins=20)
ax[0].grid()

ax[1].set_title('Histograma de β1')
ax[1].hist(vB1, density=True, bins=20)
ax[1].grid()

fig.tight_layout()

plt.show()
