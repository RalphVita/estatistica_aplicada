import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# y = [0.0, 0.15, 0.1, 0.1, 0.25, 0.1, 0.15, 0.0, 0.05, 0.0, 0.1, 0.0] 
# X = [-1.5, -1.2, -0.9, -0.6, -0.3, 0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8]

# df = pd.DataFrame({
#     'lab':
#         [-1.5,
#         -1.3,
#         -0.1,
#         -0.7,
#         -0.4,
#         -0.1,
#         0.4,
#         0.7,
#         0.1,
#         1.3,
#         1.6,
#         2.0], 
#     'val':
#         []
# })
#ax = df.plot.bar(x='lab', y='val', rot=0,width = 0.3)


y = np.array([
    
    -1.1,-1.1,-1.1,-1.1,#-1.1,
    -0.8,-0.8,-0.8,
    -0.5,-0.5,-0.5,
    -0.2,-0.2,-0.2,-0.2,-0.2,-0.2,-0.2,-0.2,
    0.1,0.1,0.1,
    0.4,0.4,0.4,0.4,#0.4,
    
    1,1,
    
    1.6,1.6,1.6
    
])

print(len(y))

plt.hist(y, 
    range = (-1.5, 2.0), 
    bins=12,
    #weights=np.zeros_like(y) + 1. / len(y),
    #cumulative=True,
    edgecolor="black")


#30*np.array(y)

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(X,y, width = 0.3)
#plt.title('Histograma da frequência relativa acumulada')
plt.title('Histograma de frequência absoluta')
plt.show()