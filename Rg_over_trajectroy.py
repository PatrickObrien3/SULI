# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:37 2013


This script is for basic information of the distance between N and C terminals of a protein and its radius of gyration along a trajectory.

You must define the topology and trajectroy path along with the filename where you want the data to be store.
Also the name of optional figures to be saved.

@author: JamesPino
"""
import sys
from scipy import interpolate
from MDAnalysis import Universe 
import numpy as np
import matplotlib.pyplot as plt 
import numpy.linalg

if '-h' in sys.argv:
	print 'Input topology file first and dcd file second and the new filename output 3rd.It will write the Raius of Gyration and N to C terminal distance.'
	sys.exit()               
               
       
TOP = '/home/jms/REX-MD/2KKJ01.top'             
DCD = '/home/jms/REX-MD/remd_all_tmp.dcd'
FILENAME="2KKJ"


         
u =Universe(TOP,DCD)
# Extract position of N and C terminal can calculate distace, write it to a file along with the radius of gyration (RG)

#f=open(str(FILENAME) +'Rg_data.txt','w')


#bb = u.selectAtoms('protein and backbone')  # a selection (a AtomGroup)
#for ts in u.trajectory:     # iterate through all frames
#  rgyr = bb.radiusOfGyration()  # method of a AtomGroup; updates with each frame
#  print >>f, " %d  %f " % (ts.frame,rgyr)
#f.close()
#Extract distance of N to C terminal and RG overtrajectory
         
x,y= np.loadtxt(str(FILENAME)+'Rg_data.txt', usecols=(0,1),unpack=True)
step=int(len(x))

xnew = np.arange(1,step,500)

F = interpolate.interp1d(x,y)   #smooth the line
fig=plt.figure(figsize=(8,8),dpi=80,facecolor='w',edgecolor='k')

plt.subplot(211)
plt.plot(xnew,F(xnew),'-',label= 'Rg')
plt.xlabel('Time ')
plt.ylabel('Angstrom')
plt.legend( loc="upper right")
plt.title(r' Rg over time')




#Plot a histogram of Rg over the trajectory
plt.subplot(212)
plt.hist(y,100,normed=False, facecolor='blue',alpha=.5)
plt.xlabel('Rg')
plt.ylabel('Count')
plt.title('Histogram of '+str(FILENAME)+' Rg')
plt.savefig(str(FILENAME)+'_Hist_Rg.png')
plt.show()
