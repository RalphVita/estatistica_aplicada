from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
import scipy.stats as stats
import math
from sklearn.metrics import mean_squared_error

fig, ax = plt.subplots(1, 1)

def ContinuityCorrectionFactor(x,n):
    if x == n:
        return

# setting the values 
# of n and p 
n = 10
p = 0.1

##### Normal ######
mu = n*p
variance = n*p*(1-p)
#print(mu,variance)
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
#print(x)


# defining list of r values 
r_values = list(range(n + 1))  
x= np.array(r_values)
# list of pmf values 
dist = [binom.pmf(r, n, p) for r in r_values ] 
# plotting the graph 
#print(dist)


#pl = ax.plot(r_values, dist,'o', ms=5)
#ax.vlines(r_values, 0, dist, colors=pl[0].get_color(), lw=2)
#ax.set_xticks(r_values)

maior = stats.norm.cdf(x+0.5, mu, sigma)
menor = stats.norm.cdf(x-0.5, mu, sigma)
print(maior)
print(menor)
print(maior-menor)
#ax.plot(x, maior-menor,'r')

#ax.plot(x, stats.norm.pdf(x, mu, sigma),'g')

rms = []
#print(len(dist),len(x))
rms.append(math.sqrt(mean_squared_error(stats.norm.pdf(x, mu, sigma), dist)))
rms.append(math.sqrt(mean_squared_error(maior-menor, dist)))

ax.bar([1,2],rms)

#ax.legend(legenda,loc=1)

ax.set_title('Erro médio da aproximação da Distribuição binomial pela Normal')
ax.set_ylabel('Erro médio quadrático')
ax.set_xlabel('n')
ax.grid(which='major', alpha=0.3)

#plt.xticks(r_values)

plt.show()



