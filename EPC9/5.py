from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from scipy.stats import t
import math

x = np.random.normal(size=50)
y = np.random.normal(size=50)

n = 50
x_sample = x
y_sample = y

result = stats.linregress(x_sample,y_sample)


print('B0:',result.intercept)
print('B1:',result.slope)


prev = result.intercept + result.slope*x_sample

sse = sum([(y1-y0)**2 for (y1,y0) in zip(y_sample,prev)])
print('sse:',sse)
var = sse/(n-2)
print('var:',var)

sxx = sum(x_sample**2) - (sum(x_sample)**2)/n
print('ssx:',sxx)

seB1 = math.sqrt(var/sxx)
print('sqrt(var/sxx)',seB1)

seB0 = math.sqrt(var*((1/n)+(np.mean(x_sample)/sxx)))
print('seB0',seB0)

alfa = 0.05
z = t.ppf(alfa/2.,n-2)

print('t:',z)


print(result.intercept+z*seB0,'< B0 <',result.intercept-z*seB0)
print(result.slope+z*seB1,'< B1 <',result.slope-z*seB1)
