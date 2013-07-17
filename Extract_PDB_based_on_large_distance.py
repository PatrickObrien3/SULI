# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:44:44 2013

@author: jms
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

colormap=cm.gist_rainbow
distances = (13, 17, 33, 43)
x,r1 =np.loadtxt('13_17.out',unpack=True)
x,r2 =np.loadtxt('13_33.out',unpack=True)
x,r3 =np.loadtxt('13_43.out',unpack=True)
x,r4 =np.loadtxt('17_33.out',unpack=True)
x,r5 =np.loadtxt('17_43.out',unpack=True)
x,r6 =np.loadtxt('33_43.out',unpack=True)

def extract(frame,distance1,distance2,value1,value2,value3,value4):
    pdb=np.zeros((1,2))
    PDB=[]
    for j in range(0,len(r1)):
        if distance1[j]>= float(value1):
            if distance1[j]<=float(value1+value3):
                if distance1[j]>=float(value2): 
                    if distance2[j]<=float(value2+value4):
                        print 'trajin 1JJS.dcd '+str(int(frame[j]))+' '+str(int(frame[j]))
    print 'trajout x pdb'
    #np.savetxt('PDB_list_greaterthan'+str(value)+'.txt',pdb,fmt='%d %4e')
extract(x,r1,r2,8.5,9.0,0.65,0.65)

#PDB,distance=np.loadtxt(sys.arvg[1],unpack=True)
