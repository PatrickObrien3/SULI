# -*- coding: utf-8 -*-
"""
Created on 

@author:JamesPino
"""

import numpy as np
import pylab as plt

SS=np.loadtxt('SS.sum',skiprows=1)

plt.bar(SS[:,0],SS[:,1],color='blue',label='3-10-Helix',alpha=.5 )
plt.bar(SS[:,0],SS[:,2],color='red',label='alpha Helix',alpha=.5)
plt.bar(SS[:,0],SS[:,3],color='green',label='PI-Helix',alpha=.5)
plt.bar(SS[:,0],SS[:,4],color='black',label='paralle sheet',alpha=.5)
plt.bar(SS[:,0],SS[:,5],color='pink',label='anti parrallel',alpha=.5)
plt.legend(loc=0)

plt.show()