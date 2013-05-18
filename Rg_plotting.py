# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(JamesPino)s
"""
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(14,7),dpi=200)
dEG=np.array([[0,10,20,40],[15.36,14.62,14.68,13.90]])
NaCl_283=[13.74,13.72,13.84]
NaCl_293=[14.5,14.89,14.85]
NaCl_310=[14.24,14.58]
Prot_Conc=np.array([[.54,3.88,6.84],[13.3,np.average(NaCl_293),15.28]])
dPEG=np.array([16.8])
TEMP=(283,293,310)
TEMP=np.asarray(TEMP)
CONC=np.array([50,150,500])
Rg_50=[13.74,14.5,14.24]
Rg_150=[13.72,14.89,14.58]
Rg_500=[13.90,14.85]
conc_3=np.array(15.26)
conc_0o54=np.array(13.3)
conc_6o64=np.array(15.28)
Guin=(15.36,14.62,14.68,13.9,13.72,14.89,14.58,13.84,14.85,13.74,14.5,14.24,15.28,16.86)
Pair_Dist=(16.3,14.5,14.4,13.6,13.2,14.6,14,13.5,14.4,12.5,14.3,14,15.2,14.95,13.3)
#plt.hist([x,y])
#plt.show()
plt.subplot(221)

plt.plot(TEMP,Rg_50,'o',label='50mM')
plt.plot(TEMP,Rg_150,'x',label='150mM')
plt.plot(TEMP[0:2],Rg_500,'>',label='500mM')
plt.legend(loc='0')
plt.ylabel('Rg(Ang)',fontsize=24)
plt.xlabel('Temp(K)',fontsize=24)
plt.xlim(270,320)
plt.grid(True)
plt.subplot(222)
plt.plot(CONC,NaCl_283,'o',label='283K')
plt.plot(CONC,NaCl_293,'x',label='293K')
plt.plot(CONC[0:2],NaCl_310,'>',label='310K')
plt.ylabel('Rg(Ang',fontsize=24)
plt.xlabel('Concentration of NaCl (mM)',fontsize=24)
plt.xlim(0,550)
plt.grid(True)
plt.legend(loc='0')
plt.subplot(223)
plt.plot(dEG[0],dEG[1],'o')
plt.legend(loc='0')
plt.grid(True)
plt.xlim(-1,50)
plt.ylabel('Rg(Ang)',fontsize=24)
plt.xlabel('Concentration of dEG(%)',fontsize=22)
plt.subplot(224)
plt.xlabel('Concentration of NCBD(mg/ml)',fontsize=22)
#plt.bar(conc_3,label='2.88 mgml')
#plt.bar(conc_0o54,label='0.54 mgml')
#plt.bar(conc_6o64,label='6.84 mgml')

plt.plot(Prot_Conc[0],Prot_Conc[1],'o')

plt.grid(True)
plt.ylabel('Rg(Ang)',fontsize=24)
plt.savefig('/Users/ronaldholt/Desktop/Rg_4plots.png',dpi=500)
plt.show()
