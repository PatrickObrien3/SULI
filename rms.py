import matplotlib.mlab as mlab
import os
import numpy as np
import matplotlib.pyplot as plt
from math import *




filename="~/Desktop/rms.log"
x, y =np.loadtxt(filename, usecols =(0, 2), unpack=True )
		
plt.legend(loc='lower left')
plt.title("I(Q) vs Q")
plt.xlabel("Q")
plt.ylabel("I(Q)")
plt.show()
