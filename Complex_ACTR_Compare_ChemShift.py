import matplotlib.pyplot as plt
import numpy as np



CA=np.loadtxt('ca_aligned.txt',skiprows=1)
cc_CA=np.corrcoef(CA[:,1],CA[:,3])

HA=np.loadtxt('ha_aligned.txt',skiprows=1)
cc_HA=np.corrcoef(HA[:,1],HA[:,3])

C=np.loadtxt('c_aligned.txt',skiprows=1)
cc_C=np.corrcoef(C[:,1],C[:,3])

fig = plt.figure(figsize=(10,6),dpi=300)


RES,HA_avg,HA_err=np.loadtxt('HA_xyz',skiprows=26,unpack=True)
RES,CA_avg,CA_err=np.loadtxt('CA_xyz',skiprows=26,unpack=True)
RES,C_avg,C_err=np.loadtxt('C_xyz',skiprows=26,unpack=True)

ax1=fig.add_subplot(311)
ax1.errorbar(HA[:,2],HA[:,3],yerr=HA[:,4],label='HA')
ax1.plot(HA[:,0],HA[:,1],'ro',alpha=.5,label='exp HA ACTR/NCBD')
ax1.text(21, 4.25, 'H'+r'$\alpha$', color='k',fontsize=18)
ax1.text(80, 5.25, 'Cor.Coef.='+str(cc_HA[0,1]), color='k',fontsize=18)
#plt.title('HA')
plt.ylim(3.0,6.0)

ax2=fig.add_subplot(312)
A=ax2.errorbar(CA[:,0],CA[:,3],yerr=CA[:,4],label='MD CA')
B=ax2.plot(CA[:,0],CA[:,1],'ro',alpha=.5,label='exp CA ACTR/NCDB')
ax2.text(21, 55,'C'+ r'$\alpha$', color='k',fontsize=18)
ax2.text(80,42.5,'Corr.Coef ='+ str(cc_CA[0,1]), color='k',fontsize=18)
#plt.title('CA')
plt.ylim(40,70)


ax3=fig.add_subplot(313)
ax3.errorbar(C[:,2],C[:,3],yerr=C[:,4],label='C')
ax3.plot(C[:,0],C[:,1],'ro',alpha=.5,label='exp C ACTR/NCBD')
#plt.title('C')
ax3.text(21, 176, r'C', color='k',fontsize=18)
ax3.text(80, 170, r'Corr.Coeff='+str(cc_C[0,1]), color='k',fontsize=18)
plt.ylim(168,182)


fig.legend((A),('MD' ), 'upper left')
fig.legend((B),('Experimental ACTR/NCBD'), 'upper right')
fig.tight_layout()
fig.savefig('Chem_shift.png',dpi=300)

#plt.show()


