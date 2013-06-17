# -*- coding: utf-8 -*-
"""
Created on 

@author:JamesPino
"""

import numpy as np
import pylab as plt

CA1=np.loadtxt('/Volumes/JPINO8/1JJS1/Chem_shift/CA_xyz')
CA2=np.loadtxt('/Volumes/JPINO8/1JJS2/Chem_shift/CA_xyz')
CA3=np.loadtxt('/Volumes/JPINO8/1JJS3/Chem_shift/CA_xyz')
CA=[]
CA.append(CA1[:,1])
CA.append(CA2[:,1])
CA.append(CA3[:,1])
CA=np.transpose(CA)

CAE=[]
CAE.append(CA1[:,2])
CAE.append(CA2[:,2])
CAE.append(CA3[:,2])
CAE=np.transpose(CAE)
avg_CAE=np.average(CAE,axis=1)
avg_CA=np.average(CA,axis=1)
Final_CA=np.column_stack((CA1[:,0],avg_CA,avg_CAE))
np.savetxt('1JJS_CA_all_xyz',Final_CA)


C1=np.loadtxt('/Volumes/JPINO8/1JJS1/Chem_shift/C_xyz')
C2=np.loadtxt('/Volumes/JPINO8/1JJS2/Chem_shift/C_xyz')
C3=np.loadtxt('/Volumes/JPINO8/1JJS3/Chem_shift/C_xyz')
C=[]
C.append(C1[:,1])
C.append(C2[:,1])
C.append(C3[:,1])
C=np.transpose(C)
CE=[]
CE.append(C1[:,2])
CE.append(C2[:,2])
CE.append(C3[:,2])
CE=np.transpose(CE)
avg_CE=np.average(CE,axis=1)
avg_C=np.average(C,axis=1)
Final_C=np.column_stack((C1[:,0],avg_C,avg_CE))
np.savetxt('1JJS_C_all_xyz',Final_C)


HA1=np.loadtxt('/Volumes/JPINO8/1JJS1/Chem_shift/HA_xyz')
HA2=np.loadtxt('/Volumes/JPINO8/1JJS1/Chem_shift/HA_xyz')
HA3=np.loadtxt('/Volumes/JPINO8/1JJS1/Chem_shift/HA_xyz')
HA=[]
HA.append(HA1[:,1])
HA.append(HA2[:,1])
HA.append(HA3[:,1])
HA=np.transpose(HA)
HAE=[]
HAE.append(HA1[:,2])
HAE.append(HA2[:,2])
HAE.append(HA3[:,2])
HAE=np.transpose(HAE)
avg_HAE=np.average(HAE,axis=1)
avg_HA=np.average(HA,axis=1)
Final_HA=np.column_stack((HA1[:,0],avg_HA,avg_HAE))
np.savetxt('1JJS_HA_all_xyz',Final_HA)