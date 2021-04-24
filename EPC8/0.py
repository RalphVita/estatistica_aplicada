import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import norm
import json


N=9 #(ver N na Tabela 1)
f=1 #(escolher no item 1)
v=1 #(v=1 no item 1 e escolher no item 3)
sx=0.1*N
sy=v*sx
mx=N+f*0.1*N
my=N
x= np.random.normal(mx,sx,1000)
y= np.random.normal(my,sy,1000)
    

print(x)
#print(y)
