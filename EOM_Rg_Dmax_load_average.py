import matplotlib.pyplot as plt
import numpy as np
import os
NAME='ACTR'
filename='/home/jms/ACTR/EOM/Models_'

#NAME='COMPLEX'
#filename='/home/jms/1KBH/ANAL/EOM_Complex/Models_'




EIQ_err=EIQ_err/np.max(EIQ[:])
EIQ=EIQ/np.max(EIQ[:])
DMAX=[]
Dfreq=[]
DSfreq=[]
RG=[]
Rfreq=[]
RSfreq=[]
b=1
for k in xrange(1,6):
#	x,y,z=np.loadtxt(filename+str(k)+'/Data/GA001/Rg_distr'+NAME+'001.fit',skiprows=51,usecols=(0,1,2), unpack=True)
	dmax,Freq,Sel=np.loadtxt(filename+str(k)+'/Data/GA001/Size_distr'+NAME+'001.data',skiprows=51,usecols=(0,1,2), unpack=True)	
	rg,freq,sel=np.loadtxt(filename+str(k)+'/Data/GA001/Rg_distr'+NAME+'001.dat',skiprows=4,usecols=(0,1,2), unpack=True)


	if b==1:
		DMAX=dmax
		Dfreq=np.append(Freq,y,axis=1)
		DSfreq=np.append(Sel,z,axis=1)   
		b=2
		RG=rg
		Rfreq=np.append(freq,y,axis=1)
		RSfreq=np.append(sel,z,axis=1)   
		b=2
	else:
		q=np.column_stack((q,y))
		q2=np.column_stack((q2,z))
q_avg=np.average(q,axis=1)
q2_avg=np.average(q2,axis=1)
q_std=np.std(q,axis=1)
q2_std=np.std(q2,axis=1)
data1=np.column_stack((I,q_avg,q_std))
data2=np.column_stack((I,q2_avg,q2_std))
np.savetxt('IvsQ1_avg.txt',data1)
np.savetxt('IvsQ2_avg.txt',data2)




fig=plt.figure(figsize=(8,6),dpi=100)
ax=fig.add_subplot(111)

q_std=q_std/np.max(q_avg[:])
q_avg=q_avg/np.max(q_avg[:])
q2_std=q2_std/np.max(q2_avg[:])
q2_avg=q2_avg/np.max(q2_avg[:])
#plt.errorbar(I,q_avg,yerr=q_std,label='q1')
plt.errorbar(I,q2_avg,yerr=q2_std,label='MD selected')
plt.errorbar(EI,EIQ,yerr=EIQ_err,label='Experimental')
ax.set_yscale('log')
plt.legend(loc=0)
plt.savefig('IvsQ_Compare.png')
plt.show()
