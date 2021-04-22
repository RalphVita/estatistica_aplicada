import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import norm
import json
import seaborn as sb

import data
import math
x = np.array(data.x)
r = np.array(data.r)

#20 Amostras aleatórias
n = 20
#r = np.random.choice(x, n) 
print(r.tolist())

##### Normal ######
mu = r.mean()#np.mean(x)
variance = x.var()
print(mu,variance)
sigma = math.sqrt(variance)/math.sqrt(n)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
#plt.plot(x, norm.pdf(x, mu, sigma))
#sb.set_style('whitegrid')
sb.lineplot(x, norm.pdf(x, mu, sigma) , color = 'black')

norm(loc = 5.3 , scale = 1).cdf(4.5)

plt.xlabel(r"X̄")
plt.ylabel(r"f(X̄)")
plt.grid()
plt.show()
#print(x)