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
r = np.array([244.12059485557674, 249.60920790399115, 243.38328375515266, 247.6844568067865, 241.83291174917494, 246.39736123417393, 241.36088976969177, 256.92614340960756, 246.76256317292845, 251.44558685254145, 256.1624450604093, 252.88426074149055, 256.48285968673616, 250.3886466048864, 247.0362323518625, 261.72165578841754, 251.35324051527286, 244.08509362970304, 249.602114930256, 250.23908456855443, 249.309072813486, 250.00852378850306, 248.6708514427984, 256.04135231462504, 250.0494714260195, 257.863375607851, 242.4124823457088, 240.6704937217145, 255.84370026959172, 246.92980856720465, 237.69337633238874, 255.52986967778776, 245.66505931424837, 262.0763722751728, 246.47043038554176, 259.1595503706619, 244.32071936621884, 243.4286329437852, 256.5516576744872, 260.3896351832187, 250.85185858939298, 250.74731669734757, 246.51787638861887, 252.51270589597274, 250.29775821033166, 257.54808944632623, 250.4867618452954, 258.6329751776377, 244.8437585997843, 246.1870575026332])

#20 Amostras aleatórias
n = 50
#r = np.random.choice(x, n) 
print(r.tolist())

##### Normal ######
mu = r.mean()#np.mean(x)
variance = x.var()
print(mu,variance)
sigma = math.sqrt(variance)/math.sqrt(n)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
#plt.plot(x, norm.pdf(x, mu, sigma))
#sb.set_style('whitegrid')
points = sb.lineplot(x, norm.pdf(x, mu, sigma) , color = 'gray').get_lines()[0].get_data()

x = points[0]
y = points[1]

# norm.ppf(0.025,loc = 247.78, scale = 6.45)
# X1 = norm.ppf(0.025,mu, sigma)
# X2 = norm.ppf(1-0.025,mu, sigma)

plt.fill_between(x,y, where = x >=242.1406, color='indianred')
plt.fill_between(x,y, where = x <=258.1469, color='indianred')
plt.fill_between(x,y, where = (x<=258.1469) & (x>=242.1406), color='paleturquoise')
#plt.fill_between(x,y, where = x <=250.1438, color='blue')

#plt.text(210, y, s, fontsize=12)
plt.title("pdf para µ = 250 e σ = 4.08")
plt.xlabel(r"X̄")
plt.ylabel(r"f(X̄)")
plt.grid()
plt.show()
#print(x)