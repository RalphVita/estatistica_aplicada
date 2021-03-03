#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches


iris = datasets.load_iris()

df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

df['target'] = df['target'].replace(0, 'setosa')
df['target'] = df['target'].replace(1, 'versicolor')
df['target'] = df['target'].replace(2, 'virginica')

df.rename(columns={'target': 'species'}, inplace=True)


# mediana = df.groupby('species').agg('median')
# mediana.reset_index(implace = True)

# sns.barplot(x="sepal length (cm)", y="total_bill", hue="sex", data=tips)

print(df.groupby('species').agg('median'))

fig, ax = plt.subplots(figsize=(8,6))
#ax.scatter(df.x, df.y, c = pd.Categorical(df.label).codes, cmap='tab20b')


#df.groupby('species').agg('mean').plot.scatter(c='species')
df.groupby('species').agg('mean').transpose().plot.bar(ax = ax)
df.groupby('species').agg('median').transpose().plot.bar(ax = ax, linestyle= '--', fill=False)

SA = mpatches.Patch(color='black',linestyle='--', label='Media')
#plt.legend(iris.target_names)
plt.legend([SA])

#df.groupby('species').agg('median').plot.

plt.xticks(rotation='0')

plt.title('Média e Mediana das características por espécie')

plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.5)


# # media = df.groupby('species').agg('mean').reset_index().transpose()
# # print(media)
# # #exit()
# # sns.barplot(x="species", hue="sex", data=media)


#plt.legend(handles=[NA,EU,AP,SA], loc=2)

plt.show()