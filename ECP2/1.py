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


# df.boxplot(by='target')

# plt.xticks([1, 2, 3], iris.target_names)

# plt.show()

df.rename(columns={'target': 'species'}, inplace=True)
#plt.title('Boxplot das características por espécie')
#sns.set(style="ticks") 
sns.set_theme()
plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
sns.boxplot(x='species',y='sepal length (cm)',data=df)
#plt.xticks([0, 1, 2], iris.target_names)
plt.subplot(2,2,2)
sns.boxplot(x='species',y='sepal width (cm)',data=df)
#plt.xticks([0, 1, 2], iris.target_names)
plt.subplot(2,2,3)
sns.boxplot(x='species',y='petal length (cm)',data=df)
#plt.xticks([0, 1, 2], iris.target_names)
plt.subplot(2,2,4)
sns.boxplot(x='species',y='petal width (cm)',data=df)
#plt.xticks([0, 1, 2], iris.target_names)
plt.tight_layout(pad=3.0)

plt.show()