# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:18:24 2013

@author: ronaldholt
"""

import numpy as np

import pylab as plt

#make a 3 row by 1 column plot of chemical shifts comparing simulated NCBD with experimental values

EXP_C=np.loadtxt('JJS_CS_allEXP_MDavg.txt',skiprows=1)
EXP_CA = np.loadtxt('CA_JJS_CS_ExpandMD.txt',skiprows=1)
EXP_HA = np.loadtxt('HA_JJS_CS_EXPandMD.txt',skiprows=1)


fig = plt.figure(figsize=(10,6),dpi=300)


ax1=fig.add_subplot(313)
ax1.errorbar(EXP_C[:,0],EXP_C[:,1],yerr=EXP_C[:,2],label='MD C')
ax1.plot(EXP_C[:,0],EXP_C[:,4],'ro',alpha=.5,label='1KBH')
ax1.plot(EXP_C[:,0],EXP_C[:,6],'bo',alpha=.5,label='2KKJ')
ax1.plot(EXP_C[:,0],EXP_C[:,8],'go',alpha=.5,label='2L14')
ax1.text(135, 55, 'C'+r'$\alpha$', color='k',fontsize=18)
#plt.title('HA')
#ax1.ylim(3.0,6.0)
EXP_C = np.ma.array(EXP_C, mask=np.isnan(EXP_C))
#np.ma.corrcoef(maskedarr,rowvar=False,allow_masked=True)
C_CC1=np.corrcoef(EXP_C[:,1],EXP_C[:,4])
C_CC2=np.corrcoef(EXP_C[:,1],EXP_C[:,6])
C_CC3=np.corrcoef(EXP_C[:,1],EXP_C[:,8])


ax2=fig.add_subplot(312)
ax2.errorbar(EXP_CA[:,0],EXP_CA[:,1],yerr=EXP_CA[:,2],label='MD CA')
ax2.plot(EXP_CA[:,0],EXP_CA[:,4],'ro',alpha=.5,label='1KBH')
ax2.plot(EXP_CA[:,0],EXP_CA[:,6],'bo',alpha=.5,label='2KKJ')
ax2.plot(EXP_CA[:,0],EXP_CA[:,8],'go',alpha=.5,label='2L14')
ax2.text(135, 55,'CA'+ r'$\alpha$', color='k',fontsize=18)
#plt.title('CA')
#ax2.ylim(40,70)


ax3=fig.add_subplot(311)
ax3.errorbar(EXP_HA[:,0],EXP_HA[:,1],yerr=EXP_HA[:,2],label='MD HA')
ax3.plot(EXP_HA[:,0],EXP_HA[:,4],'ro',alpha=.5,label='1KBH')
ax3.plot(EXP_HA[:,0],EXP_HA[:,6],'bo',alpha=.5,label='2KKJ')

ax3.text(135, 4.25, 'HA'+r'$\alpha$', color='k',fontsize=18)
#ax3.ylim(170,180)
fig.tight_layout()

fig.legend((A),('MD' ), 'upper left')
fig.legend((B),('Experimental ACTR/NCBD'), 'upper right')
fig.savefig('Chem_shift.png',dpi=300)
#plt.show()