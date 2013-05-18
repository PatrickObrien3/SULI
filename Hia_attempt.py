# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(JamesPino)s
"""

import scipy 

import numpy, scipy
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist
from scipy.cluster.vq import kmeans,vq
for line in dataFile:
     #append each column except the first column which is the gene ID
     dataMatrix.append([float(x) for x in line.strip().split('\t')[1:]])
     

#get your data into a 2d array where rows are genes, and columns 
#are conditions
data = numpy.array(dataMatrix)

#calculate a distance matrix
distMatrix = dist.pdist(data)

#convert the distance matrix to square form. The distance matrix 
#calculated above contains no redundancies, you want a square form 
#matrix where the data is mirrored across the diagonal.
distSquareMatrix = dist.squareform(distMatrix)

#calculate the linkage matrix 
linkageMatrix = hier.linkage(distSquareMatrix)

dendro = hier.dendrogram(linkageMatrix)

#get the order of rows according to the dendrogram 
leaves = dendro['leaves'] 

#reorder the original data according to the order of the 
#dendrogram. Note that this slice notation is numpy specific.
#It just means for every row specified in the 'leaves' array,
#get all the columns. So it effectively remakes the data matrix
#using the order from the 'leaves' array.
transformedData = data[leaves,:]
     
LINK=scipy.cluster.hierarchy.linkage(icaoffs,method='single',metric='euclidean')


CLU=scipy.cluster.hierarchy.fcluster(CLU,.01,depth=3)

DEND=scipy.cluster.hierarchy.dendrogram(CLU)
centroids,_ = kmeans(icacoffs,5)
idx,_ = vq(icacoffs,centroids)
plt.plot(icacoffs[idx==0,0],icacoffs[idx==0,1],'ob',icacoffs[idx==1,0],icacoffs[idx==1,1],'or',icacoffs[idx==2,0],icacoffs[idx==2,1],'og',icacoffs[idx==3,0],icacoffs[idx==3,1],'og',icacoffs[idx==4,0],icacoffs[idx==4,1],'og')
plt.plot(centroids[:,0],centroids[:,1],centroids[:,2],'sg',markersize=8)
plt.show()