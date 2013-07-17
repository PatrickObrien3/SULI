# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:55:11 2013

@author: jms
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

colormap=cm.gist_rainbow
distances = (13, 17, 33, 43)
x,r1 =np.loadtxt('13_17.out',unpack=True)
x,r2 =np.loadtxt('13_33.out',unpack=True)
x,r3 =np.loadtxt('13_43.out',unpack=True)
x,r4 =np.loadtxt('17_33.out',unpack=True)
x,r5 =np.loadtxt('17_43.out',unpack=True)
x,r6 =np.loadtxt('33_43.out',unpack=True)
FRame,ENERGY=np.loadtxt('Norm_Energy.txt',usecols=(0,1),delimiter=" ",unpack=True)
n=0
fig=plt.figure(figsize=(12,9))
for i in distances:
    for j in distances:
        if i<j:
            x,y=np.loadtxt(str(i)+'_'+str(j)+'.out',unpack=True)
            n=n+1
            plt.subplot(3,2,n)
            plt.hist(y,100,label=str(i)+'_'+str(j))#, orientation='horizontal')
            plt.legend(loc=0)
        else:
            continue
plt.legend(loc=0)
fig.tight_layout()
plt.savefig('Hydro_distance.png',dpi=150,bbox_inches='tight')
#plt.show()

def plot_3d_scatter(x,y,z,label1,label2,label3,number):
    fig = plt.figure(figsize=(12,12),dpi=150);
    ax1=fig.add_subplot(221,projection='3d')
    P=ax1.scatter(x,y,z,c=ENERGY,cmap=colormap)
    cbar = fig.colorbar(P,ticks=[-3,0,3])
    cbar.ax.set_yticklabels(['<-3','0','>3'])
    ax2=fig.add_subplot(222)
    P=ax2.scatter(x,y,alpha=.5,label=str(label1)+' vs '+str(label2),c=ENERGY,cmap=colormap)
    cbar = fig.colorbar(P,ticks=[-3,0,3])
    cbar.ax.set_yticklabels(['<-3','0','>3'])
    plt.xlim(x.min(),x.max())
    plt.ylim(y.min(),y.max())
    plt.legend(loc=0)
    ax3=fig.add_subplot(223)
    P=plt.scatter(x,z,alpha=.5,label=str(label1)+' vs '+str(label3),c=ENERGY,cmap=colormap)
    cbar = fig.colorbar(P,ticks=[-3,0,3])
    cbar.ax.set_yticklabels(['<-3','0','>3'])
    plt.xlim(x.min(),x.max())
    plt.ylim(z.min(),z.max())    
    plt.legend(loc=0)
    ax4=fig.add_subplot(224)
    P=plt.scatter(x,z,alpha=.5,label=str(label1)+' vs '+str(label3),c=ENERGY,cmap=colormap)
    cbar = fig.colorbar(P,ticks=[-3,0,3])
    cbar.ax.set_yticklabels(['<-3','0','>3'])
    plt.xlim(x.min(),x.max())
    plt.ylim(z.min(),z.max())    
    plt.legend(loc=0)
    plt.savefig("Correlation_distance_"+str(number)+".png",dpi=150,bbox_inches='tight')
    plt.clf()
plot_3d_scatter(r1,r2,r3,'L13-L17','L13-L33','L13-F43',1)
plot_3d_scatter(r1,r3,r4,'L13-L17','L13-F43','L17-L33',2)
plot_3d_scatter(r1,r4,r5,'L13-L17','L17-L33','L17-F43',3)
plot_3d_scatter(r1,r5,r6,'L13-L17','L17-F43','L17-F43',4)
plot_3d_scatter(r2,r3,r4,'L13-L33','L13-F43','L14-L33',5)
plot_3d_scatter(r2,r4,r5,'L13-L33','L17-L33','L17-F43',6)
plot_3d_scatter(r2,r5,r6,'L13-L33','L17-F43','L33-F43',7)
plot_3d_scatter(r3,r4,r5,'L13-F43','L14-L33','L17-F43',8)
plot_3d_scatter(r3,r5,r6,'L13-F43','L17-F43','L33-F43',9)
plot_3d_scatter(r4,r5,r6,'L14-L33','L17-F43','L33-F43',10)

