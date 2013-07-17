# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:54:11 2013

@author: jamesPino
"""
import os
import sys
import numpy as np


FILENAME=sys.argv[1] 

q=[]

b=1

for i in range(1,50001):
    print "loaded", i
    x,y=np.loadtxt(str(i)+'00.int', skiprows=1, usecols=(0,1), unpack=True)
    if b==1:
        I=x
        q=np.append(q,y,axis=1)      
        b=2
    else:
         q=np.column_stack((q,y))
print np.shape(q)
t=np.column_stack((I,q))
print t
#np.savetxt(FILENAME+'_All_IvsQ.csv',t, delimiter=',',fmt='%8.4f')
q_avg=np.average(q,axis=1) 
STD=np.std(q,axis=1)
IvsQ_xzy=np.column_stack((I,q_avg,STD))
np.savetxt(FILENAME+'__avg_XYZ.txt',IvsQ_xzy)
           

