from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
import scipy.stats as stats
import math
from sklearn.metrics import mean_squared_error

fig, ax = plt.subplots(1, 2)
plt.title('Aproximação da Distribuição binomial pela Normal\nn = 10, p = 0.1')

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

ax[1].bar(['Erro Sem correção','Erro com correção'],rms)

#ax.legend(legenda,loc=1)

ax[1].set_title('Erro médio')
ax[1].set_ylabel('Erro médio quadrático')
ax[1].set_xlabel('n')
ax[1].grid(which='major', alpha=0.3)

#plt.xticks(r_values)











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


pl = ax[0].plot(r_values, dist,'o', ms=5)
ax[0].vlines(r_values, 0, dist, colors=pl[0].get_color(), lw=2)
#ax.set_xticks(r_values)

maior = stats.norm.cdf(x+0.5, mu, sigma)
menor = stats.norm.cdf(x-0.5, mu, sigma)
print(maior)
print(menor)
print(maior-menor)


ax[0].plot(x, stats.norm.pdf(x, mu, sigma),'g')
ax[0].plot(x, maior-menor,'r')

rms = []
#print(len(dist),len(x))
rms.append(math.sqrt(mean_squared_error(stats.norm.pdf(x, mu, sigma), dist)))
rms.append(math.sqrt(mean_squared_error(maior-menor, dist)))

#ax.bar(['Erro Sem correção','Erro com correção'],rms)

ax[0].legend(['Binomial','Normal','Nomal corrigida'],loc=1)

ax[0].set_title('Distribuição binomial vs Normal')
ax[0].set_ylabel('f(x) = P(X = x)')
ax[0].set_xlabel('x')
ax[0].grid(which='major', alpha=0.3)

#plt.xticks(r_values)














plt.show()



