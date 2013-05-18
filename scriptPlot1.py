import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from math import *


a=1; b=2
while a < b:
	filename = ('remd_' + str(a) + '00.int')
	a=a+1
	x, y =np.loadtxt(filename, skiprows=1, usecols =(0, 2), unpack=True )
	z = a
	plt.semilogy(x, y)
plt.show()



#a=0; b=98
#while a < b:
#	filename = ('adk_dims1_' + str(a) + '00.int')
#	a=a+1
#	x=np.loadtxt(filename, skiprows=1, usecols =(0,3))
#	plot(x)
#show()




