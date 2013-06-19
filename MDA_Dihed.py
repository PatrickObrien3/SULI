# -*- coding: utf-8 -*-


import numpy
import sys
from MDAnalysis import Universe, collection, Timeseries
try:
    import matplotlib
    matplotlib.use('agg')  # no interactive plotting, only save figures
    from pylab import errorbar, legend, xlabel, ylabel, savefig, clf, gca, draw
    have_matplotlib = True
except ImportError:
    have_matplotlib = False

import os

TOP=sys.argv[1]
DCD=sys.argv[2]
FILE=sys.argv[3]

os.system('pwd')
universe= Universe(TOP,DCD)
print universe.atoms
protein=universe.selectAtoms("protein")
list(protein)

numresidues = protein.numberOfResidues()

collection.clear()
for res in range(2, numresidues-1):
    print "Processing residue %d" % res
    #  selection of the atoms involved for the phi for resid '%d' %res
    ## selectAtoms("atom 4AKE %d C"%(res-1), "atom 4AKE %d N"%res, "atom %d 4AKE CA"%res, "atom 4AKE %d C" % res)
    phi_sel = universe.residues[res].phi_selection()

    #  selection of the atoms involved for the psi for resid '%d' %res
    psi_sel = universe.residues[res].psi_selection()

    # collect the timeseries of a dihedral
    collection.addTimeseries(Timeseries.Dihedral(phi_sel))
    collection.addTimeseries(Timeseries.Dihedral(psi_sel))

# iterate through trajectory and compute (see docs for start/stop/skip options)
collection.compute(universe.trajectory)

# finding the avg and stdev for each residue
phi = []
psi = []
for data_phi in collection[0::2]:
    dih = numpy.rad2deg(data_phi[0])
    phi.append([dih.mean(), dih.std()])
for data_psi in collection[1::2]:
    dih = numpy.rad2deg(data_psi[0])
    psi.append([dih.mean(), dih.std()])

# making an array for phi and psi data
res = numpy.arange(2, numresidues-1)
phi = numpy.array(phi)
psi = numpy.array(psi)

# plotting and saving the dihe for each resid
if have_matplotlib:
    clf()
    a = errorbar(res, phi[:,0], phi[:,1], fmt='ro', label=r"$\Phi$")
    b = errorbar(res, psi[:,0], psi[:,1], fmt='bs', label=r"$\Psi$")
    legend((a[0], b[0]), (r"$\Phi$", r"$\Psi$"))
    xlabel("Residue number")
    ylabel(r"Dihedral in degrees")
    savefig(FILE+"_backbone_dihedrals_residue.png")
    print "Figures saved as backbone_dihedrals_residue.{pdf,png}"

    # Ramachandran plot
    clf()
    errorbar(phi[:,0], psi[:,0], xerr=phi[:,1], yerr=psi[:,1], fmt="o")
    xlabel(r"$\Phi$")
    ylabel(r"$\Psi$")
    ax = gca()
    degreeFormatter = matplotlib.ticker.FormatStrFormatter(r'%d$^\circ$')
    ax.xaxis.set_major_formatter(degreeFormatter)
    ax.yaxis.set_major_formatter(degreeFormatter)
    draw()

    
    savefig(FILE+"_backbone_dihedrals_ramachandran.png")
    print "Figures saved as backbone_dihedrals_ramachandran.{pdf,png}"
