# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:35:50 2013

@author: ronaldholt
"""



"""
MDAnalysis example: Simple blocking analysis
============================================

Calculate the radius of gyration for increasing number of blocks over
a trajectory.

See: H. Flyvbjerg and H. G. Petersen. Error estimates on averages of
correlated data. 91(1):461-466, 1989.

"""

import numpy
import MDAnalysis

def blocked(universe, nblocks, analyze):
    size = universe.trajectory.numframes/nblocks
    blocks = []
    for block in xrange(nblocks):
        a = []
        for ts in u.trajectory[block*size:(block+1)*size]:
            a.append(analyze(universe))
        blocks.append(numpy.average(a))
    blockaverage = numpy.average(blocks)
    blockstd = numpy.std(blocks)

    return nblocks, size, blockaverage, blockstd

def rgyr(universe):
    return universe.selectAtoms('protein').radiusOfGyration()

import matplotlib
matplotlib.use('agg')  # no interactive plotting, only save figures
from pylab import errorbar, subplot, xlabel, ylabel, savefig
u = MDAnalysis.Universe("/Users/ronaldholt/Google Drive/ORNL Research/1JJS.prmtop","/Users/ronaldholt/Google Drive/ORNL Research/1JJS_1us.dcd")
results = []
for nblocks in xrange(2,10):
    results.append(blocked(u, nblocks, rgyr))
    r = numpy.array(results)
    subplot(211)
    errorbar(r[:,0], r[:,2], yerr=r[:,3])
    xlabel("number of blocks")
    ylabel(r"$\langle R_{\rm{gyr}} \rangle$ ($\AA$)")
    subplot(212)
    errorbar(r[:,1], r[:,2], yerr=r[:,3])
    xlabel("block size")
    ylabel(r"$\langle R_{\rm{gyr}} \rangle$ ($\AA$)")
    savefig("blocks.pdf")
    savefig("blocks.png")
    print "Wrote ./figures/blocks.{pdf,png}" % vars()