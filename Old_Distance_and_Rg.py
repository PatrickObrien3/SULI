# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:37 2013


This script is for basic understanding of the distance between N and C terminus of a protein and its radius of gyration along a trajectory.

You must define the topology and trajectroy path along with the filename where you want the data to be store.
Also the name of optional figures to be saved.

@author: JamesPino
"""

from scipy import interpolate
from MDAnalysis import Universe 
import numpy as np
import matplotlib.pyplot as plt 
import numpy.linalg
               
               
               
TOP = '/Users/ronaldholt/1JJS_autopsf.psf'              
DCD = '/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS_1us.dcd'    

FILENAME="1JJS_1us"

         
#u =Universe(TOP,DCD)
## Extract position of N and C terminal can calculate distace, write it to a file along with the radius of gyration (RG)
#a=1
#f=open(str(FILENAME) +'Rg_data.txt','w')
#
#nterm = u.P1.N[0]   # can access structure via segid (s4AKE) and atom name
#cterm = u.P1.C[-1]  # ... takes the last atom named 'C'
#bb = u.selectAtoms('protein and backbone')  # a selection (a AtomGroup)
#for ts in u.trajectory:     # iterate through all frames
#  r = cterm.pos - nterm.pos # end-to-end vector from atom positions
#  d = numpy.linalg.norm(r)  # end-to-end distance
#  rgyr = bb.radiusOfGyration()  # method of a AtomGroup; updates with each frame
#  print >>f, " %d %f %f " % (ts.frame, d, rgyr)
#f.close()
# Extract distance of N to C terminal and RG overtrajectory
x, y,z = np.loadtxt(str(FILENAME)+'Rg_data.txt', usecols=(0,1,2),unpack=True)
Xnew = np.arange(1,50000,500)
xnew = np.arange(1,50000,100)
f = interpolate.interp1d(x,y) #smooth th line 
F = interpolate.interp1d(x,z)   #smooth the line

plt.plot(Xnew,f(Xnew),'-',label='N term to C term Dist')
plt.xlabel('Time ')
plt.ylabel('Distance')
plt.legend( loc='upper center')
plt.title('N to C distane of '+str(FILENAME))
plt.savefig(str(FILENAME)+'N_C_dist.png')
plt.show()


plt.plot(xnew,F(xnew),'-',label= 'Rg')
plt.xlabel('Time ')
plt.ylabel('Angstrom')
plt.legend( loc="upper right")
plt.title(r'1JJS_1us Rg')
plt.savefig(str(FILENAME)+'_RgvsTime.png')
plt.show()

#Plot a histogram of the End to End Distance over over trajectory
plt.hist(y, 100, normed=False, facecolor='green', alpha=0.75)
plt.xlabel('Distance')
plt.ylabel('Count')
plt.title(r'Histogram of 1JJS_1us End to end distance')
plt.savefig(str(FILENAME)+'_Hist_Dist.png')
plt.show()

#Plot a histogram of Rg over the trajectory
plt.hist(z,100,normed=False, facecolor='blue',alpha=.5)
plt.xlabel('Rg')
plt.ylabel('Count')
plt.title('Histogram of '+str(FILENAME)+' Rg')
plt.savefig(str(FILENAME)+'_Hist_Rg.png')
plt.show()




