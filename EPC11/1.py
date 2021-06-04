import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

Y = np.loadtxt('epc11dat.txt', delimiter=',', unpack=True)[:,:500]

print(Y.var(axis = 1))
#print(np.diagonal(np.cov(Y)))

v = sorted(Y.var(1),reverse=True)/sum(Y.var(1))


fig, ax = plt.subplots(2,1,sharex=True)


g = ax[1].bar(range(1,8),np.cumsum(v))



i = 0
for p in g:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax[1].text(x+width/2,
             y+height*1.01,
             "{:.2f}".format(np.cumsum(v)[i]*100)+'%',
             ha='center',
             weight='bold')
    i+=1

ax[1].set_title('Soma cumulativa da porcentagem da variância retida')





g2 = ax[0].bar(range(1,8),v)



i = 0
for p in g2:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax[0].text(x+width/2,
             y+height*1.01,
             "{:.2f}".format(v[i]*100)+'%',
             ha='center',
             weight='bold')
    i+=1


ax[0].set_title('Porcentagem da variância retida')


'''fig, ax = plt.subplots(3,1)


ax[0].plot(x)
ax[0].set_ylabel('X')

ax[1].plot(y)
ax[1].set_ylabel('Y')

ax[2].scatter(x,y, s = 0.3)
ax[2].set_ylabel('Y')
ax[2].set_xlabel('X')

'''
fig.tight_layout()
plt.show()