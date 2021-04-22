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
points = sb.lineplot(x, norm.pdf(x, mu, sigma) , color = 'gray').get_lines()[0].get_data()

x = points[0]
y = points[1]

norm.ppf(0.025,loc = 247.78, scale = 6.45)
X1 = norm.ppf(0.025,mu, sigma)
X2 = norm.ppf(1-0.025,mu, sigma)

plt.fill_between(x,y, where = x >=260.4320037612526, color='indianred')
plt.fill_between(x,y, where = x <=235.13652510878924, color='indianred')
plt.fill_between(x,y, where = (x<=260.4320037612526) & (x>=235.13652510878924), color='paleturquoise')

#plt.text(210, y, s, fontsize=12)

plt.xlabel(r"X̄")
plt.ylabel(r"f(X̄)")
plt.grid()
plt.show()
#print(x)