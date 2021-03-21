from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
# setting the values 
# of n and p 
n = 3
p = 0.25
# defining list of r values 
r_values = list(range(n + 1)) 
# list of pmf values 
dist = [binom.pmf(r, n, p) for r in r_values ] 
# plotting the graph 


fig, ax = plt.subplots(1, 2)
plt.xticks(r_values)
plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
ax[0].plot(r_values, dist, 'bo', ms=5, mec='b')
ax[0].vlines(r_values, 0, dist, colors='b', lw=2)
ax[0].set_xticks(r_values)


ax[0].grid(which='major', alpha=0.3)
ax[0].legend(['n = 3\np = 0.25'],loc=1)
ax[0].set_title('Distribuição binomial')
ax[0].set_ylabel('f(X) = P(X = k)')
ax[0].set_xlabel('k')

ax[1].set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
ax[1].plot(r_values,np.cumsum(dist),marker='o')
#plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(0.1))
ax[1].grid(which='major', alpha=0.3)
ax[1].legend(['n = 3\np = 0.25'],loc=2)
ax[1].set_title('Distribuição binomial cumulativa')

ax[1].set_ylabel('F(X)')
ax[1].set_xlabel('k')

plt.xticks(r_values)

plt.show()



exit()


plt.xticks(r_values)
plt.bar(r_values, dist, width=0.1) 
plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.3)

print(dist)

plt.legend(['n = 3, p = 0.25'])
plt.title('Distribuição binomial cumulativa')
plt.show()
