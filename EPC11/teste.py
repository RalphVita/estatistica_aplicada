from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import scipy, random

#Generate data and fit PCA
random.seed(1)
data = np.array(np.random.normal(0, 1, 500)).reshape(100, 5)
outliers = np.array(np.random.uniform(5, 10, 25)).reshape(5, 5)
data = np.vstack((data, outliers))
pca = decomposition.PCA(n_components = 2)
scaler = StandardScaler()
scaler.fit(data)
data = scaler.transform(data)
pcaFit = pca.fit(data)
dataProject = pcaFit.transform(data)

#Calculate ellipse bounds and plot with scores
theta = np.concatenate((np.linspace(-np.pi, np.pi, 50), np.linspace(np.pi, -np.pi, 50)))
circle = np.array((np.cos(theta), np.sin(theta)))
sigma = np.cov(np.array((dataProject[:, 0], dataProject[:, 1])))
ed = np.sqrt(scipy.stats.chi2.ppf(0.95, 2))
ell = np.transpose(circle).dot(np.linalg.cholesky(sigma) * ed)
a, b = np.max(ell[: ,0]), np.max(ell[: ,1]) #95% ellipse bounds
t = np.linspace(0, 2 * np.pi, 100)

plt.scatter(dataProject[:, 0], dataProject[:, 1])
plt.plot(a * np.cos(t), b * np.sin(t), color = 'red')
plt.grid(color = 'lightgray', linestyle = '--')
plt.show()