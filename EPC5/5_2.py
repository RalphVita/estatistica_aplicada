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
# # plt.xticks(r_values)
# # #plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
# # ax.plot(r_values, dist, 'bo', ms=5, mec='b')
# # ax.vlines(r_values, 0, dist, colors='b', lw=2)
# # ax.set_xticks(r_values)


ax.grid(which='major', alpha=0.3)
#ax.legend(['n = 10\np = 0.5'],loc=1)

ax.set_title('Histograma e pdf de Y = X²')
ax.set_ylabel('f(x)')
ax.set_xlabel('x')

##### Normal ######
mu = 0
variance = 1
print(mu,variance)
sigma = math.sqrt(variance)
#x = np.random.normal(size=100)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)**2
ax.plot(x, stats.norm.pdf(x, mu, sigma))
#ax.plot(x, stats.norm.cdf(x, mu, sigma))

x = np.random.normal(size=1000)**2
ax.hist(x, weights=np.zeros_like(x) + 1. / x.size)
#ax.hist(x)

ax.legend(['Normal', 'Histograma'],loc=1)




plt.show()



