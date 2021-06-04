import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.distributions import chi2
from sklearn.decomposition import PCA


Y = np.loadtxt('epc11dat.txt', delimiter=',', unpack=True)[:,:500].T
Y3 = np.loadtxt('epc11dat.txt', delimiter=',', unpack=True).T

#print(Y)

m = Y.shape[1]
limiar = chi2.ppf(0.95,m)


# Normaliza a matriz de entrada
mu = np.mean(Y,axis=0)
stdX = np.std(Y,axis=0,ddof=1)
M = (Y-mu)
cov = np.cov(M.T)


U, S, V = np.linalg.svd(cov, full_matrices=True, compute_uv=True)

PCs = np.dot(V, M.T)

autovalores, autovetores = S,V#np.linalg.eig(C)

print("Auto-valores: ")
print(autovalores)

print("\nAuto-vetores: ")
print(autovetores)


pares_de_autos = [
    (
        np.abs(autovalores[i]),
        autovetores[:,i]
    ) for i in range(len(autovalores))
]

pares_de_autos.sort()
pares_de_autos.reverse()

#print(pares_de_autos)

total = sum(autovalores)
print(total)


P = autovetores[:,0:2]

A = autovalores[0:2]
A = np.diag(A)

#A = np.linalg.inv(A)











M = P.dot(A).dot(P.T)


# Normaliza
Z = [(y - mu) for y in Y3]

# Estatística T²
T2 = [z.dot(M).dot(z.transpose()) for z in Z]

plt.axhline(limiar, label = 'limiar', color='orange')

T = Y.dot(P)

plt.plot(T2, label = 'T²')

plt.legend()
plt.show()
