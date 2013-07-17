import numpy as np

CA1=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS1/Chem_shift/CA_xyz')
HA1=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS1/Chem_shift/HA_xyz')
C1=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS1/Chem_shift/C_xyz')

CA2=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS2/Chem_shift/CA_xyz')
HA2=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS2/Chem_shift/HA_xyz')
C2=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS2/Chem_shift/C_xyz')

CA3=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS3/Chem_shift/CA_xyz')
HA3=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS3/Chem_shift/HA_xyz')
C3=np.loadtxt('/home/jms/1JJS/1JJS_SAMMY/1JJS3/Chem_shift/C_xyz')

ca=np.column_stack((CA1[:,1],CA2[:,1],CA3[:,1]))
ha=np.column_stack((HA1[:,1],HA2[:,1],HA3[:,1]))
c=np.column_stack((C1[:,1],C2[:,1],C3[:,1]))

#ca_std=np.column_stack((CA1[:,2],CA2[:,2],CA3[:,2]))
#ha_std=np.column_stack((HA1[:,2],HA2[:,2],HA3[:,2]))
#c_std=np.column_stack((C1[:,2],C2[:,2],C3[:,2]))

ca_avg=np.average(ca,axis=1)
ha_avg=np.average(ha,axis=1)
c_avg=np.average(c,axis=1)

ca_std=np.sqrt((CA1[:,2]**2+CA2[:,2]**2+CA3[:,2]**2)/3)
c_std=np.sqrt((C1[:,2]**2+C2[:,2]**2+C3[:,2]**2)/3)
ha_std=np.sqrt((HA1[:,2]**2+HA2[:,2]**2+HA3[:,2]**2)/3)

CA=np.column_stack((CA1[:,0],ca_avg,ca_std))
HA=np.column_stack((HA1[:,0],ha_avg,ha_std))
C=np.column_stack((C1[:,0],c_avg,c_std))

np.savetxt('CA_xyz_all_1JJS.txt',CA)
np.savetxt('HA_xyz_all_1JJS.txt',HA)
np.savetxt('C_xyz_all_1JJS.txt',C)