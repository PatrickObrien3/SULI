!/usr/bin/env python

"""
MDAnalysis example: Convert DCD trajectory into XTC
===================================================

This example shows how one can use MDAnalysis to convert between
different trajectory formats.

"""

from MDAnalysis.tests.datafiles import PDB_small, DCD
from MDAnalysis import Universe, Writer


import os.path

root, ext = os.path.splitext(os.path.basename(DCD))
PDBname = root + '.PDB'  # output format determined by extension

u = Universe(PDB_small, DCD)

# create a writer instance for the output trajectory
w = Writer(PDBname, u.trajectory.numatoms)

# loop through the trajectory and write a frame for every step
for ts in u.trajectory:
    w.write(ts)
    print "Converted frame %d" % ts.frame
w.close_trajectory()
print "Converted %r --> %r" % (DCD, PDBname)


