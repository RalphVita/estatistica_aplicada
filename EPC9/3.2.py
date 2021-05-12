from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import math
import b

vB0,  vB1 = b.vB0, b.vB1



fig, ax = plt.subplots(2, 1)


##### B0 ######
mu = np.mean(vB0)
variance = np.var(vB0)
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

print('Média B0:',mu)
print('STD B0:',sigma)

#Plota PDF teórica
ax[0].set_title('β0')
ax[0].plot(x, stats.norm.pdf(x, mu, sigma), label= 'PDF')
ax[0].hist(vB0, density=True, bins=20, label='Histograma')
ax[0].grid()
ax[0].legend()

ax[0].axvline(-5.52)
ax[0].axvline(-2.9)


##### B1 ######
mu = np.mean(vB1)
variance = np.var(vB1)
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

print('Média B1:',mu)
print('STD B1:',sigma)

#Plota PDF teórica
ax[1].set_title('β1')
ax[1].plot(x, stats.norm.pdf(x, mu, sigma), label= 'PDF')
ax[1].hist(vB1, density=True, bins=20, label='Histograma')
ax[1].grid()

ax[1].axvline(13.95)
ax[1].axvline(14.47)

plt.legend()
plt.show()