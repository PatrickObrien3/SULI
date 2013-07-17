# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:45:53 2013

@author: jms
"""

import numpy as np
import os, sys

PDB,distance=np.loadtxt(sys.arvg[1],unpack=True)
Selected=sys.argv[2]
for i in PDB:
    os.system('ln -s  '+str(i)+'x.pdb   '+str(Selected))