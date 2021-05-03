import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import norm
import json
import seaborn as sb
import math
from scipy.stats import chi2
from scipy.stats import f as F



fig, ax = plt.subplots(1,1,sharex=True, sharey=True)

def Gerar(v, dois=True):
    N=9 #(ver N na Tabela 1)
    f=1 #(escolher no item 1)
    #v=1 #(v=1 no item 1 e escolher no item 3)
    sx=0.1*N
    sy=v*sx
    mx=N+f*0.1*N
    my=N
    x= np.random.normal(mx,sx,1000)
    y= np.random.normal(my,sy,1000)
        
    n = 20
    rx, ry = np.random.choice(x, n), np.random.choice(y, n)
    print(mx,x.std(),rx.std() )
    print(my,y.std(),y.std() )
    #print(y)

    f0 = rx.var()/ry.var()
    f0=f0**2
    

    print('Fobs:',f0)
    print('cdf:',F.cdf(f0,n-1,n-1),1-F.cdf(1.0/f0,n-1,n-1))
    print('Valor-p:',F.cdf(f0,n-1,n-1)+1-F.cdf(1.0/f0,n-1,n-1))

    
    cor = 'orange' if not dois else 'blue'; 


    dfn = n-1
    dfd = n-1
    #x = np.linspace(mx - 3*sx, mx + 3*sx, 1000)
    x = np.linspace(F.ppf(0.00, dfn, dfd),
                F.ppf(0.999, dfn, dfd), 100)
    #x = np.linspace(chi2.ppf(0.35, n-1),chi2.ppf(0.99, n-1), 1000)
    #print(x)
    points3 = sb.lineplot(x, F.pdf(x,n-1,n-1)).get_lines()[0].get_data()
    f1, f2 = F.ppf(1-0.025,dfd,dfn), F.ppf(0.025,dfd,dfn)

    x3 = points3[0]
    y3 = points3[1]
    ax.fill_between(x3,y3, where = (x3 > f1) | (x3 < f2), color='indianred')

    #x2 = np.linspace(mu2 - 4*std2, mu2 + 4*std2, 100)
    #points3 = sb.lineplot(x, chi2.pdf(x, n-1) , label = 'X, f = '+str(f), ax = ax,color=cor).get_lines()[0].get_data()



    # z1, z2 = norm.ppf(1-0.025,loc = mx, scale = sx/math.sqrt(n)), norm.ppf(0.025,loc = mx, scale = sx/math.sqrt(n))
    # ax.axvline(z1,color=cor)
    # ax.axvline(z2,color=cor)



    # x3 = points3[0]
    # y3 = points3[1]
    # ax.fill_between(x3,y3, where = (x3 >= z2) & (x3 <= z1), color='indianred')

    #if(dois):
     #   points3 = sb.lineplot(y, chi2.pdf(y, n-1) , label = 'Y', ax = ax, color='r').get_lines()[0].get_data()

        # z1, z2 = norm.ppf(1-0.025,loc = my, scale = sy/math.sqrt(n)), norm.ppf(0.025,loc = my, scale = sy/math.sqrt(n))
        # ax.axvline(z1,color='r')
        # ax.axvline(z2,color='r')

# x3 = points3[0]
# y3 = points3[1]
# ax.fill_between(x3,y3, where = (x3 >= z2) & (x3 <= z1), color='indianred')

Gerar(3)
#Gerar(0.8,False)

ax.set_title('Distribuição F')
#ax.set_xlabel(r"X̄,")
#ax.set_ylabel(r"f(X̄)")
#ax.set_xlim(8.3,10.4)
ax.grid()

# ax[1].set_title('Para N = 99')
# ax[1].set_xlabel(r"X̄")
# ax[1].set_ylabel(r"f(X̄)")
# ax[1].grid()

plt.tight_layout()
plt.legend(loc=0)
plt.show()