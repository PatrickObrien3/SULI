# -*- coding: utf-8 -*-
"""
Created on 

@author:JamesPino
"""

import numpy as np
import pylab as plt

SS1=np.loadtxt('/Users/ronaldholt/Desktop/ORNL/NCBD/Trajectory/1JJS1/SS.sum',skiprows=1)
SS2=np.loadtxt('/Users/ronaldholt/Desktop/ORNL/NCBD/Trajectory/1JJS2/SS.sum',skiprows=1)
SS3=np.loadtxt('/Users/ronaldholt/Desktop/ORNL/NCBD/Trajectory/1JJS3/SS.sum',skiprows=1)
alpha=[]
alpha.append(SS1[:,2])
alpha.append(SS2[:,2])
alpha.append(SS3[:,2])
alpha=np.transpose(alpha)
beta=[]
beta.append(SS1[:,5])
beta.append(SS2[:,5])
beta.append(SS3[:,5])
beta=np.transpose(beta)
avg_alpha=np.average(alpha,axis=1)
avg_beta=np.average(beta,axis=1)

per_alpha=np.sum(avg_alpha)/(59*100)*100
per_beta=np.sum(avg_beta)/(59*100)*100

plt.bar(SS1[:,0],avg_alpha,color='blue',label='alpha',alpha=.5)
plt.bar(SS1[:,0],avg_beta,color='red',label='beta',alpha=.5)
plt.legend(loc=0)
plt.show()