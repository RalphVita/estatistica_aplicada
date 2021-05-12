import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from sklearn.model_selection import train_test_split 
from scipy import stats
import math
from scipy.stats import t

fig, ax = plt.subplots(3,1)

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

print('B0:',b0)
print('B1:',b1)


#Modelo vs Teste
ax[0].plot(X_test,prev)
ax[0].scatter(X_test,y_test)
ax[0].set_title('Modelo vs Dados de teste')
ax[0].set_ylabel('y_test')
ax[0].set_xlabel('X_test')



ax[1].scatter(X_test,residuos)
ax[1].axhline(0)
ax[1].set_title('Resíduos')
ax[1].set_xlabel('X_test')



mu, sigma = np.mean(residuos), np.std(residuos)

print('Média: ', mu)
print('std: ', sigma)


n = len(X_test)

sse = sum([(y1-y0)**2 for (y1,y0) in zip(y_test,prev)])
print('sse:',sse)
var = sse/(n-2)
print('var:',var)

sxx = sum(X_test**2) - (sum(X_test)**2)/n
print('ssx:',sxx)

seB1 = math.sqrt(var/sxx)
print('sqrt(var/sxx)',seB1)

seB0 = math.sqrt(var*((1/n)+(np.mean(X_test)/sxx)))
print('seB0',seB0)

alfa = 0.05
z = t.ppf(alfa/2.,n-2)

print('t:',z)

print('t0:',b1/seB1)







x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

#Plota PDF teórica
ax[2].set_title('Resíduos')
ax[2].plot(x, stats.norm.pdf(x, mu, sigma), label= 'PDF')
ax[2].hist(residuos, density=True, bins=20, label='Histograma')
ax[2].grid()




fig.tight_layout(pad=0.5)



plt.legend()


plt.show()