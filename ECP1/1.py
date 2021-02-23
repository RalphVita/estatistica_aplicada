#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
# X = iris.data#[:, :]
# y = iris.target

# print(iris.feature_names)
# print(iris.target_names)

# print(X)

data = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

setosa = data[data['target'] == 0]


fig, ax = plt.subplots(1,3, figsize=(10,4))


#fig.suptitle('sepal length (cm)')

setosa.hist('petal length (cm)', bins=3, ax = ax[0])
ax[0].set_title('bins = 3')

setosa.hist('petal length (cm)', bins=10, ax = ax[1])
ax[1].set_title('bins = 10')

setosa.hist('petal length (cm)', bins = 20, ax = ax[2])
ax[2].set_title('bins = 20')

plt.show()