## Fatores
## n A A2 A3 c4 B3 B4 B5 B6 d2 1/d2 d3 D1 D2 D3 D4

import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from sklearn.model_selection import train_test_split 
from scipy import stats
import math
from scipy.stats import t

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

#Ler X e Y
x, y = np.loadtxt('epc10dat.txt', delimiter='   ', usecols=(0, 1), unpack=True)

#Separa primeiras 1200: 70% Treino, 30% Teste
X_train, X_test, y_train, y_test = train_test_split(x[:1200], y[:1200], train_size=0.7)

#Calcula B0 e B1 com os dados de treino
b1, b0, r_value, p_value, std_err = stats.linregress(X_train,y_train)

#Dados previsto pelo modelo
prev = b0 + b1*X_test

#Resíduos
residuos = [(y1-y0) for (y1,y0) in zip(y_test,prev)]


#Ler fator c4
c4 = np.loadtxt('fatores.txt', delimiter=' ', usecols=4, unpack=True)

print(c4)

m = 10
n = 25

a = np.random.choice(residuos, m*n, False)
media = np.mean(a.mean())
s = np.mean(a.std())
'''for i in range(m):
    #n Amostras aleatórias
    a = np.random.choice(residuos, n, False)
    media.append()
    s.append(a.std())

media = np.mean(media)
s = np.mean(s)'''

CL = media
UCL = media + (3*s/(c4[n-2]*math.sqrt(n)))
LCL = media - (3*s/(c4[n-2]*math.sqrt(n)))

print('UCL:',UCL)
print('CL:',CL)
print('LCL:',LCL)






#Dados previsto pelo modelo
prev = b0 + b1*x

#Resíduos
residuos = [(y1-y0) for (y1,y0) in zip(y,prev)]


media = running_mean(residuos,25)






ARL = 0
FN = 0
cont = 0
for r in media[1200:]:
    if r > UCL:
        cont += 1
    else:
        cont = 0
        FN +=1
    if cont > 1:
        break

    ARL +=1

ARL +=1
print('ARL:', ARL)
print('FN:', FN/800.0)



plt.axhline(UCL, color='orange')
plt.axhline(CL, color='orange')
plt.axhline(LCL, color='orange')


plt.plot(media, label = 'N = '+str(n))

plt.title('Gráfico de x barra')
plt.legend()

plt.show()