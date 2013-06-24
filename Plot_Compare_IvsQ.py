import matplotlib.pyplot as plt
import numpy as np
import pylab

import os
import sys

FILE1=sys.argv[1]
FILE2=sys.argv[2]
FILE3=sys.argv[3]
def PLOT(FILE):
	x,y,z=np.loadtxt(FILE, usecols=(0,1,2), unpack=True)
	z=z/y.max()
	y=y/y.max()
	plt.errorbar(x,y,yerr=z,label=FILE[:-4])
	plt.legend(loc=3)
	plt.xlabel("Q",fontsize=32)
	plt.xlim([.05,.3])
	plt.ylim([0.0001,1])
	plt.ylabel("I(Q)",fontsize=32)
	plt.grid(True)
	pylab.yticks(fontsize=25)
	pylab.xticks(fontsize=25)
PLOT(FILE1)
PLOT(FILE2)
PLOT(FILE3)
plt.savefig('IvsQ_Compare.png',dpi=300)
plt.show()
