from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
import scipy.stats as stats
import math
import seaborn as sns
from numpy import random
from sklearn.metrics import mean_squared_error

n = 10
#sns.distplot(random.chisquare(df=1, size=1000), hist=False)
df=n
x = np.linspace(stats.chi2.ppf(0.0001, df),stats.chi2.ppf(0.999, df), 1000)
y = stats.chi2.pdf(x,df)
plt.plot(x[np.nonzero(y < 0.8)], y[y<0.8], label='n = '+str(n))


##### Normal ######
mu = n
variance = 2*n#*math.sqrt(2)
print(mu,variance)
sigma = math.sqrt(variance)
#x = np.random.normal(size=100)
#x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
plt.plot(x, stats.norm.pdf(x, mu, sigma))

plt.title('Chi-quadrado vs Normal')
plt.legend(['chi2(x,10)', 'א(n,√2n)'],loc=1)
plt.grid(alpha=0.2)

plt.ylabel('f(x)')
plt.xlabel('x')

plt.show()




print(math.sqrt(mean_squared_error(stats.norm.pdf(x, mu, sigma), y[y<0.8])))