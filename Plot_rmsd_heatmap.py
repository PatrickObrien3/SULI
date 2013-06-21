import pylab as plt
import numpy as np
import matplotlib.cm as cm
rmsd=np.loadtxt('rmsd.out')

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('raw data')
im = ax1.imshow(rmsd[:,1:], cmap=cm.get_cmap('rainbow', 20))
fig.colorbar(im) 
plt.show()
