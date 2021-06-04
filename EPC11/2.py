import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.distributions import chi2
from sklearn.decomposition import PCA


Y = np.loadtxt('epc11dat.txt', delimiter=',', unpack=True)[:,:500].T

#print(Y)

m = Y.shape[1]

mu = np.mean(Y,axis=0)
stdX = np.std(Y,axis=0,ddof=1)

Z = (Y-mu)/stdX

S = np.cov(Z.T)

#print(S)
#print((Y-mu).T.dot(Y-mu)/(Y.shape[0]-1))

M = np.linalg.inv(S)

limiar = chi2.ppf(0.95,m)

model = dict()
model['mu'] = mu.tolist()
model['stdX'] = stdX.tolist()
model['M'] = M.tolist()
model['S'] = np.cov(Z.T).tolist()
model['limiar'] = limiar
print(mu)

M = Y - mu
C = M.T.dot(M)/(Y.shape[0]-1)

print(C.shape)

autovalores, autovetores = np.linalg.eig(C)

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

total = sum(autovalores)
print(total)


P = autovetores[:,0:2]

T = Y.dot(P)

plt.plot(T)
plt.show()

# PCA
pca = PCA(n_components=2)
pca.fit(Y)



# print("Auto-valores: ")
# print(pca.explained_variance_)

# # Principais Componentes
# P = pca.components_[:,0:7]




# # Λ = diag{λ1 , λ2 ,..,λa }
# A = pca.singular_values_[0:7]
# A = np.diag(A)

# print("\nAuto-vetores: ")
# print(pca.components_)



# print("\nVariancias: ")
# print(pca.explained_variance_ratio_)


# X = pca.transform(Y)

# print(X.shape)