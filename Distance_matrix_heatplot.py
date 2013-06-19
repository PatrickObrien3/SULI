import numpy as np
import matplotlib.pyplot as plt
import pylab
import sys

FILE=sys.argv[1]


#F=open('Distance_data.txt','w')

STD_Matrix=np.arange(1,60)
Dist_Matrix=np.arange(1,60)
for i in range(1,60):
    avg=[]
    std=[]
    for j in range(i+1,60):
        print str(i)+'_'+str(j)+'.out'
        x,y=np.loadtxt(str(i)+'_'+str(j)+'.out',usecols=(0,1),unpack=True)
        tmp_a=np.average(y)
        tmp_b=np.std(y)        
        avg=np.append(avg,tmp_a)
        std=np.append(std,tmp_b)
    
    res=np.arange(i+1,60)
    for j in range(i):
        std=np.insert(std,0,0)
        avg=np.insert(avg,0,0)
    STD_Matrix=np.column_stack((STD_Matrix,std))
    Dist_Matrix=np.column_stack((Dist_Matrix,avg))    
np.savetxt(FILE+'_Std_distanceMat.txt',STD_Matrix)    
np.savetxt(FILE+'_Avg_distanceMat.txt',Dist_Matrix)
  

pylab.imshow(Dist_Matrix[:,1:])
pylab.colorbar()
pylab.savefig(FILE+'Dist_matrix.png',dpi=200)
pylab.imshow(STD_Matrix[:,1:])
pylab.colorbar()
pylab.savefig(FILE+'StD_matrix.png',dpi=200)
