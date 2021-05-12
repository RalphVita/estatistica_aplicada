from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('epc9dat.txt', delimiter='   ', usecols=(0, 1), unpack=True)

#Pegar 500 indices aceatórios
idx = np.random.choice(np.arange(len(x)), 500, replace=False)
idx_sort = sorted(idx) #Ordenar os indices
x_sample = x[idx_sort]
y_sample = y[idx_sort]

r = []

for i in range(len(x_sample)):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_sample,np.roll(y_sample,-i))
    r.append(r_value)

plt.plot(r)

plt.ylabel('R²')
plt.xlabel('deslocamento')
plt.grid()
plt.title('Correlação cruzada para 500 amostras aleatórias ordenadas')

plt.show()
