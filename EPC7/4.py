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

fig, ax = plt.subplots(2,1,sharex=True, sharey=True)

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
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
#plt.plot(x, norm.pdf(x, mu, sigma))
#sb.set_style('whitegrid')


mu2 = 260.43
std2=2.9058469516701635
x2 = np.linspace(mu2 - 4*std2, mu2 + 4*std2, 100)
points2 = sb.lineplot(x2, norm.pdf(x2, mu2, std2) , label = 'μ = 260.43',ax = ax[1]).get_lines()[0].get_data()

x_ = points2[0]
y_ = points2[1]

ax[1].fill_between(x_,y_, where = x_ <= 258.4739797244314, color='indianred')






mu2 = 260.43
std2 = sigma
x2 = np.linspace(mu2 - 4*std2, mu2 + 4*std2, 100)
points3 = sb.lineplot(x2, norm.pdf(x2, mu2, std2) , label = 'μ = 260.43', ax = ax[0]).get_lines()[0].get_data()

x3 = points3[0]
y3 = points3[1]
ax[0].fill_between(x3,y3, where = (x3 <= 260.43), color='indianred')

print(sigma)
std2=2.9058469516701635
points = sb.lineplot(x, norm.pdf(x, mu, std2) , label = 'μ = 247.78',ax = ax[1]).get_lines()[0].get_data()
points = sb.lineplot(x, norm.pdf(x, mu, sigma) , label = 'μ = 247.78',ax = ax[0]).get_lines()[0].get_data()


#norm.ppf(0.025,loc = 247.78, scale = 6.45)
X1 = norm.ppf(0.025,mu, sigma)
X2 = norm.ppf(1-0.025,mu, sigma)

#plt.fill_between(x,y, where = x >=260.4320037612526, color='indianred')
#plt.fill_between(x,y, where = x <=235.13652510878924, color='indianred')
#plt.fill_between(x,y, where = (x<=260.4320037612526) & (x>=235.13652510878924), color='paleturquoise')

#plt.text(210, y, s, fontsize=12)

ax[0].set_title('Para N = 20')
ax[0].set_xlabel(r"X̄")
ax[0].set_ylabel(r"f(X̄)")
ax[0].grid()

ax[1].set_title('Para N = 99')
ax[1].set_xlabel(r"X̄")
ax[1].set_ylabel(r"f(X̄)")
ax[1].grid()

plt.tight_layout()

plt.show()
#print(x)