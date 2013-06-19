import numpy as np
import matplotlib.pyplot as plt
import os
import sys

FILE=sys.argv[1]
EXT='/home/jms/NMR_Chem_Shift/'

fig = plt.figure(figsize=(10,6),dpi=300)

x1,HA1=np.loadtxt(EXT+'HA_only_16363',unpack=True)
y1,C1=np.loadtxt(EXT+'C_only_16363',unpack=True)
z1,CA1=np.loadtxt(EXT+'CA_only_16363',unpack=True)

x2,HA2=np.loadtxt(EXT+'HA_only_17073',unpack=True)
y2,C2=np.loadtxt(EXT+'C_only_17073',unpack=True)
z2,CA2=np.loadtxt(EXT+'CA_only_17073',unpack=True)

#x3,HA3=np.loadtxt(EXT+'HA_only',unpack=True)
#y3,C3=np.loadtxt(EXT+'C_only',unpack=True)
#z3,CA3=np.loadtxt(EXT+'CA_only',unpack=True)


y4,C4=np.loadtxt(EXT+'C_only_15398',unpack=True)
z4,CA4=np.loadtxt(EXT+'CA_only_15398',unpack=True)


RES,HA_avg,HA_err=np.loadtxt('HA_xyz',unpack=True)
RES,CA_avg,CA_err=np.loadtxt('CA_xyz',unpack=True)
RES,C_avg,C_err=np.loadtxt('C_xyz',unpack=True)

ax1=fig.add_subplot(311)
ax1.errorbar(RES,HA_avg,yerr=HA_err,label='HA')
ax1.plot(x1,HA1,'ko',alpha=.5,label='exp HA 2KKJ')
ax1.plot(x2,HA2,'ro',alpha=.5,label='exp HA 2L14')
#ax1.plot(x3,HA3,'go',alpha=.5,label='exp HA 2C52')
#ax1.ylim(3.0,6.0)

ax2=fig.add_subplot(312)
A=ax2.errorbar(RES,CA_avg,yerr=CA_err,label='CA')
B=ax2.plot(z1,CA1,'ko',alpha=.5,label='exp CA 2KKJ')
C=ax2.plot(z2,CA2,'ro',alpha=.5,label='exp CA 2L14')
#D=ax2.plot(z3,CA3,'go',alpha=.5,label='exp CA 2C52')
E=ax2.plot(z4,CA4,'mo',alpha=.5,label='exp CA 1KBH')
#ax2.ylim(40,70)


ax3=fig.add_subplot(313)
ax3.errorbar(RES,C_avg,yerr=C_err,label='C')
ax3.plot(y1,C1,'ko',alpha=.5,label='exp C 2KKJ')
ax3.plot(y2,C2,'ro',alpha=.5,label='exp C 2L14')
#ax3.plot(y3,C3,'go',alpha=.5,label='exp C 2C52')
ax3.plot(y4,C4,'mo',alpha=.5,label='exp C 1KBH')
#ax3.ylim(170,180)

#fig.legend((B,C),('2KKJ', '2L14'), 'upper left')
#fig.legend(A,'MD', 'upper center')
#fig.legend((D,E),('2C52','1KBH'), 'upper right')
fig.savefig(FILE+'_Chem_shift.png',dpi=300,bbox_inches='tight')
fig.show()
