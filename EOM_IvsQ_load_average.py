import matplotlib.pyplot as plt
import numpy as np
import os
#NAME='ACTR'
#filename='/home/jms/ACTR/EOM/Models_'

NAME='COMPLEX'
filename='/home/jms/1KBH/ANAL/EOM_Complex/Models_'


#experimental data
#EI,EIQ,EIQ_err=np.loadtxt(' ~/eom_actr_ncbd/actr_files/icnorm_actr_bsub.dat',skiprows=1,unpack=True)
EI,EIQ,EIQ_err=np.loadtxt('/home/jms/eom_actr_ncbd/complex/icnorm_ncbd_actr_bsub.dat',skiprows=1,unpack=True)


EIQ_err=EIQ_err/np.max(EIQ[:])
EIQ=EIQ/np.max(EIQ[:])
q=[]
q2=[]
b=1
for k in xrange(1,11):
	x,y,z=np.loadtxt(filename+str(k)+'/Data/GA001/profiles'+NAME+'001.fit',skiprows=51,usecols=(0,1,2), unpack=True)
#	x,y,z=np.loadtxt(filename+str(k)+'/Data/GA001/profiles'+NAME+'001.fit',skiprows=101,usecols=(0,1,2), unpack=True)	
	if b==1:
		I=x
		q=np.append(q,y,axis=1)
		q2=np.append(q2,z,axis=1)   
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

q_std=q_std/np.max(q_avg[:])
q_avg=q_avg/np.max(q_avg[:])
q2_std=q2_std/np.max(q2_avg[:])
q2_avg=q2_avg/np.max(q2_avg[:])
plt.errorbar(I,q_avg,yerr=q_std,label='q1')
plt.errorbar(I,q2_avg,yerr=q2_std,label='q2')
plt.errorbar(EI,EIQ,yerr=EIQ_err,label='exp')
plt.legend(loc=0)
plt.savefig('IvsQ_Compare.png')
plt.show()
