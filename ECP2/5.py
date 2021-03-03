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

bins = 20

df.rename(columns={'target': 'species'}, inplace=True)





formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

#plt.title('Boxplot das características por espécie')
#sns.set(style="ticks") 
sns.set_theme()
plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
sns.histplot(hue='species',x='sepal length (cm)',data=df, bins=bins, alpha=0.6,element="step")
#plt.legend([0, 1, 2], iris.target_names)
#plt.xticks([0, 1, 2], iris.target_names)
#plt.legend(iris.target_names)
plt.subplot(2,2,2)
sns.histplot(hue='species',x='sepal width (cm)',data=df,bins=bins, alpha=0.6,element="step")
#plt.xticks([0, 1, 2], iris.target_names)
#plt.legend(iris.target_names)
plt.subplot(2,2,3)
sns.histplot(hue='species',x='petal length (cm)',data=df,bins=bins, alpha=0.6,element="step")
#plt.xticks([0, 1, 2], iris.target_names)
#plt.legend(iris.target_names)
plt.subplot(2,2,4)
sns.histplot(hue='species',x='petal width (cm)',data=df,bins=bins, alpha=0.6,element="step")
#plt.xticks([0, 1, 2], iris.target_names)
#plt.legend(iris.target_names)

plt.tight_layout(pad=3.0)



#df.groupby('species').hist()

# # # fig, axes = plt.subplots(4, 4, figsize=(10, 6))

# # # grouped = df.groupby('species')
# # # #print(grouped.groups.keys())

# # # for g in grouped:
# # #     #grp = grouped.get_group(key)
# # #     #ax.set_title(faixa_etaria[int(key)-1])
# # #     g.hist(ax = axes)
# # #     #grp.size().unstack(fill_value=0).plot.pie(ax = ax)




plt.show()