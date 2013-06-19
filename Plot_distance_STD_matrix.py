import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys


FILE1=sys.argv[1]
FILE2=sys.argv[2]


Dist_Matrix=np.loadtxt(FILE1)
STD_Matrix=np.loadtxt(FILE2)

fig=plt.figure(figsize=(10,10))
fig.add_subplot(121)
plt.imshow(Dist_Matrix[:,1:])
plt.xlabel('Residue Number')
plt.title(r'Distance Matrix Average')
plt.colorbar()
fig.add_subplot(122)
plt.imshow(STD_Matrix[:,1:])
plt.xlabel('Residue Number')
plt.title(r'Standard Deviation of Distance Matrix')
plt.colorbar()
plt.savefig('CA_CA_distMat.png',dpi=200)
plt.show()
