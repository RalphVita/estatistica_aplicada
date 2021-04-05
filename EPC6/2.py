import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
import json
import math

import data
import y
x = np.array(data.x)

fig, ax = plt.subplots(1, 1)

ax.set_title('Histograma cumulativo x CDF teórica')

medias = [np.random.choice(x, 20).mean() for _ in range(50)]

n = 20
mu = np.mean(x)
sigma = np.std(x)/math.sqrt(n)

print(mu,np.std(x),sigma)

#Restringe ao intervalos de 230 a 270 => Em torno da média
x_ = [i for i in range(230,270,1)]

#Plota CDF teórica, para média e desvio calculados
ax.plot(x_, scipy.stats.norm.cdf(x_, 250, 6.45), label= 'cdf teórica')

#Histograma relativo acumudado das 50 médias do execício anterior
ax.hist(medias,bins = 20, density = True, cumulative = True,
        label='Histograma cumulativo')


plt.legend()
plt.show()
