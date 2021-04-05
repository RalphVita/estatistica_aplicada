import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
import json
import scipy.stats as stats

import data
import y
x = np.array(data.x)

a = 200
b = 300


fig, ax = plt.subplots(2, 1)

ax[1].set_title('Histograma')
#ax[0].plot(x)
print(x.var)
std = x.std()
x_ = []
y1= []
y2= []
variancias = []
n=20
for i in range(50):
    #20 Amostras aleatórias
    r1 = np.random.choice(x, 20)
    #Variância das amostras
    s2 = r1.var()   

    #Calcula intervalos
    var_min = (n-1)*s2/stats.chi2.ppf(0.05, n-1)
    var_max = (n-1)*s2/stats.chi2.ppf(1-0.05, n-1)

    x_.append(i)
    y1.append(var_min)
    y2.append(var_max)

    variancias.append(s2)



#Restringe ao intervalos de 300 a 1300 => Em torno da variância
x2 = np.array([i for i in range(300,1300,1)])

#Plota chi2 teórica, para média e desvio de X
ax[1].plot(x2, scipy.stats.chi2.pdf((x2-250)/std, 19), label= 'chi2(x,19) teórica')

#Plota Histograma
ax[1].hist(variancias, bins = 20, weights=np.zeros_like(variancias) + 1. / len(variancias), cumulative=False,
        label='Histograma')




ax[0].set_title('Intervalos da variância')

#ax[0].set_ylim(300, 1300)

plt.legend()
ax[0].plot(x_, y2, 'ro', ms=5, mec='r')
ax[0].vlines(x_, 0, y2, colors='r', lw=2)

ax[0].plot(x_, y1, 'bo', ms=5, mec='b')
ax[0].vlines(x_, 0, y1, colors='b', lw=2)

#ax[1].set_xticks(x_)

ax[0].axhline(x.var())

fig.tight_layout()
plt.show()

