# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(JamesPino)s
"""
import os
import numpy as np
import matplotlib.pyplot as plt

MD_Run=np.loadtxt('/Users/ronaldholt/Desktop/ORNL/NCBD/AMBER/1JJS1/All_IvsQ.csv',delimiter=',') 
EXP_data='/Users/ronaldholt/Google_Drive/ORNL_Research/IvsQ_SANS/'
a=[]
b=1
li=[0]
for filename in os.listdir(EXP_data):
    if filename.endswith(".txt"):
        x,y=np.loadtxt(EXP_data+'/'+filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        z=y/np.max(y)
        if b==1:
            li.append(filename)
            a=np.column_stack((x,z))
            b=2
        else:
            a=np.column_stack((a,z))
            li.append(filename)
I=MD_Run[10:,0]

avg=np.average(a[:,1:],axis=1)
avg_norm=avg/np.max(avg)



ran_lis=np.random.random_integers(1,100000,size=20)
for i in ran_lis:
    plt.subplot(221)
    md=MD_Run[10:,str(i)]
    md_norm=md/np.max(md)
    plt.semilogy(I,md_norm,'+',label=MD_Run[0,str(i)])
    ran_lis=np.random.random_integers(1,100000,size=20)
for i in range(1,len(a[0,:])):
    plt.semilogy(a[10:91,0],avg_norm[10:91,str(i)])
for i in ran_lis:
    plt.subplot(222)
    md=MD_Run[10:,str(i)]
    md_norm=md/np.max(md)
    plt.semilogy(I,md_norm,'+',label=MD_Run[0,str(i)])
    ran_lis=np.random.random_integers(1,100000,size=20)
for i in ran_lis:
    plt.subplot(223)
    md=MD_Run[10:,str(i)]
    md_norm=md/np.max(md)
    plt.semilogy(I,md_norm,'+',label=MD_Run[0,str(i)])
ran_lis=np.random.random_integers(1,100000,size=20)
for i in ran_lis:
    plt.subplot(224)
    md=MD_Run[10:,str(i)]
    md_norm=md/np.max(md)
    plt.semilogy(I,md_norm,'+',label=MD_Run[0,str(i)])