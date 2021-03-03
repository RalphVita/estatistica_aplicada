#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns
import pandas as pd
import numpy as np

iris = datasets.load_iris()

df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

df['target'] = df['target'].replace(0, 'setosa')
df['target'] = df['target'].replace(1, 'versicolor')
df['target'] = df['target'].replace(2, 'virginica')

df.rename(columns={'target': 'species'}, inplace=True)



df.groupby('species').std().transpose().plot.bar()

#plt.xticks([0, 1, 2], iris.target_names, rotation='0')

plt.title('Desvio padrão das características das espécies')

plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.5)
plt.xticks(rotation='0')

plt.show()