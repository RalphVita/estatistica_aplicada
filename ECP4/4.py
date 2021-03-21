from scipy import stats
import numpy as np

# xk = 5*np.arange(10)
# pk = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
xk = np.arange(5)**2
pk = (0.6561, 0.2916, 0.0486, 0.0036, 0.0001)
custm = stats.rv_discrete(name='custm', values=(xk, pk))
print(xk)
print(sum(pk))
print('Média: ',custm.mean())
print('Variancia: ',custm.var())
print('Desvio padrão: ',custm.std())