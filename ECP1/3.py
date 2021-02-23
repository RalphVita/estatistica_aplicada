#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()

df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

grouped = df.groupby('target')

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6,4), sharey=True)



for (key, ax) in zip(grouped.groups.keys(), axes.flatten()):
    grp = grouped.get_group(key)
    ax.set_title(iris.target_names[int(key)])
    grp.plot.scatter(x = 'petal width (cm)', y = 'petal length (cm)',ax=ax,c='none',edgecolor='blue', s=30)
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

#ax.legend()
plt.show()