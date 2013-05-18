# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:54:11 2013


"""
import os
import sys
import numpy as np

#TOP = sys.argv[1]
#DCD = sys.argv[2]
#FILENAME=sys.argv[3] 
os.chdir('/Users/ronaldholt/Google_Drive/ORNL_Research/IvsQ_SANS/')
a=[]
b=1
li=['I(q)']
for filename in os.listdir("."):
    if filename.endswith(".txt"):
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        if b==1:
            li.append(filename)
            a=np.column_stack((x,y))
            b=2
        else:
            a=np.column_stack((a,y))
            li.append(filename)
li=np.transpose(li)
print np.shape(a)
print np.shape(li)
t=np.vstack((li,a))
print t

np.savetxt('All_IvsQ.csv',t, delimiter=',',fmt="    %5ss")
#np.savetxt('IvsQ_all',a)

