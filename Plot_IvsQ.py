import matplotlib.mlab as mlab
import os
import numpy as np
import matplotlib.pyplot as plt
from math import *


for filename in os.listdir("."):
	if filename.endswith(".int")
		x, y =np.loadtxt(filename, skiprows=1, usecols =(0, 2), unpack=True )
		plt.semilogy(x, y)
plt.legend(loc='lower left')
plt.title("I(Q) vs Q")
plt.xlabel("Q")
plt.ylabel("I(Q)")
plt.show()
