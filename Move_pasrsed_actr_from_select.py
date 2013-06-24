import os
import numpy as np

directory='/home/jms/1KBH/ANAL/EOM_Complex/Models_'

f=open('PDB_List.txt','w')
run=1
def renumber_for_distance(working_directory):
    j=1
    for k in range(1,11):
        j=1
        WORK=str(working_directory)+str(k)+'/Data/Selected00'+str(run)
        os.chdir(WORK)
        os.mkdir(WORK+'/parsed')
        pdb,freq=np.loadtxt('../GA00'+str(run)+'/best_curve00'+str(run)+'.txt',skiprows=2,unpack=True)
        print 'Model', str(k) ,' of 10'
        for i in pdb:
            print j
            print>>f, 'Model_  '+str(k)+'  /   '+str(int(i))+'x00.log is now '+str(j)+'x00.log'
            os.system('ln -s    '+str(WORK)+'/p_actr/'+str(int(i))+'x.pdb  '+WORK+'/parsed/.')
            os.system('ln -s    '+str(WORK)+'/p_actr/'+str(int(i))+'x.pdb  '+WORK+'/parsed/'+str(j)+'x00.log')
            
            j+=1
        print 'Completed function run'
    return j
renumber_for_distance(directory)
f.close()