import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import os
import sys

FILE1=sys.argv[1]
FILE2=sys.argv[2]
#FILE3=sys.argv[3]
#FILE4=sys.argv[4]
#FILE5=sys.argv[5]
def PLOT(FILE,LAN):
    x,y,z = np.loadtxt(FILE, usecols=(0, 1,2), unpack=True)
    z=z/y.max()
    y=y/y.max()
    plt.xlabel("Q")
    plt.ylabel("I(Q)")
    plt.grid(True)
    plt.errorbar(x,y,yerr=z,label=LAN)
    plt.legend(loc=0)
def PLOT1(FILE,LAN):
    x,y,z = np.loadtxt(FILE, skiprows=2,usecols=(0, 1,2), unpack=True)
    z=z/y.max()
    y=y/y.max()
    plt.xlabel("Q")
    plt.ylabel("I(Q)")
    plt.grid(True)
    plt.errorbar(x,y,yerr=z,label=LAN)
    plt.legend(loc=0)
PLOT(FILE1,'MD averaged NCBD/ACTR Complex')
#PLOT(FILE2,'1KBH2')
#PLOT(FILE3,'ACTR')
PLOT1(FILE2,'Experimental NCBD/ACTR Complex')
#PLOT1(FILE4,'Experimental ACTR')
plt.savefig('IvsQ_Complex_Compare.png',dpi=300)
plt.show()