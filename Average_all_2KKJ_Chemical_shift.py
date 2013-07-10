# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:36:13 2013

@author: jms
"""

import numpy as np

CA1=np.loadtxt('/home/jms/2KKJ/1/Chemical_Shift/CA_xyz')
HA1=np.loadtxt('/home/jms/2KKJ/1/Chemical_Shift/HA_xyz')
C1=np.loadtxt('/home/jms/2KKJ/1/Chemical_Shift/C_xyz')

CA2=np.loadtxt('/home/jms/2KKJ/2/Chemical_Shift/CA_xyz')
HA2=np.loadtxt('/home/jms/2KKJ/2/Chemical_Shift/HA_xyz')
C2=np.loadtxt('/home/jms/2KKJ/2/Chemical_Shift/C_xyz')

CA3=np.loadtxt('/home/jms/2KKJ/3/Chemical_Shift/CA_xyz')
HA3=np.loadtxt('/home/jms/2KKJ/3/Chemical_Shift/HA_xyz')
C3=np.loadtxt('/home/jms/2KKJ/3/Chemical_Shift/C_xyz')

CA4=np.loadtxt('/home/jms/2KKJ/4/Chemical_Shift/CA_xyz')
HA4=np.loadtxt('/home/jms/2KKJ/4/Chemical_Shift/HA_xyz')
C4=np.loadtxt('/home/jms/2KKJ/4/Chemical_Shift/C_xyz')

CA5=np.loadtxt('/home/jms/2KKJ/5/Chemical_Shift/CA_xyz')
HA5=np.loadtxt('/home/jms/2KKJ/5/Chemical_Shift/HA_xyz')
C5=np.loadtxt('/home/jms/2KKJ/5/Chemical_Shift/C_xyz')

CA6=np.loadtxt('/home/jms/2KKJ/6/Chemical_Shift/CA_xyz')
HA6=np.loadtxt('/home/jms/2KKJ/6/Chemical_Shift/HA_xyz')
C6=np.loadtxt('/home/jms/2KKJ/6/Chemical_Shift/C_xyz')

CA7=np.loadtxt('/home/jms/2KKJ/7/Chemical_Shift/CA_xyz')
HA7=np.loadtxt('/home/jms/2KKJ/7/Chemical_Shift/HA_xyz')
C7=np.loadtxt('/home/jms/2KKJ/7/Chemical_Shift/C_xyz')

CA8=np.loadtxt('/home/jms/2KKJ/8/Chemical_Shift/CA_xyz')
HA8=np.loadtxt('/home/jms/2KKJ/8/Chemical_Shift/HA_xyz')
C8=np.loadtxt('/home/jms/2KKJ/8/Chemical_Shift/C_xyz')

CA9=np.loadtxt('/home/jms/2KKJ/9/Chemical_Shift/CA_xyz')
HA9=np.loadtxt('/home/jms/2KKJ/9/Chemical_Shift/HA_xyz')
C9=np.loadtxt('/home/jms/2KKJ/9/Chemical_Shift/C_xyz')

CA10=np.loadtxt('/home/jms/2KKJ/10/Chemical_Shift/CA_xyz')
HA10=np.loadtxt('/home/jms/2KKJ/10/Chemical_Shift/HA_xyz')
C10=np.loadtxt('/home/jms/2KKJ/10/Chemical_Shift/C_xyz')



ca=np.column_stack((CA1[:,1],CA2[:,1],CA3[:,1],CA4[:,1],CA5[:,1],CA6[:,1],CA7[:,1],CA8[:,1],CA9[:,1],CA10[:,1])  )
ha=np.column_stack((HA1[:,1],HA2[:,1],HA3[:,1],HA4[:,1],HA5[:,1],HA6[:,1],HA7[:,1],HA8[:,1],HA9[:,1],HA10[:,1]   ))
c=np.column_stack((C1[:,1],C2[:,1],C3[:,1],C3[:,1],C4[:,1],C5[:,1],C6[:,1],C7[:,1],C8[:,1],C9[:,1],C10[:,1]))


ca_avg=np.average(ca,axis=1)
ha_avg=np.average(ha,axis=1)
c_avg=np.average(c,axis=1)

ca_std=np.sqrt((  CA1[:,2]**2 +CA2[:,2]**2 +CA3[:,2]**2  +CA4[:,2]**2 +  CA5[:,2]**2+CA6[:,2]**2+CA7[:,2]**2+CA8[:,2]**2+CA9[:,2]**2+CA10[:,2]**2)/10)
c_std=np.sqrt((   C1[:,2]**2  +C2[:,2]**2  +C3[:,2]**2  +C4[:,2]**2   +  C5[:,2]**2+C6[:,2]**2+C7[:,2]**2+C8[:,2]**2+C9[:,2]**2+C10[:,2]**2)/10)
ha_std=np.sqrt((  HA1[:,2]**2 +HA2[:,2]**2 +HA3[:,2]**2 +HA4[:,2]**2  +  HA5[:,2]**2+HA6[:,2]**2+HA7[:,2]**2+HA8[:,2]**2+HA9[:,2]**2+HA10[:,2]**2)/10)

CA=np.column_stack((CA1[:,0],ca_avg,ca_std))
HA=np.column_stack((HA1[:,0],ha_avg,ha_std))
C=np.column_stack((C1[:,0],c_avg,c_std))

np.savetxt('CA_xyz_all_1JJS.txt',CA)
np.savetxt('HA_xyz_all_1JJS.txt',HA)
np.savetxt('C_xyz_all_1JJS.txt',C)