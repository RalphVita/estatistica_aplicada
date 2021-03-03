#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns
import pandas as pd
import numpy as np

iris = datasets.load_iris()

df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])


df.rename(columns={'target': 'species'}, inplace=True)



df.groupby('species').mean().plot.bar()

plt.xticks([0, 1, 2], iris.target_names, rotation='0')

plt.title('Média das características por espécie')

plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.5)

plt.show()