# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.pylab as plt


os.chdir('/Users/ronaldholt/Desktop/ORNL/Csub_Files')
lis_files= os.listdir(".")
I=1
for filename in lis_files:
    if filename.startswith("150mM"):
        plt.subplot(411)        
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.semilogy(I,q,label=filename)
        plt.legend(loc=0)
        plt.title("I(Q) vs. Q")
        plt.xlim([.1,.3])
        plt.ylim([0,1])
    if filename.startswith("500mM"):
        plt.subplot(412)        
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.semilogy(I,q,label=filename)
        plt.legend(loc=0)
        plt.xlim([.1,.3])
        plt.ylim([0,1])
    if filename.startswith("50mM"):
        plt.subplot(413)
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.xlim([.1,.3])
        plt.ylim([0,1])
        plt.semilogy(I,q,label=filename)
    if filename.startswith("dEG" or "0per"):
        plt.subplot(414)
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.semilogy(I,q,label=filename)
        plt.legend(loc=0)
        plt.xlabel("Q")
        plt.xlim([.1,.3])
        plt.ylim([0,1])
        plt.ylabel("I(Q)")
plt.show()
