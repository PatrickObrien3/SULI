# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:38:30 2013

@author: jms
"""

import numpy as np
import pylab as plt
F=open('Correlation_values.txt','w')
#which one to plot
root1='/home/jms/1JJS/1JJS_SAMMY/Chem_shift/'
root2='/home/jms/2KKJ/Chemical_shift/'
root3='/home/jms/1ZOQ/1ZOQ/1/ANAL/Chemical_Sehift/'
#run='2KKJ'
run='1JJS'
rootnumber=root3
#MD_CA = np.loadtxt( str(rootnumber)+'CA_xyz_all_'+str(run)+'.txt' )
#MD_C = np.loadtxt( str(rootnumber)+'C_xyz_all_'+str(run)+'.txt' )
#MD_HA = np.loadtxt( str(rootnumber)+'HA_xyz_all_'+str(run)+'.txt' )

MD_CA = np.loadtxt( '/home/jms/1ZOQ/1ZOQ/1/ANAL/Chemical_Shift/CA_xyz' )
MD_C = np.loadtxt( '/home/jms/1ZOQ/1ZOQ/1/ANAL/Chemical_Shift/C_xyz' )
MD_HA = np.loadtxt( '/home/jms/1ZOQ/1ZOQ/1/ANAL/Chemical_Shift/HA_xyz' )

JJS_CA=np.loadtxt(str(rootnumber)+'JJS_CA_aligned.txt',skiprows=1)
JJS_C=np.loadtxt(str(rootnumber)+'JJS_C_aligned.txt',skiprows=1)
#JJS_HA=np.loadtxt(str(rootnumber)+'JJS_HA_aligned.txt',skiprows=1)

cc1_CA=np.corrcoef(JJS_CA[:,1],JJS_CA[:,3])
cc1_C=np.corrcoef(JJS_C[:,1],JJS_C[:,3])
print 'Ca correlation with JJS is ',cc1_CA
print 'C correlation with JJS is ',cc1_C
#cc1_HA=np.corrcoef(JJS_HA[:,1],JJS_HA[:,3])

KBH_CA=np.loadtxt(str(rootnumber)+'KBH_CA_aligned.txt',skiprows=1)
KBH_HA=np.loadtxt(str(rootnumber)+'KBH_HA_aligned.txt',skiprows=1)
KBH_C=np.loadtxt(str(rootnumber)+'KBH_C_aligned.txt',skiprows=1)

cc2_CA=np.corrcoef(KBH_CA[:,1],KBH_CA[:,3])
cc2_C=np.corrcoef(KBH_C[:,1],KBH_C[:,3])
cc2_HA=np.corrcoef(KBH_HA[:,1],KBH_HA[:,3])
print 'Ca correlation with JJS is ',cc2_CA
print 'C correlation with JJS is ',cc2_C
print 'Ha correlation with JJS is ',cc2_HA

KKJ_CA=np.loadtxt(str(rootnumber)+'KKJ_CA_aligned.txt',skiprows=1)
KKJ_HA=np.loadtxt(str(rootnumber)+'KKJ_HA_aligned.txt',skiprows=1)
KKJ_C=np.loadtxt(str(rootnumber)+'KKJ_C_aligned.txt',skiprows=1)

cc3_CA=np.corrcoef(KKJ_CA[:,1],KKJ_CA[:,3])
cc3_C=np.corrcoef(KKJ_C[:,1],KKJ_C[:,3])
cc3_HA=np.corrcoef(KKJ_HA[:,1],KKJ_HA[:,3])

print 'Ca correlation with KKJ is ',cc3_CA
print 'C correlation with KKJ is ',cc3_C
print 'Ha correlation with KKJ is ',cc3_HA

L14_CA=np.loadtxt(str(rootnumber)+'L14_CA_aligned.txt',skiprows=1)
L14_HA=np.loadtxt(str(rootnumber)+'L14_HA_aligned.txt',skiprows=1)
L14_C=np.loadtxt(str(rootnumber)+'L14_C_aligned.txt',skiprows=1)

cc4_CA=np.corrcoef(L14_CA[:,1],L14_CA[:,3])
cc4_C=np.corrcoef(L14_C[:,1],L14_C[:,3])
cc4_HA=np.corrcoef(L14_HA[:,1],L14_HA[:,3])

print 'Ca correlation with L14 is ',cc4_CA
print 'C correlation with L14 is ',cc4_C
print 'Ha correlation with L14 is ',cc4_HA

fig = plt.figure(figsize=(10,6),dpi=300)

ax1=fig.add_subplot(311)
plt.errorbar(MD_HA[:,0]+2059,MD_HA[:,1],yerr=MD_HA[:,2],label='MD')
#plt.plot(JJS_HA[:,0],JJS_HA[:,1],label='1JJS')
plt.plot(KBH_HA[:,0]+2059,KBH_HA[:,1],'ro',alpha=.5,label='1KBH')
plt.plot(KKJ_HA[:,0]+2059,KKJ_HA[:,1],'bo',alpha=.5,label='2KKJ')
plt.plot(L14_HA[:,0]+2059,L14_HA[:,1],'mo',alpha=.5,label='2L14')
ax1.text(2061, 5.5, 'H'+r'$\alpha$', color='k',fontsize=18)
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])

plt.ylim(3.0,6.5)
#plt.legend(loc=0)

ax2=fig.add_subplot(313)
plt.errorbar(MD_C[:,0]+2059,MD_C[:,1],yerr=MD_C[:,2],label='MD')
plt.plot(JJS_C[:,0]+2059,JJS_C[:,1],'go',alpha=.5,label='1JJS')
plt.plot(KBH_C[:,0]+2059,KBH_C[:,1],'ro',alpha=.5,label='1KBH')
plt.plot(KKJ_C[:,0]+2059,KKJ_C[:,1],'bo',alpha=.5,label='2KKJ')
plt.plot(L14_C[:,0]+2059,L14_C[:,1],'mo',alpha=.5,label='2L14')
ax2.text(2061, 180 ,r'C', color='k',fontsize=18)
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#plt.legend(loc=0)
plt.ylim(170,185)


ax3=fig.add_subplot(312)
plt.errorbar(MD_CA[:,0]+2059,MD_CA[:,1],yerr=MD_CA[:,2],label='MD')
plt.plot(JJS_CA[:,0]+2059,JJS_CA[:,1],'go',alpha=.5,label='1JJS')
plt.plot(KBH_CA[:,0]+2059,KBH_CA[:,1],'ro',alpha=.5,label='1KBH')
plt.plot(KKJ_CA[:,0]+2059,KKJ_CA[:,1],'bo',alpha=.5,label='2KKJ')
plt.plot(L14_CA[:,0]+2059,L14_CA[:,1],'mo',alpha=.5,label='2L14')
ax3.text(2061, 78,'C'+ r'$\alpha$', color='k',fontsize=18)
box = ax3.get_position()
ax3.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.legend(loc=0)
plt.ylim(40,85)

#fig.tight_layout()
fig.savefig('Chem_shift.png',dpi=300)
#plt.show()
print>>F, '            1JJS              2L14              1KBH             2KKJ'
print>>F, 'AlphaC   ',cc1_CA[0,1],' ',cc2_CA[0,1],'  ',cc3_CA[0,1],'  ',cc4_CA[0,1]
print>>F, 'C        ',cc1_C[0,1],' ',cc2_C[0,1],'  ',cc3_C[0,1],'   ',cc4_C[0,1]
print>>F, 'HA                        ',cc2_HA[0,1],'  ',cc3_HA[0,1],'  ',cc4_HA[0,1]
F.close()