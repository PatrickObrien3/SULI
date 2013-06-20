# -*- coding: utf-8 -*-
"""
Created on 

@author:JamesPino
"""

import os
import numpy as p


for i in range(1,4238):
    for k in range(1,4238):
        main = Universe('/home/jms/EOM_06202013/Complex_all/RMSD'+str(i)','/home/jms/EOM_0602013/Complex_all/RMSD/'+str(i))
        reference=Universe('/home/jms/EOM_0602013/Complex_all/RMSD/'+str(k),'/home/jms/EOM_0602013/Complex_all/RMSD/'+str(k))        
        bb = main.selectAtoms('backbone')
        A = bb.coordinates()  # coordinates of first frame
        cc=reference.selectAtoms('backbone')        
        B = cc.coordinates()  # coordinates of last frame
        rmsd(A,B)

STD_Matrix=np.arange(1,60)
Dist_Matrix=np.arange(1,60)
for i in range(1,60):
    avg=[]
    std=[]
    for j in range(i+1,60):
        print str(i)+'_'+str(j)+'.out'
        x,y=np.loadtxt(str(i)+'_'+str(j)+'.out',usecols=(0,1),unpack=True)
        tmp_a=np.average(y)
        tmp_b=np.std(y)        
        avg=np.append(avg,tmp_a)
        std=np.append(std,tmp_b)
    