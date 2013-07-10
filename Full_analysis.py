# -*- coding: utf-8 -*-
"""
Created on 

1. Take the trajectory and turn it into pdbs
2.Rename the pdb files as 1x.pdb ... Nx.pdb
3.calculate the secondary strucutre of the trajectory
4. Run cryson,
5. Run  shiftx on pdbs
6. Extract all C Calpha and Halpha from out files
7. Make EOM analysis folders where you split u the trajectorys over 10 sample
of 10,000 out. links pdb files, log files, and .int files from cryson 
8. Make onefile2.l86 list of all intensity and gajoe.l86 for all log files
8.Run EOM on pdbs using basic parameters
9. Move all selected files from GA00*/best_curve00*.txt file, this will
make new directoy with only select models which you can look at the
chemicalshifts and sec structure to compare with standard
10. Move all EOM select models from all samples into one folder and rename them
from 1.... N , run ptraj and get a heat map of RMSD. Remeber to turn swapon -a.


@author:JamesPino
"""

import os
import sys


os.system('ptraj 1KBH_ww.prmtop trajin.analysis')
os.system('python ~/Projects/SULI/RenameRemoveChar.py X 2')
os.system('python ~/Projects/SULI/Cryson_script.py')
os.system('python ~/Projects/Chem_shiftx.py ')
os.system('python ~/Projects/')
os.system('python ~/Projects/EOM_prep.py')