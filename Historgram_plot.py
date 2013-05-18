import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab

x, y = np.loadtxt('out.txt', usecols=(0, 1), unpack=True)
y.max()
mu= y.mean()
sigma= y.std()



n, bins, patches = plt.hist(y, 100, normed=False, facecolor='green', alpha=0.75)



plt.xlabel('Rg')
plt.ylabel('Count')
plt.title(r'Histogram of Rg')

plt.grid(True)

plt.show()
