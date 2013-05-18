# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:48:04 2013

@author: ronaldholt
"""

from scipy import interpolate

from MDAnalysis import Universe 
from MDAnalysis import analysis
import numpy as np
import matplotlib.pyplot as plt 
import numpy.linalg
   
TOP = '/Users/ronaldholt/1JJS_autopsf.psf'              
DCD = '/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS_1us.dcd'    
#
FILENAME="1JJS_1us"

         
u =Universe(TOP,DCD)
analysis.rms.RMSD(u,  select='all', filename='rmsd.dat', mass_weighted=False, tol_mass=0.1, ref_frame=0)