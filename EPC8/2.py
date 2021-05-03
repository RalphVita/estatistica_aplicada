import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import norm
import json
import seaborn as sb
import math

x = np.array([265,240,258,295,251,245,287,314,260,279,283,240,238,225,247])
y = np.array([229,231,227,240,238,241,234,256,247,239,246,218,219,226,233])


n = 15
print('Xm',x.mean())
print('Ym',y.mean())
#print(y)

Zobs = (x.mean() - y.mean()) / math.sqrt((x.var()/n)+(y.var()/n))

valorP = 1-norm.cdf(Zobs,0,1)

print('Zobs:',Zobs)
print('cdf:',norm.cdf(Zobs,0,1))
print('Valor-p:',valorP)