# -*- coding: utf-8 -*-
"""
Created on 


Creates half a heat map of RMSD between all pdb files. This is used to show that
the selected models from each run of EOM are similar and we can use one of the 
selected models and it should represent the entire trajectory.
@author:JamesPino
"""

import os
import numpy as np
from MDAnalysis import *
from MDAnalysis.analysis.align import rmsd


RMSD_Matrix=np.arange(1,4239)

f=open('rmsd.txt','w')
for i in range(1,4239):
    tmp_rmsd=[]
    for k in range(i+1,4239):
        main = Universe(str(i)+"x.pdb" )
        reference=Universe(str(k)+"x.pdb" )       
        bb = main.selectAtoms('backbone') 
        A = bb.coordinates()  # coordinates of main frame
        cc=reference.selectAtoms('backbone')        
        B = cc.coordinates()  # coordinates of reference frame
        x = rmsd(A,B);#print>>f , i , k , x;
        print  i , k , x;
        tmp_rmsd=np.append(tmp_rmsd,x)
    for j in range(i):
        tmp_rmsd=np.insert(tmp_rmsd,0,0)
    RMSD_Matrix=np.column_stack((RMSD_Matrix,tmp_rmsd))
np.savetxt('RMSD_MATRIX.out',RMSD_Matrix)

