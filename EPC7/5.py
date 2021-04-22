from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

import data
import math
x = np.array(data.x)
r = []

for i in range(50):
    #20 Amostras aleatórias
    r.append(np.random.choice(x, 20).mean())

print(r)

fig = plt.figure()
ax = fig.add_subplot(111)
#x = stats.loggamma.rvs(c=2.5, size=500)
stats.probplot(r, dist='norm', sparams=(x.mean(),x.std(),), plot=ax)
ax.set_title("Probplot para normal")

# Show the results with Matplotlib:

plt.show()