# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:40:26 2013

@author: ronaldholt
"""


from MDAnalysis import *
from MDAnalysis.analysis.align import *
import numpy as np
from numpy import linalg

u =Universe("/Users/ronaldholt/1JJS_autopsf.psf","/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS_1us.dcd")
asel = u.selectAtoms('segid P1 and backbone and not type O')

masses = np.repeat(asel.masses(), 3)
mass_matrix = np.sqrt(np.identity(len(masses))*masses)

skip = 1
num_ts = u.trajectory.numframes/skip
num_coor = len(asel)*3

ca_pos = u.trajectory.timeseries(asel, skip=skip, format='fac')
collection.addTimeseries(Timeseries.CenterOfMass(asel))
ca_com = np.transpose(u.trajectory.correl(collection, skip=skip))

# Recenter on center of mass of selection
ca_pos -= ca_com[:,np.newaxis]
kg = asel.masses()*(1.6605388e-27)
# Remove rotational degrees of freedom
ref = ca_pos[0]
for coor in ca_pos[1:]:
    rotmatrix =rotation_matrix(coor, ref, kg)
    coor[:] =coor*rotmatrix

ca = np.reshape(ca_pos, (num_ts, -1))
ca_avg = np.average(ca)
ca2 = ca - ca_avg[np.newaxis,:]
ca_cov = np.zeros((num_coor, num_coor),np.float)
for ts in ca2:
    ca_cov += np.outerproduct(ts, ts)
ca_cov /= num_ts
ca_cov1 = ca_cov*mass_matrix
del ca_cov
ca_cov2 = np.dot(mass_matrix, ca_cov1)
del ca_cov1

N_av = 6.0221367e23
hplanck_bar = 6.6260755e-34/(2*np.pi)
k =  1.3806580000000001e-23
T = 300 # kelvin
eigenv, eigenvec = np.linalg.eigvals(ca_cov2)
real = [e.real/100. for e in eigenv]
f = file('eigenval.dat', 'w')
for i, val in enumerate(real):
    f.write(`i+1` + '\t' + `val` + '\n')
f.close()

eigenval = eigenv*1.6605402e-27*1e-20
omega_i = np.sqrt(k*T/(eigenval))

term = (hplanck_bar*omega_i)/(k*T)
summation_terms = (term/(np.exp(term)-1.))-np.log(1.-Numeric.exp(-term))
S_ho = k*N_av*np.sum(summation_terms)