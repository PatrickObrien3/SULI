import numpy as np
import os
import sys


filename='/home/jms/1KBH/ANAL/EOM_Complex/Models_'
for k in range(1,6):
	os.chdir(filename+str(k)+'/Data/')
	pdb,freq=np.loadtxt(filename+str(k)+'/Data/GA001/best_curve001.txt',skiprows=2,usecols=(0,1),dtype=int, unpack=True)
	os.mkdir(filename+str(k)+'/Data/Selected001')
	for i in pdb:
		os.system('cp   '+filename+str(k)+'/Data/'+str(i)+'x.pdb   '+filename+str(k)+'/Data/Selected001/')
		os.chdir(filename+str(k)+'/Data/Selected001/')
	for i in pdb:
		os.system('/home/jms/Install/shiftx/./shiftx 1 '+str(i)+'x.pdb  ' +str(i)+'.out')
		print str(i)
	print 'finished chemical shift'
	for i in pdb:
		print i
		os.system(" sed '75,280d' " +str(i)+".out >> "+str(i)+".txt") 
	print 'finished sed'
	s=0
	HA=[]
	Ca=[]
	Res=[]
	C=[]
	for i in pdb:
		print i
		if s==0:
			data=np.loadtxt(str(i)+ '.txt',comments='*',skiprows=2,usecols=(0,2,5,7))
			Res=np.concatenate((Res,data[:,0]),axis=0)
			HA=data[:,1]
			Ca=data[:,2]
			C=data[:,3]
			s=s+1
		else:
			data=np.loadtxt(str(i)+ '.txt' ,comments='*',skiprows=2,usecols=(0,2,5,7))
			HA=np.column_stack((HA,data[:,1]))
			Ca=np.column_stack((Ca,data[:,2]))
			C=np.column_stack((C,data[:,3]))

	HA_avg=np.average(HA,axis=1)
	Ca_avg=np.average(Ca,axis=1)
	C_avg=np.average(C,axis=1)
	
	HA_std=np.std(HA,axis=1)
	CA_std=np.std(Ca,axis=1)
	C_std=np.std(C,axis=1)
	
	B_HA=np.column_stack((Res,HA_avg,HA_std))
	B_CA=np.column_stack((Res,Ca_avg,CA_std))
	B_C=np.column_stack((Res,C_avg,C_std))
	os.mkdir('TXT')
	os.system('mv *txt TXT')
	os.mkdir('OUT')
	os.system('mv *out OUT')

	np.savetxt('HA_all.txt',HA)
	np.savetxt('Ca_all.txt',Ca)
	np.savetxt('C_all.txt',C)
	
	np.savetxt('HA_xyz',B_HA)
	np.savetxt('CA_xyz',B_CA)
	np.savetxt('C_xyz',B_C)

