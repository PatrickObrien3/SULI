
import sys
import numpy as np
import matplotlib.pyplot as plt

Complex='/home/jms/CHRIS_DATA/SS/avg_ss1KBH_all_MD.txt'
Actr='/home/jms/CHRIS_DATA/SS/SS_ACTR.out'
res1,alph1 = np.loadtxt(Complex,usecols=(0,1),unpack=True)
res2,alph2 = np.loadtxt(Actr,skiprows=1,usecols=(0,2),unpack=True)
sel_res1, sel_alph1 = np.loadtxt(sys.argv[1],skiprows=1,usecols=(0,2),unpack=True)
sel_res2, sel_alph2 = np.loadtxt(sys.argv[2],skiprows=1,usecols=(0,2),unpack=True)


x=np.sum(alph/100)
y=np.sum(alph2/100)

percent_alpha1=np.sum(sel_alph/100)
percent_alpha2=np.sum(sel_alph/100)
fig = plt.figure(figsize=(10,6),dpi=300)
ax1=fig.add_subplot(111)

plt.bar(res1[:77],alph1[:77],color='blue',alpha=0.6,label='Complex')
plt.bar(res2,alph2,color='red',alpha=0.6,label='ACTR')
plt.bar(sel_res1,sel_alph1,color='red',alpha=0.6,label='Select Complex')
plt.bar(sel_res2,sel_alph2,color='red',alpha=0.6,label='Select ACTR')


plt.xlim=(0.0,77.0)
ax1.text(0, 60, '% Complex'+r'$\alpha$='+str(x), color='k',fontsize=18)
ax1.text(0, 70, '% ACTR'+r'$\alpha$='+str(y), color='k',fontsize=18)
ax1.text(0, 70, '% Select Complex'+r'$\alpha$='+str(percent_alpha1), color='k',fontsize=18)
ax1.text(0, 70, '% Select Complex'+r'$\alpha$='+str(percent_alpha2), color='k',fontsize=18)


plt.grid(True)
plt.legend(loc=0)
plt.savefig('Secondary_struc.png')
#plt.show()


