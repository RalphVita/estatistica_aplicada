from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
# setting the values 
# of n and p 
n = 125
p = 0.1
# defining list of r values 
r_values = list(range(n + 1)) 
# list of pmf values 
dist = [binom.pmf(r, n, p) for r in r_values ] 
# plotting the graph 

print(1-sum(dist[0:6]))