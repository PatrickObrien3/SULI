# -*- coding: utf-8 -*-
"""
Created on 

1. Take the trajectory and turn it into pdbs
2. Rename the pdb files as 1x.pdb ... Nx.pdb
3. Calculate the secondary strucutre of the trajectory
4. Run cryson,
5. Run  shiftx on pdbs
6. Extract all C, Calpha, and Halpha chemical shifts from out files
7. Make EOM analysis folders where you split up the trajectorys over 10 sample
of 10,000. links pdb files, log files, and .int files from cryson 
8. Make onefile2.l86 list of all intensity and gajoe.l86 for all log files
8.Run EOM gajoe.l86 on pdbs using basic parameters
9. Move all selected files from GA00*/best_curve00*.txt file, this will
make new directoy with only select models which you can look at the
chemicalshifts and sec structure to compare with standard
10. Link all EOM select models from all samples into one folder and rename them
from 1.... N , run ptraj and get a heat map of RMSD. Remeber to turn swapon -a.


@author:JamesPino
"""

import os


number=50 #number for sample
List=['1JJS1','1JJS2','1JJS3']
#List=['1JJS3','1JJS2']
#List=['ACTR1','ACTR2']
#List=['1KBH3','1KBH4']
for i in List:
    os.chdir('/home/jms/'+str(i[:4])+'/'+str(i[-1])+'/ANAL/') #change to directory where DCD files are
    os.system('ptraj '+str(i)+'_ww.prmtop trajin.analysis ') #produce the PDB files from DCD
    os.system('python ~/Projects/SULI/RenameRemoveChar.py  x 2  ') #rename the PDB files
    os.system('python ~/Projects/SULI/Cryson_script.py ') #run cryson on the PDB files
    os.system('python ~/Projects/SULI/Chem_shiftx.py ') #run chemical shift on all
    os.system('python ~/Projects/SULI/sed.py ' +str(i[:4]))#sed all chemical shift files

#os.system('python ~/Projects/EOM_prep.py')
#os.sysmte('python ~/Projects/