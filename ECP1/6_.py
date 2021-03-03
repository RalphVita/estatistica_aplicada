import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib import cm

df = pd.read_csv('prataprivado_secomsipop1.-pesquisasdados-abertos2016f2fpesquisa-brasileira-de-midia-2016banco-de.csv', ';')

meio = ['TV','Rádio','Jornal','Internet']
faixa_etaria = ['16 A 17','18 A 24','25 A 34','35 A 44','45 A 54','55 A 64','65 E MAIS']

df = df[df['P102'] < 6]
df = df[df['P102'] != 4]
#print(df)
#grp = df['P102'].groupby(['IDAD','P102'])

#print(grp.size())
print(df.groupby(['IDAD', 'P102']).size())
#print(df.groupby(['IDAD', 'P102']).size().groupby(level=0).max())

grouped = df.groupby(['IDAD'])#.size()#.unstack(fill_value=0)
print(grouped)


cmap = plt.get_cmap("tab20c")
# outer_colors = cmap([ 0,  4,  8, 12, 16, 0, 4])
inner_colors = cmap(np.arange(4)*4)

# Create colors
a, b, c,d,e,f,g=[   plt.cm.Purples,
                    plt.cm.Blues, 
                    plt.cm.Reds, 
                    plt.cm.Greens,
                    plt.cm.Oranges,
                    plt.cm.Greys,
                    plt.cm.YlOrRd]

outer_colors = [a(0.3), b(0.3), c(0.3),d(0.3), e(0.3), f(0.3),g(0.3)] 
# inner_colors = [
#                     a(0.5), a(0.4), a(0.3), a(0.2), a(0.1),
#                     b(0.5), b(0.4), b(0.3), b(0.2), b(0.1),
#                     c(0.5), c(0.4), c(0.3), c(0.2), c(0.1),
#                     d(0.5), d(0.4), d(0.3), d(0.2), d(0.1),
#                     e(0.5), e(0.4), e(0.3), e(0.2), e(0.1),
#                     f(0.5), f(0.4), f(0.3), f(0.2), f(0.1),
#                     g(0.5), g(0.4), g(0.3), g(0.2), g(0.1)
#                 ]


fig, ax = plt.subplots()

size = 0.3

ax.pie(df.groupby(['IDAD']).size(), radius=1,labels = faixa_etaria,colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))
       
l = ['TV','Rádio','Jornal','Internet',
        'TV','Rádio','Jornal','Internet',
        'TV','Rádio','Jornal','Internet',
        'TV','Rádio','Jornal','Internet',
        'TV','Rádio','Jornal','Internet',
        'TV','Rádio','Jornal','Internet',
        'TV','Rádio','Jornal','Internet']
ax.pie(df.groupby(['IDAD', 'P102']).size(), radius=1-size,labels = l,
         colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

print(df.groupby(['IDAD', 'P102']).size())

ax.set(aspect="equal", title='Principal meio de comunicação por faixa etária')

l1 = mpatches.Patch(color=inner_colors[0], label='TV')
l2 = mpatches.Patch(color=inner_colors[1], label='Rádio')
l3 = mpatches.Patch(color=inner_colors[2], label='Jornal')
l4 = mpatches.Patch(color=inner_colors[3], label='Internet')

plt.legend(handles=[l1,l2,l3,l4], loc=(1.0, 0.1))

plt.show()