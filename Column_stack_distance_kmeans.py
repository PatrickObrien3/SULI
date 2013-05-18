import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist
import scipy
os.chdir('/Users/ronaldholt/Desktop/DISTANCE')

for i in range(1,2):
    data=[]
    for j in range(i+1,60):
        print str(i)+'_'+str(j)+'.out'
        x,y=np.loadtxt(str(i)+'_'+str(j)+'.out',usecols=(0,1),unpack=True)
        if j==2:
            data=np.arange(1,len(x)+1)
        data=np.column_stack((data,y))
    np.savetxt(str(i)+'all.txt',data)
res=np.arange(1,60)
for i in range(1,50000,100):
    plt.plot(res[1:],data[i,1:],'o')



TRY=data[:1000,1:]
distMat=dist.pdist(TRY)
distSquareMatix=dist.squareform(distMat)
linkageMatri=hier.linkage(distSquareMatix)
dendro=hier.dendrogram(linkageMatri)
leaves=dendro['leaves']
transformedData = data[leaves,:]
#plt.show()

KM=scipy.cluster.vq.kmeans2(TRY,100,iter=1000,minit='random')
NEW=np.array(KM[0])
labels=np.array(KM[1])
for i in range(1,len(NEW)):
    plt.plot(res[1:],NEW[i,0:],'-')
plt.show()



