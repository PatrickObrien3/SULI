# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:27:37 2013

@author: ronaldholt
"""


from MDAnalysis import *

import numpy.linalg
                 # always start with a Universe
u =Universe("/Users/ronaldholt/1JJS_autopsf.psf","/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS_1us.dcd")

nterm = u.P1.N[0]   # can access structure via segid (s4AKE) and atom name
cterm = u.P1.C[-1]  # ... takes the last atom named 'C'
bb = u.selectAtoms('protein and backbone')  # a selection (a AtomGroup)
for ts in u.trajectory:     # iterate through all frames
  r = cterm.pos - nterm.pos # end-to-end vector from atom positions
  d = numpy.linalg.norm(r)  # end-to-end distance
  rgyr = bb.radiusOfGyration()  # method of a AtomGroup; updates with each frame
  print "frame = %d: d = %f Angstroem, Rgyr = %f Angstroem" % (ts.frame, d, rgyr)