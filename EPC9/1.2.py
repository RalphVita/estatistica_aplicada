from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO


#Calcular e imprimir estatisticas
def Estatistica(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

    print('R²:',r_value)
    print('p-values:',p_value)

#Ler X e Y
x, y = np.loadtxt('epc9dat.txt', delimiter='   ', usecols=(0, 1), unpack=True)

#Pegar 500 amostras aleatórias
idx = np.random.choice(np.arange(len(x)), 500, replace=False)
x_sample = x[idx]
y_sample = y[idx]

#Estatisticas para X e Y
Estatistica(x,y)
#Estatíticas para as amostras
Estatistica(x_sample,y_sample)

