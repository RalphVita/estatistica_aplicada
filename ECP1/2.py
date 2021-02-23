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

#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#['setosa' 'versicolor' 'virginica']

df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

# setosa = data[data['target'] == 0]
# versicolor = data[data['target'] == 1]
# virginica = data[data['target'] == 2]

df['target'] = df['target'].replace(0, 'setosa')
df['target'] = df['target'].replace(1, 'versicolor')
df['target'] = df['target'].replace(2, 'virginica')
print(df)
#fig, ax = plt.subplots(1,3, figsize=(10,4))


#fig.suptitle('sepal length (cm)')

#df.groupby(['target'])['sepal width (cm)'].mean().plot.bar()

#df.plot.bar()


df = df[['sepal width (cm)','target']]

ax = pd.concat(
    [
        df.groupby(['target']).mean()['sepal width (cm)'].rename('Média'), 
        df.groupby(['target']).median()['sepal width (cm)'].rename('Mediana'), 
        df.groupby(['target']).std()['sepal width (cm)'].rename('Desvio padrão'),
        df.groupby(['target']).apply(pd.DataFrame.kurtosis)['sepal width (cm)'].rename('Curtose')
    ],
     #keys=['Média', 'Mediana', 'Desvio padrão','Curtose'],
    axis=1).plot.bar(rot=0)

#ax.get_legend().set_bbox_to_anchor((-1.1, 1))
#ax.legend(loc = 'best')#,bbox_to_anchor=(.5, 0.7))

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=4, fancybox=True, shadow=True)

ax.set_ylabel('sepal width (cm)')
#print(df.groupby(['target']).apply(pd.DataFrame.kurtosis)['sepal width (cm)'])
#plt.legend(loc='lower')
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

plt.show()