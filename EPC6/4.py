import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
import json

import data
import y
x = np.array(data.x)

a = 200
b = 300
# x = np.random.uniform(a,b,1000)


# with open('data.json', 'w') as outfile:
#     json.dump(json.dumps(x.tolist()), outfile)


# def confidence_interval(data, confidence=0.95):
#     dist = NormalDist.from_samples(data)
#     z = NormalDist().inv_cdf((1 + confidence) / 2.)
#     h = x.std() * z / ((len(data) - 1) ** .5)
#     return dist.var - h, dist.var + h



fig, ax = plt.subplots(2, 1)

ax[1].set_title('Histograma')
#ax[0].plot(x)

std = x.std()
x_ = []
y1= []
y2= []
variacias = []
for i in range(1,51):
    r1 = np.random.choice(x, 20)
    var = r1.var()
    variacias.append(var)
    #conf_int = scipy.stats.norm.interval(0.05, loc=mean_, scale=std) 
    
    #conf_int = confidence_interval(r1,0.95)

    conf_int = (scipy.stats.norm.interval(0.05, loc=var, scale=var))

    x_.append(i)
    y1.append(conf_int[0])
    y2.append(conf_int[1])





ax[1].hist(variacias, weights=np.zeros_like(variacias) + 1. / len(variacias), cumulative=False,
        label='Histograma')

# n = 20
# mu = np.mean(variacias)
# sigma = np.std(x)/math.sqrt(n)
# x_ = [i for i in range(350,1050,1)]
# ax[1].plot(x_,scipy.stats.norm.cdf(x_, mu, sigma), label= 'cdf teórica')

#y1, y2 = y.y1, y.y2

# with open('y1.json', 'w') as outfile:
#     json.dump(json.dumps(y1), outfile)

# with open('y2.json', 'w') as outfile:
#     json.dump(json.dumps(y2), outfile)


ax[0].set_title('Intervalos da variância')

ax[0].set_ylim(300, 1300)


ax[0].plot(x_, y2, 'ro', ms=5, mec='r')
ax[0].vlines(x_, 0, y2, colors='r', lw=2)

ax[0].plot(x_, y1, 'bo', ms=5, mec='b')
ax[0].vlines(x_, 0, y1, colors='b', lw=2)

#ax[1].set_xticks(x_)

ax[0].axhline(x.var())

fig.tight_layout()
plt.show()

