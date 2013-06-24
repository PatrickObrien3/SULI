import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
import os
import sys

FILE1=sys.argv[1]
FILE2=sys.argv[2]
FILE3=sys.argv[3]
FILE4=sys.argv[4]
def LOAD(FILE):
    x, y = np.loadtxt(FILE, usecols=(0, 1), unpack=True)
    print 'Range is ' ,  y.min(), y.max()
    print 'Standard Dev is %8.4f' % y.std()
    print 'Mean is %8.4f' %y.mean()
    n, bins, patches = plt.hist(y, 100, normed=1,label=FILE[:-4], alpha=0.75)
    plt.xlabel('Rg')
    plt.ylabel('Count')
    plt.title(r'Histogram of Rg')
#plt.xlim(9,35.0)
#plt.ylim(0,7000)
    plt.grid(True)
    #plt.show()
    plt.legend(loc=0)
LOAD(FILE1)
LOAD(FILE2)
LOAD(FILE3)
LOAD(FILE4)
plt.show()
