# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:32:02 2013

@author: ronaldholt
"""

from MDAnalysis import *
import numpy as np
from numpy import *
from numpy import linalg

u =Universe("/Users/ronaldholt/1JJS_autopsf.psf","/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS_1us.dcd")
asel = u.selectAtoms(' ( name CA ) ')
print asel

#---------------------------------
#  making the mass matrix
#---------------------------------
kg = asel.masses()*(1.6605388e-27)
masses = np.repeat(kg, 3)
mass_matrix = np.identity(len(masses))*masses

#--------------------------------
#  Preparing to read the CA position at every 5 steps in the traj
#--------------------------------
skip = 10
num_ts = u.trajectory.numframes/skip
num_coor = len(asel)*3
ca_pos = u.trajectory.timeseries(asel, skip=skip, format='fac')

#---------------------------------
# converting angstroms to meters and merging the xyz of timeseries 
#---------------------------------
ca = (1e-10)*(np.reshape(ca_pos, (num_ts, -1)))
print "ca", shape(ca)

#---------------------------------
#  making the covariance matrix
#---------------------------------
ca_avg = np.average(ca)
print "ca_av", shape(ca_avg)
ca2 = ca - ca_avg[np.newaxis,...]
print "ca2", shape(ca2)
ca_cov = np.zeros((num_coor, num_coor), np.float)
for ts in ca2:
    ca_cov += np.outer(ts, ts)
ca_cov /= num_ts
print "ca_cov", shape(ca_cov)
print "mass_matrix", shape(mass_matrix)

#---------------------------------
#  calculating the entropy
#---------------------------------
hplanck_bar = 6.6260755e-34/(2*np.pi) # J*s
k = (1.380658e-23)        # J/K
Avogadro = 6.0221367e23   # /mol
T = 300                   # Kelvin
term = (k*T**2)/(hplanck_bar**2)
print "term =", term
determ = linalg.det((term*np.dot(ca_cov,mass_matrix))+identity(len(mass_matrix)))
print "det = ", determ
S_ho = k/2*Avogadro*math.log(determ)
print "S_ho=", S_ho