from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np

lst = []
def binomial(p):
    # setting the values 
    # of n and p 
    n = 10
    p = p/10
    lst.append('p = '+str(p))
    # defining list of r values 
    r_values = list(range(n + 1)) 
    # list of pmf values 
    dist = [binom.pmf(r, n, p) for r in r_values ] 
    # plotting the graph 




    plt.xticks(r_values)
    plt.plot(r_values, dist, marker='o') 

    # p = plt.plot(r_values, dist,'o', ms=5)
    # plt.vlines(r_values, 0, dist, colors=p[0].get_color(), lw=2)
    #plt.bar(r_values, dist, width=0.1) 

#binomial(10)
#for p in range(9,-1,-3):
for p in range(0,11,1):
    binomial(p)

plt.ylabel('P(X = k)')
plt.xlabel('k')
plt.title('Distribuição binomial (n = 10)')

#binomial(10)



    #print(dist)
plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.3)
plt.legend(lst)
#plt.legend(['n = 3, p = 0.25'])
#plt.title('Distribuição binomial cumulativa')
plt.show()
