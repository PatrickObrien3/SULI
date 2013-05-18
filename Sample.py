# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import os
import matplotlib.pylab as plt
from math import*
os.chdir('/Users/ronaldholt/Desktop/ORNL/SANS_NCBD_Reduced')
for filename in os.listdir("."):
    if filename.endswith(".txt"):
    	x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
    	x=x[27:91]
    	z=y[27:91]
    	plt.loglog(x,z,label=filename)
plt.legend(loc='lower left')
plt.title("I(Q) vs. Q")
plt.xlabel("Q")
plt.xlim([.1,.3])
plt.ylabel("I(Q)")
plt.show()

