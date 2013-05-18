import numpy as np
from matlibplot import pyplot as pp
N=2
M=100
n=N/2
difference=np.zero((1,n*M))
for i in xrange(M):
    A=np.random.normal(0,1,(N,N))
    AT=A.transpose()
    B=A+AT
    V,D=np.linalg.eig(B)
    V.sort()
    for j in xrange(n):
        difference.append(V[j+1]-V[j])
m=np.mean(difference)
