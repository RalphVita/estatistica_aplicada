from scipy.stats import binom 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import numpy as np
import scipy.stats as stats
import math
import seaborn as sns
from numpy import random

for n in range(1,11):
    #sns.distplot(random.chisquare(df=1, size=1000), hist=False)
    df=n
    x = np.linspace(stats.chi2.ppf(0.0001, df),stats.chi2.ppf(0.999, df), 1000)
    y = stats.chi2.pdf(x,df)
    plt.plot(x[np.nonzero(y < 0.8)], y[y<0.8], label='n = '+str(n))

plt.legend()
plt.title('Efeito do número de graus de liberdade')
plt.grid(alpha=0.2)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()
