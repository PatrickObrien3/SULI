
import sys
import numpy as np
import matplotlib.pyplot as plt

Complex='/home/jms/CHRIS_DATA/SS/avg_ss1KBH_all_MD.txt'
Actr='/home/jms/CHRIS_DATA/SS/SS_ACTR.out'
res1,alph1 = np.loadtxt(Complex,usecols=(0,1),unpack=True)
res2,alph2 = np.loadtxt(Actr,skiprows=1,usecols=(0,2),unpack=True)
sel_res1, sel_alph1 = np.loadtxt(sys.argv[1],skiprows=1,usecols=(0,2),unpack=True)
sel_res2, sel_alph2 = np.loadtxt(sys.argv[2],skiprows=1,usecols=(0,2),unpack=True)


x=np.sum(alph1/100)#complex
y=np.sum(alph2/100)#actr

percent_alpha1=np.sum(sel_alph1/100)#complex
percent_alpha2=np.sum(sel_alph2/100)#actr


fig = plt.figure(figsize=(10,6),dpi=300)
ax1=fig.add_subplot(121)


plt.bar(res2,alph2,color='red',alpha=0.6,label='ACTR')
plt.bar(sel_res2,sel_alph2,color='blue',alpha=0.6,label='Select ACTR')

ax2=fig.add_subplot(122)
plt.bar(res1,alph1,color='red',alpha=0.6,label='Complex')
plt.bar(sel_res1,sel_alph1,color='blue',alpha=0.6,label='Select Complex')



#plt.xlim=(0.0,77.0)
ax1.text(30, 90, '% '+r'$\alpha$='+str(x), color='k',fontsize=18)
ax1.text(30, 80, '% '+r'$\alpha$='+str(y), color='k',fontsize=18)
ax2.text(30, 70, '% '+r'$\alpha$='+str(percent_alpha1), color='k',fontsize=18)
ax2.text(30, 60, '% '+r'$\alpha$='+str(percent_alpha2), color='k',fontsize=18)


plt.grid(True)
plt.legend(loc=0)
plt.savefig('Secondary_struc.png')
#plt.show()


