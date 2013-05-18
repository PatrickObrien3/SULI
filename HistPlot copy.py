# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:07:27 2013

Must add delimiter=',' for a CSV 

@author: ronaldholt
"""

def Hist(filename):
    import numpy as np
    import matplotlib.pyplot as plt 

    x, y = np.loadtxt(filename,dtype='float',usecols=(0, 1), unpack=True)
    y.max()
    y.mean()
    y.std()
    plt.hist(y, 100, normed=False, facecolor='green', alpha=0.75)
    plt.xlabel('Rg')
    plt.ylabel('Count')
    plt.title(r'Histogram of Rg')
    plt.grid(True)
    plt.savefig('/Users/ronaldholt/Desktop/Hist.png')
    plt.show()
if __name__ == "__main__":
    import sys
    Hist((sys.argv[1]))