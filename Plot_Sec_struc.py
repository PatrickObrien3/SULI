import numpy as np
import matplotlib.pyplot as plt


A,B=np.loadtxt('SS_1KBH2.out',skiprows=1,usecols=(0,2),unpack=True)
A1,B1=np.loadtxt('SS_1KBH1.out',skiprows=1,usecols=(0,2),unpack=True)
D,E,F=np.loadtxt('SS_ACTR.out',skiprows=1,usecols=(0,2,4),unpack=True)


x=np.sum(B/100)
y=np.sum(B1/100)
percent_alpha=(x+y)/2
percent_alpha1=np.sum(E/100)
fig = plt.figure(figsize=(10,6),dpi=300)
ax1=fig.add_subplot(111)
plt.bar(A[:77],B[:77],color='blue',alpha=0.6,label='Complex')
plt.bar(D,E,color='red',alpha=0.6,label='ACTR')
plt.xlim=(0.0,77.0)
ax1.text(0, 60, '% Complex'+r'$\alpha$='+str(percent_alpha), color='k',fontsize=18)
ax1.text(0, 70, '% ACTR'+r'$\alpha$='+str(percent_alpha1), color='k',fontsize=18)
plt.grid(True)
plt.legend(loc=0)
plt.savefig('Secondary_struc.png')
#plt.show()
