import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import norm
import json
import seaborn as sb
import math



fig, ax = plt.subplots(1,1,sharex=True, sharey=True)

def Gerar(f, dois=True):
    N=9 #(ver N na Tabela 1)
    #f=0.5 #(escolher no item 1)
    v=1 #(v=1 no item 1 e escolher no item 3)
    sx=0.1*N
    sy=v*sx
    mx=N+f*0.1*N
    my=N
    x= np.random.normal(mx,sx,1000)
    y= np.random.normal(my,sy,1000)
        
    n = 100
    rx, ry = np.random.choice(x, n), np.random.choice(y, n)
    print(mx,x.mean(),rx.mean() )
    print(my,y.mean(),y.mean() )
    #print(y)

    Zobs = (rx.mean() - ry.mean()) / math.sqrt(((sx**2)/n)+((sy**2)/n))

    valorP = 1-norm.cdf(Zobs,0,1)

    print('Zobs:',Zobs)
    print('cdf:',norm.cdf(Zobs,0,1))
    print('Valor-p:',valorP)

    
    cor = 'orange' if not dois else 'blue'; 

    #x2 = np.linspace(mu2 - 4*std2, mu2 + 4*std2, 100)
    points3 = sb.lineplot(x, norm.pdf(x, mx, sx/math.sqrt(n)) , label = 'X, f = '+str(f), ax = ax,color=cor).get_lines()[0].get_data()



    z1, z2 = norm.ppf(1-0.025,loc = mx, scale = sx/math.sqrt(n)), norm.ppf(0.025,loc = mx, scale = sx/math.sqrt(n))
    ax.axvline(z1,color=cor)
    ax.axvline(z2,color=cor)



    # x3 = points3[0]
    # y3 = points3[1]
    # ax.fill_between(x3,y3, where = (x3 >= z2) & (x3 <= z1), color='indianred')

    if(dois):
        points3 = sb.lineplot(y, norm.pdf(y, my, sy/math.sqrt(n)) , label = 'Y', ax = ax, color='r').get_lines()[0].get_data()

        z1, z2 = norm.ppf(1-0.025,loc = my, scale = sy/math.sqrt(n)), norm.ppf(0.025,loc = my, scale = sy/math.sqrt(n))
        ax.axvline(z1,color='r')
        ax.axvline(z2,color='r')

# x3 = points3[0]
# y3 = points3[1]
# ax.fill_between(x3,y3, where = (x3 >= z2) & (x3 <= z1), color='indianred')

Gerar(0.5)
#Gerar(0.8,False)

ax.set_title('Para N = 100')
#ax.set_xlabel(r"X̄,")
#ax.set_ylabel(r"f(X̄)")
ax.set_xlim(8.3,10.4)
ax.grid()

# ax[1].set_title('Para N = 99')
# ax[1].set_xlabel(r"X̄")
# ax[1].set_ylabel(r"f(X̄)")
# ax[1].grid()

plt.tight_layout()
plt.legend(loc=0)
plt.show()