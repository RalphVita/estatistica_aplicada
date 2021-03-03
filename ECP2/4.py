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


# mediana = df.groupby('species').agg('median')
# mediana.reset_index(implace = True)

# sns.barplot(x="sepal length (cm)", y="total_bill", hue="sex", data=tips)

print(df.groupby('species').agg(['mean','median']).transpose())

df.groupby('species').agg('mean').transpose().plot.scatter()
df.groupby('species').agg('median').transpose().plot.bar()

plt.legend(iris.target_names)

#df.groupby('species').agg('median').plot.

plt.xticks(rotation='0')

plt.title('Desvio padrão das características por espécie')

plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.5)



#sns.barplot(x="day", y="total_bill", hue="sex", data=tips)

plt.show()