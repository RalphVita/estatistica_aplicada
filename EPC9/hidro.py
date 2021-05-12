from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from scipy.stats import t
import math

x, y = np.loadtxt('hidrogenio.txt', delimiter=' ', usecols=(0, 1), unpack=True)

#slope, intercept, r_value, p_value, std_err, intercept_stderr = stats.linregress(x,y)
#print(slope, intercept, r_value, p_value, std_err, intercept_stderr)

result = stats.linregress(x,y)


prev = result.intercept + result.slope*x

sse = sum([(y1-y0)**2 for (y1,y0) in zip(y,prev)])
var = sse/18
print(sse/18)

sxx = sum(x**2) - (sum(x)**2)/20
print(sxx)

print(math.sqrt(var/sxx))

alfa = 0.05
n = 20
z = t.ppf(alfa/2.,n-2)

print(z)

print(result.slope+z*math.sqrt(var/sxx))
print(result.slope-z*math.sqrt(var/sxx))

t0 = result.slope/math.sqrt(var/sxx)

print('t0',t0)