import numpy as np
#import matplotlib.pyplot as plt
import os

#os.chdir('/home/jms/Desktop/TXT/')
os.system('rm list')
os.system('ls -1 *.txt >> list')
HA=[]
Ca=[]
Res=[]
C=[]
s=0
data_list=np.loadtxt('list',dtype=str)
for i in data_list:
    if i.endswith('.txt'):
        print i
        #data=np.loadtxt(i,skiprows=2,usecols=(0,2,5,7),)  
        if s==0:
            
	    data=np.loadtxt(i,skiprows=2,usecols=(0,2,5,7),)
	    Res=np.concatenate((Res,data[:,0]),axis=0)
            HA=data[:,1]
            Ca=data[:,2]
            C=data[:,3]
            s=s+1
        else:
	    data=np.loadtxt(i,skiprows=2,usecols=(2,5,7),)
            HA=np.column_stack((HA,data[:,0]))
            Ca=np.column_stack((Ca,data[:,1]))
            C=np.column_stack((C,data[:,2]))

HA_avg=np.average(HA,axis=1)
Ca_avg=np.average(Ca,axis=1)
C_avg=np.average(C,axis=1)

HA_std=np.std(HA,axis=1)
CA_std=np.std(Ca,axis=1)
C_std=np.std(C,axis=1)

B_HA=np.column_stack((Res,HA_avg,HA_std))
B_CA=np.column_stack((Res,Ca_avg,CA_std))
B_C=np.column_stack((Res,C_avg,C_std))


np.savetxt('HA_all.txt',HA)
np.savetxt('Ca_all.txt',Ca)
np.savetxt('C_all.txt',C)
np.savetxt('HA_xyz',B_HA)
np.savetxt('CA_xyz',B_CA)
np.savetxt('C_xyz',B_C)
  
