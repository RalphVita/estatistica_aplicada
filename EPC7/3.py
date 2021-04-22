import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import norm
import json
import seaborn as sb

import data
import math
x = np.array(data.x)
r = np.array(data.r)

#20 Amostras aleatórias
n = 20
#r = np.random.choice(x, n) 
#print(r.tolist())

##### Normal ######
mu = r.mean()#np.mean(x)
variance = x.var()
print(mu,variance)
sigma = math.sqrt(variance)/math.sqrt(n)


print(norm.ppf(0.1, 0, 1))
print(norm.ppf(0.1, 0, 1)*sigma-260.43)