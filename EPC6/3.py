import numpy as np
import matplotlib.pyplot as plt 
import random
import scipy.stats  
from statistics import NormalDist
from scipy.stats import t
import json

import data
import y
x = np.array(data.x)
    

a = 200
b = 300
# x = np.random.uniform(a,b,1000)


# with open('data.json', 'w') as outfile:
#     json.dump(json.dumps(x.tolist()), outfile)


def intervalo_confianca(amostra, confidence=0.95):
    media = np.mean(data)
    z = t.ppf((1+confidence)/2.)
    h = x.std() * z / ((len(data) - 1) ** .5)
    return media - h, media + h



fig, ax = plt.subplots(2, 1)

ax[0].set_title('Variavel X - Distribuição uniforme')
ax[0].plot(x)

std = x.std()
x_ = []
y1= []
y2= []

alfa = 0.05
confidence = 1-alfa
#Z para o intervalo de confiaça pedido
z = t.ppf((1+confidence)/2.,19) # = 
std = x.std()
print(std)
h = std   / (20 ** .5)
print(h)

for i in range(50):
    #20 Amostras aleatórias
    r = np.random.choice(x, 20) 
    #Média das amostras
    media = r.mean() 
    #Desvio padrão das amostras
    s = r.std()

    #Calcula intervalos
    µ_min, µ_max = media - 2.09*s, media + 2.09*s

    x_.append(i)
    y1.append(µ_min)
    y2.append(µ_max)

y1, y2 = y.y1, y.y2

# with open('y1.json', 'w') as outfile:
#     json.dump(json.dumps(y1), outfile)

# with open('y2.json', 'w') as outfile:
#     json.dump(json.dumps(y2), outfile)


ax[1].set_title('Intervalos de confiança das médias')

ax[1].set_ylim(200, 300)


ax[1].plot(x_, y2, 'ro', ms=5, mec='r')
ax[1].vlines(x_, 0, y2, colors='r', lw=2)

ax[1].plot(x_, y1, 'bo', ms=5, mec='b')
ax[1].vlines(x_, 0, y1, colors='b', lw=2)



#ax[1].set_xticks(x_)

ax[1].axhline(x.mean())

fig.tight_layout()
plt.show()

