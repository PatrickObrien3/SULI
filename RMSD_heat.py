import os
import numpy as np

directory='/home/jms/EOM_06202013/ACTR/'
savedir='/home/jms/EOM_06202013/ACTR/RMSD/'
f=open('PDB_List.txt','w')
F=open('trajin.RMSD','w')
def renumber_for_distance(working_directory,save_directory):
    j=1
    for k in range(1,6):
        os.chdir(str(working_directory)+str(k))
        pdb,freq=np.loadtxt('best_curve001.txt',skiprows=2,unpack=True)
        print 'Model', str(k) ,' of 10'
        for i in pdb:
            print j
            print>>F, 'trajin  '+str(j)+'x.pdb'
            #print>>f, 'Model_  '+str(k)+'  /   '+str(int(i))+'.pdb is now '+str(j)+'.pdb'
            #os.system('ln -s    '+str(working_directory)+str(k)+'/Selected001/'+str(int(i))+'x.pdb  '+savedir+str(j)+'x.pdb')
            j+=1
        print 'Completed function run'
    print>>F,'rms2d @CA rmsout rmsd.out'
    return j
renumber_for_distance(directory,savedir)
f.close()
F.close()