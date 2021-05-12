from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# def Estatistica(x,y):
#     slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

#     print('R²:',r_value)
#     print('p-values:',p_value)

x, y = np.loadtxt('epc9dat.txt', delimiter='   ', usecols=(0, 1), unpack=True)

r = []

for i in range(len(x)):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,np.roll(y,-i))
    r.append(r_value)

plt.plot(r)

plt.ylabel('R²')
plt.xlabel('deslocamento')
plt.grid()
plt.title('Correlação cruzada')

plt.show()
