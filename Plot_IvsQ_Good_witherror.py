# -*- coding: utf-8 -*-
import numpy as np
import os
import matplotlib.pylab as plt
import pylab


os.chdir('/Users/ronaldholt/Desktop/ORNL/Csub_Files')
lis_files= os.listdir(".")
I=1
fig=plt.figure(figsize=(12, 12))
a1=fig.add_subplot(412)
a1.set_yscale('log')
#a1.set_xscale('log')
x,y,z=np.loadtxt('150mM_NaCl_10C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='150 mM NaCl at 283K')


x,y,z=np.loadtxt('150mM_NaCl_20C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='150 mM NaCl at 293K')

x,y,z=np.loadtxt('150mM_NaCl_37C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='150 mM NaCl at 310K')

plt.legend(loc=3)
#plt.xlabel("Q",fontsize=32)
plt.xlim([.05,.3])
plt.ylim([0.0001,.02])
plt.ylabel("I(Q)",fontsize=32)
plt.grid(True)
pylab.yticks(fontsize=25)
pylab.xticks(fontsize=25)        
a2=fig.add_subplot(411)
a2.set_yscale('log')
#a2.set_xscale('log')
x,y,z=np.loadtxt('50mM_NaCl_10C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='50 mM NaCl at 283K')

x,y,z=np.loadtxt('50mM_NaCl_20C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)

plt.errorbar(x,y,yerr=z,label='50 mM NaCl at 293K')

x,y,z=np.loadtxt('50mM_NaCl_37C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='50 mM NaCl at 310K')
plt.legend(loc=3)
#plt.xlabel("Q",fontsize=32)
plt.xlim([.05,.3])
plt.ylim([0.0001,.02])
#plt.ylabel("I(Q)",fontsize=32)
plt.grid(True)
pylab.yticks(fontsize=25)
pylab.xticks(fontsize=25)

a3=fig.add_subplot(413)
#a3.set_xscale('log')
a3.set_yscale('log')
x,y,z=np.loadtxt('500mM_NaCl_10C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='500 mM NaCl at 283K')

x,y,z=np.loadtxt('500mM_NaCl_20C.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)

plt.errorbar(x,y,yerr=z,label='500 mM NaCl at 293K')
plt.legend(loc=3)
plt.grid(True)
#plt.xlabel("Q",fontsize=32)
plt.xlim([.05,.3])
plt.ylim([0.0001,.02])
#plt.ylabel("I(Q)",fontsize=32)
pylab.yticks(fontsize=25)
pylab.xticks(fontsize=25)

a4=fig.add_subplot(414)
#a4.set_xscale('log')
a4.set_yscale('log')
x,y,z=np.loadtxt('0per.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='0 percent Osmolyte')

x,y,z=np.loadtxt('dEG_10per.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)


plt.errorbar(x,y,yerr=z,label='10 percent Osmolyte')
plt.grid(True)
plt.ylabel("I(Q)",fontsize=32)


x,y,z=np.loadtxt('dEG_20per.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='20 percent Osmolyte')


x,y,z=np.loadtxt('dEG_40per.txt', skiprows=1, usecols=(0,1,2), delimiter=",", unpack=True)
plt.errorbar(x,y,yerr=z,label='40 percent Osmolyte')
plt.legend(loc=3)
plt.xlabel("Q",fontsize=32)
plt.xlim([.05,.3])
plt.ylim([0.0001,.02])
#plt.ylabel("I(Q)",fontsize=32)
plt.grid(True)
pylab.yticks(fontsize=25)
pylab.xticks(fontsize=25)

plt.savefig('IvsQ_Temp_salt_osm.png',dpi=300)
plt.show()