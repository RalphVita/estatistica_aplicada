from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
import scipy.stats as stats
import math

# setting the values 
# of n and p 
n = 10
p = 0.5
# defining list of r values 
r_values = list(range(n + 1)) 
# list of pmf values 
dist = [binom.pmf(r, n, p) for r in r_values ] 
# plotting the graph 


fig, ax = plt.subplots(1, 1)
plt.xticks(r_values)
#plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
ax.plot(r_values, dist, 'bo', ms=5, mec='b')
ax.vlines(r_values, 0, dist, colors='b', lw=2)
ax.set_xticks(r_values)


ax.grid(which='major', alpha=0.3)
#ax.legend(['n = 10\np = 0.5'],loc=1)

ax.set_title('Distribuição Binomial x Normal')
ax.set_ylabel('f(x) = P(X = x)')
ax.set_xlabel('x')

##### Normal ######
mu = n*p
variance = n*p*(1-p)
print(mu,variance)
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
ax.plot(x, stats.norm.pdf(x, mu, sigma),'r')

ax.legend(['Binomial', 'Normal'],loc=1)
# ax[1].set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
# ax[1].plot(r_values,np.cumsum(dist),marker='o')
# #plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(0.1))
# ax[1].grid(which='major', alpha=0.3)
# ax[1].legend(['n = 3\np = 0.25'],loc=2)
# ax[1].set_title('Distribuição binomial cumulativa')

# ax[1].set_ylabel('F(X)')
# ax[1].set_xlabel('k')

plt.xticks(r_values)

plt.show()



