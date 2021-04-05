from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
import scipy.stats as stats
import math
from sklearn.metrics import mean_squared_error

fig, ax = plt.subplots(1, 1)
legenda = []
rms = []
ns = [5,8,11,14,17,20]
for n in ns:
    legenda.append('n = '+str(n))
    # setting the values 
    # of n and p 
    #n = 10
    p = 0.5

    ##### Normal ######
    mu = n*p
    variance = n*p*(1-p)
    #print(mu,variance)
    sigma = math.sqrt(variance)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    #print(x)
    

    # defining list of r values 
    r_values = list(range(n + 1))  
    x= r_values
    # list of pmf values 
    dist = [binom.pmf(r, n, p) for r in r_values ] 
    # plotting the graph 
    print(dist)


    # pl = ax.plot(r_values, dist,'o', ms=5)
    # ax.vlines(r_values, 0, dist, colors=pl[0].get_color(), lw=2)
    # #ax.set_xticks(r_values)

    
    #ax.plot(x, stats.norm.pdf(x, mu, sigma),pl[0].get_color())

    print(len(dist),len(x))
    rms.append(math.sqrt(mean_squared_error(stats.norm.pdf(x, mu, sigma), dist)))

ax.bar(ns,rms)

#ax.legend(legenda,loc=1)

ax.set_title('Erro médio da aproximação da Distribuição binomial pela Normal')
ax.set_ylabel('Erro médio quadrático')
ax.set_xlabel('n')
ax.grid(which='major', alpha=0.3)

ax.set_xticks([5,8,11,14,17,20])

plt.show()



