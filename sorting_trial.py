# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(JamesPino)s
"""

import numpy as np
import matplotlib.pylab 
import matplotlib.pyplot as plt


DATA=np.arange(1,60)

for i in range(1,60):
    y=np.random.normal(1,.1,59-i)
    for j in range(i):
        y=np.insert(y,0,0)
    DATA=np.column_stack((DATA,y))
datatype=[('frame_number','S10'),('distance',float)]


