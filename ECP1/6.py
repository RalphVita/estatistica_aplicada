import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('prataprivado_secomsipop1.-pesquisasdados-abertos2016f2fpesquisa-brasileira-de-midia-2016banco-de.csv', ';')

meio = ['TV','Rádio','Jornal','Revista','Internet']
faixa_etaria = ['16 A 17;1','18 A 24','25 A 34','35 A 44','45 A 54','55 A 64','65 E MAIS']

df = df[df['P102'] < 6]
#print(df)
#grp = df['P102'].groupby(['IDAD','P102'])

#print(grp.size())
print(df.groupby(['IDAD', 'P102']).size())
print(df.groupby(['IDAD', 'P102']).size().groupby(level=0).max())

#df = df.groupby(['P102','IDAD']).size().unstack(fill_value=0)
#df.plot.pie(subplots=True,figsize=(8, 3),layout=(4,2))#, index=meio)


fig, axes = plt.subplots(3, 3, figsize=(10, 6))

grouped = df.groupby(['P102','IDAD'])
#print(grouped.groups.keys())

for (key, ax) in zip(grouped.groups.keys(), axes.flatten()):
    grp = grouped.get_group(key)
    #ax.set_title(faixa_etaria[int(key)-1])
    ax.pie(grp, labels=row.index, startangle=30)
    #grp.size().unstack(fill_value=0).plot.pie(ax = ax)

plt.show()