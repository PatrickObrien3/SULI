# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:28:16 2013

@author: ronaldholt
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


x,r1 =np.loadtxt('13_17.out',unpack=True)
x,r2 =np.loadtxt('13_33.out',unpack=True)
x,r3 =np.loadtxt('13_43.out',unpack=True)
x,r4 =np.loadtxt('17_33.out',unpack=True)
x,r5 =np.loadtxt('17_43.out',unpack=True)
x,r6 =np.loadtxt('33_43.out',unpack=True)

data=np.column_stack((x,r1,r2,r3,r4,r5,r6))
a1,a2,a3,a4,a5,a6=0,5,10,15,20,100

cluster1=[]
cluster2=[]
cluster3=[]
cluster4=[]
cluster5=[]
cluster6=[]
cluster7=[]


def extract(data,index):
    cluster1=[]
    cluster2=[]
    cluster3=[]
    cluster4=[]
    mean = np.mean(data[:,index])
    std = np.std(data[:,index])    
    for i in range(0,len(data)):
        if 0 < data[i,index] < mean-std:
            cluster1.append(data[i,:])
        if mean-std<  data[i,index] < mean:
            cluster2.append(data[i,:])
        if mean <     data[i,index] <mean+std:
            cluster3.append(data[i,:])
        if mean+std < data[i,index] < 100:
            cluster4.append(data[i,:])
    cluster1=np.array(cluster1)
    cluster2=np.array(cluster2)
    cluster3=np.array(cluster3)
    cluster4=np.array(cluster4)
    return cluster1,cluster2,cluster3,cluster4
                       
a1,a2,a3,a4=extract(data,1)
print np.shape(a1)
print np.shape(a2)
print np.shape(a3)
print np.shape(a4)


a11,a12,a13,a14=extract(a1,2)
print 'a11 ',np.shape(a11)
print 'a12 ',np.shape(a12)
print 'a13 ',np.shape(a13)
print 'a14 ',np.shape(a14)
a21,a22,a23,a24=extract(a2,2)
print 'a21 ',np.shape(a21)
print 'a22 ',np.shape(a22)
print 'a23 ',np.shape(a23)
print 'a24 ',np.shape(a24)
a31,a32,a33,a34=extract(a3,2)
print 'a31 ',np.shape(a31)
print 'a32 ',np.shape(a32)
print 'a33 ',np.shape(a33)
print 'a34 ',np.shape(a34)
a41,a42,a43,a44=extract(a4,2)
print 'a41 ',np.shape(a41)
print 'a42 ',np.shape(a42)
print 'a43 ',np.shape(a43)
print 'a44 ',np.shape(a44)

def prep_ptraj(array,filename):
    f=open(str(filename),'w')
    for i in range(1,len(array)):
        print 'trajin '+str(array[i,0])+' '+str(array[i,0])
    f.close()
prep_ptraj(a11,'trajin_cluster1')