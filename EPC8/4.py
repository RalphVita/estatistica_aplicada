import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import norm
import json


N=9 #(ver N na Tabela 1)

x= np.random.normal(N,0.05*N,1000)

for k in range(0,500):
    x[k+500] += 0.3*N*k/500 

    

plt.plot(x)



#fig.tight_layout()
plt.show()