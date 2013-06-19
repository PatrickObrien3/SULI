import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab

#y = np.loadtxt('outfile.txt')
x, y = np.loadtxt('out.txt', usecols=(0, 1), unpack=True)
print 'Range is ' ,  y.min(), y.max()
print 'Standard Dev is %8.4f' % y.std()
print 'Mean is %8.4f' %y.mean()



n, bins, patches = plt.hist(y, 100, normed=False, facecolor='blue', alpha=0.75)



plt.xlabel('Rg')
plt.ylabel('Count')
plt.title(r'Histogram of Rg')
#plt.xlim(9,35.0)
#plt.ylim(0,7000)
plt.grid(True)

plt.show()
