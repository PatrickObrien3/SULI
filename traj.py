# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:11:38 2013

@author: ronaldholt
"""

#!/usr/bin/env python
# Example script, part of MDAnalysis
"""
RMSD to a reference structure
=============================

Simple example implementation that shows how to calculate the RMSD
over a trajectory.

"""

import numpy
import MDAnalysis

import sys

from MDAnalysis.analysis.align import rmsd,  qcp

def rmsd_traj(traj, ref, **kwargs):
    select = kwargs.pop('select', 'backbone')
    selections = kwargs.pop('selections', {'reference':select,'mobile':select})

    frames = traj.trajectory
    nframes = len(frames)
    rmsd = numpy.zeros((nframes,))

    ref_atoms = ref.selectAtoms(selections['reference'])
    traj_atoms = traj.selectAtoms(selections['mobile'])
    natoms = traj_atoms.numberOfAtoms()

    # if performing a mass-weighted alignment/rmsd calculation
    #masses = ref_atoms.masses()
    #weight = masses/numpy.mean(masses)

    # reference centre of mass system
    ref_com = ref_atoms.centerOfMass()
    ref_coordinates = ref_atoms.coordinates() - ref_com

    # allocate the array for selection atom coords
    traj_coordinates = traj_atoms.coordinates().copy()

    # R: rotation matrix that aligns r-r_com, x~-x~com
    #    (x~: selected coordinates, x: all coordinates)
    # Final transformed traj coordinates: x' = (x-x~_com)*R + ref_com
    for k,ts in enumerate(frames):
        # shift coordinates for rotation fitting
        # selection is updated with the time frame
        x_com = traj_atoms.centerOfMass()
        traj_coordinates[:] = traj_atoms.coordinates() - x_com

        ### NOTE: If you're only interested in RMSD and never in the
        ###       transformation matrix then set 'R = None' instead of
        ###       allocating an array.
        R = numpy.zeros((9,),dtype=numpy.float64)

        # Need to transpose coordinates such that the coordinate array is
        # 3xN instead of Nx3. Also qcp requires that the dtype be float64
        a = ref_coordinates.T.astype('float64')
        b = traj_coordinates.T.astype('float64')
        rmsd[k] = qcp.CalcRMSDRotationalMatrix(a,b,natoms,R,None)

        print "%5d  %8.3f A" % (k, rmsd[k])

        ### only comment in if you want to manipulate or write out
        ### the fitted trajectory
        ###
        ## R = numpy.matrix(R.reshape(3,3))
        ##
        ###  Transform each atom in the trajectory (use inplace ops to avoid copying arrays)
        ## ts._pos   -= x_com
        ## ts._pos[:] = ts._pos * R # R acts to the left & is broadcasted N times.
        ## ts._pos   += ref_com

    return rmsd

if __name__ == '__main__':
   from MDAnalysis import *
#   from MDAnalysis.tests.datafiles import PSF, DCD, PDB_small
   ref = Universe("/Users/ronaldholt/Desktop/ORNL/NCBD/PDB/2KKJ.pdb")   # reference structure 4AKE
   trj = Universe("/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS.prmtop","/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS_1us.dcd")        # trajectory of change 1AKE->4AKE

   print "CA RMSD for %(DCD)r versus %(PDB_small)r" % vars()
   rmsds1 = rmsd_traj(trj, ref, select='name CA')

   print "CA RMSD for %(DCD)r versus first frame" % vars()
#   ref = Universe(PSF, DCD)
   ref.trajectory[0]  # go to first frame
   rmsds2 = rmsd_traj(trj, ref, select='name CA')

   print "CA RMSD for %(DCD)r versus last frame" % vars()
#   ref = Universe(PSF, DCD)
   ref.trajectory[-1]  # go to last frame
   rmsds3 = rmsd_traj(trj, ref, select='name CA')

   try:
       import matplotlib
       matplotlib.use('agg')  # fast windowless plotting
       from pylab import plot, xlabel, ylabel, legend, title, savefig
       plot(rmsds1, linewidth=2, color='black', label='4AKE')
       plot(rmsds2, linewidth=2, color='red', label='first frame')
       plot(rmsds3, linewidth=2, color='blue', label='last frame')

       xlabel('trajectory frame')
       ylabel(r'root mean square distance ($\mathrm{\AA}$)')
       title('DIMS trajectory of Adenylate Kinase from 1AKE to 4AKE')
       legend(loc='best')
       savefig("figures/rmsd.pdf")
       savefig("figures/rmsd.png")
       print "Wrote figures/rmsd.{pdf,png}"
   except ImportError:
       print "No pylab/matplotlib, no graphs."