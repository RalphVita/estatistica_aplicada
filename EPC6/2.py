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
# p = 0.5
mu = np.mean(medias)
# variance = n*p*(1-p)
#print(mu,variance)
sigma = np.std(x)/math.sqrt(n)
x_ = [i for i in range(230,270,1)]

print(mu,np.std(x),sigma)
ax.plot(x_,scipy.stats.norm.cdf(x_, mu, sigma), label= 'cdf teórica')

ax.hist(medias, weights=np.zeros_like(medias) + 1. / len(medias), cumulative=True,
        label='Histograma cumulativo')


plt.legend()
plt.show()
