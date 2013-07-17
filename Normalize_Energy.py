# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(JamesPino)s
"""

import numpy as np


def normalize(array,imin=-3,imax=3):
    dmin=array.min()
    dmax=array.max()
    return imin + (imax-imin) * (array-dmin) / (dmax-dmin)
    

def extract_energy(filename):
    frame,TE=np.loadtxt(filename,usecols=(0,4),skiprows=1,unpack=True)
    print "Number of frames",np.shape(frame)
    NORM=normalize(TE)
    Norm_data=np.column_stack((frame,NORM))
    np.savetxt("Norm_Energy.txt",Norm_data)
    
    
extract_energy("Energy.txt")
