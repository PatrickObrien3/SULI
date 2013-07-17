# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:43:36 2013

@author: jms
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

<<<<<<< HEAD
JJS='/Users/ronaldholt/Google_Drive/ORNL/Trajectorys/1JJS/'
KKJ='/Users/ronaldholt/Google_Drive/ORNL/Trajectorys/2KKJ/'
ZOQ='/Users/ronaldholt/Google_Drive/ORNL/Trajectorys/1ZOQ/'


x,r11 =np.loadtxt(str(JJS)+'13_17.out',unpack=True)
x,r12 =np.loadtxt(str(JJS)+'13_33.out',unpack=True)
x,r13 =np.loadtxt(str(JJS)+'13_43.out',unpack=True)
x,r14 =np.loadtxt(str(JJS)+'17_33.out',unpack=True)
x,r15 =np.loadtxt(str(JJS)+'17_43.out',unpack=True)
x,r16 =np.loadtxt(str(JJS)+'33_43.out',unpack=True)
y,r21 =np.loadtxt(str(KKJ)+'13_17.out',unpack=True)
y,r22 =np.loadtxt(str(KKJ)+'13_33.out',unpack=True)
y,r23 =np.loadtxt(str(KKJ)+'13_43.out',unpack=True)
y,r24 =np.loadtxt(str(KKJ)+'17_33.out',unpack=True)
y,r25 =np.loadtxt(str(KKJ)+'17_43.out',unpack=True)
y,r26 =np.loadtxt(str(KKJ)+'33_43.out',unpack=True)
z,r31 =np.loadtxt(str(ZOQ)+'13_17.out',unpack=True)
z,r32 =np.loadtxt(str(ZOQ)+'13_33.out',unpack=True)
z,r33 =np.loadtxt(str(ZOQ)+'13_43.out',unpack=True)
z,r34 =np.loadtxt(str(ZOQ)+'17_33.out',unpack=True)
z,r35 =np.loadtxt(str(ZOQ)+'17_43.out',unpack=True)
z,r36 =np.loadtxt(str(ZOQ)+'33_43.out',unpack=True)
=======


distances = (13, 17, 33, 43)
x,r11 =np.loadtxt('/home/jms/1JJS/All/13_17.out',unpack=True)
x,r12 =np.loadtxt('/home/jms/1JJS/All/13_33.out',unpack=True)
x,r13 =np.loadtxt('/home/jms/1JJS/All/13_43.out',unpack=True)
x,r14 =np.loadtxt('/home/jms/1JJS/All/17_33.out',unpack=True)
x,r15 =np.loadtxt('/home/jms/1JJS/All/17_43.out',unpack=True)
x,r16 =np.loadtxt('/home/jms/1JJS/All/33_43.out',unpack=True)
y,r21 =np.loadtxt('/home/jms/NCBD-AMBER/2KKJ/13_17.out',unpack=True)
y,r22 =np.loadtxt('/home/jms/NCBD-AMBER/2KKJ/13_33.out',unpack=True)
y,r23 =np.loadtxt('/home/jms/NCBD-AMBER/2KKJ/13_43.out',unpack=True)
y,r24 =np.loadtxt('/home/jms/NCBD-AMBER/2KKJ/17_33.out',unpack=True)
y,r25 =np.loadtxt('/home/jms/NCBD-AMBER/2KKJ/17_43.out',unpack=True)
y,r26 =np.loadtxt('/home/jms/NCBD-AMBER/2KKJ/33_43.out',unpack=True)
z,r31 =np.loadtxt('/home/jms/1ZOQ/1ZOQ/1/ANAL/13_17.out',unpack=True)
z,r32 =np.loadtxt('/home/jms/1ZOQ/1ZOQ/1/ANAL/13_33.out',unpack=True)
z,r33 =np.loadtxt('/home/jms/1ZOQ/1ZOQ/1/ANAL/13_43.out',unpack=True)
z,r34 =np.loadtxt('/home/jms/1ZOQ/1ZOQ/1/ANAL/17_33.out',unpack=True)
z,r35 =np.loadtxt('/home/jms/1ZOQ/1ZOQ/1/ANAL/17_43.out',unpack=True)
z,r36 =np.loadtxt('/home/jms/1ZOQ/1ZOQ/1/ANAL/33_43.out',unpack=True)
>>>>>>> 086d1d83b02725d861f5eb966fcc8dc37d7612c1

fig=plt.figure(figsize=(12,9))

plt.subplot(3,2,1)

weights = np.ones_like(r11)/len(r11)
<<<<<<< HEAD
plt.hist(r11, 75,weights=weights,alpha=.5,label='1JJS',color='blue')
weights = np.ones_like(r21)/len(r21)
plt.hist(r21, 75,weights=weights,alpha=.5,label='2KKJ',color='gray')
weights = np.ones_like(r31)/len(r31)
plt.hist(r31, 75,weights=weights,alpha=.5,label='1ZOQ',color='orange')
=======
plt.hist(r11, 75,weights=weights,alpha=.5,label='1JJS')
weights = np.ones_like(r21)/len(r21)
plt.hist(r21, 75,weights=weights,alpha=.5,label='2KKJ')
weights = np.ones_like(r31)/len(r31)
plt.hist(r31, 75,weights=weights,alpha=.5,label='1ZOQ')
>>>>>>> 086d1d83b02725d861f5eb966fcc8dc37d7612c1
plt.legend(loc=0)

plt.subplot(3,2,2)

weights = np.ones_like(r12)/len(r12)
<<<<<<< HEAD
plt.hist(r12, 75,weights=weights,alpha=.5,label='1JJS',color='blue')
weights = np.ones_like(r22)/len(r22)
plt.hist(r22, 75,weights=weights,alpha=.5,label='2KKJ',color='gray')
weights = np.ones_like(r32)/len(r32)
plt.hist(r32, 75,weights=weights,alpha=.5,label='1ZOQ',color='orange')
plt.legend(loc=0)

plt.subplot(3,2,3)

weights = np.ones_like(r13)/len(r13)
plt.hist(r13, 75,weights=weights,alpha=.5,label='1JJS',color='blue')
weights = np.ones_like(r23)/len(r23)
plt.hist(r23, 75,weights=weights,alpha=.5,label='2KKJ',color='gray')
weights = np.ones_like(r33)/len(r33)
plt.hist(r33, 75,weights=weights,alpha=.5,label='1ZOQ',color='orange')
plt.legend(loc=0)

plt.subplot(3,2,4)

weights = np.ones_like(r14)/len(r14)
plt.hist(r14, 75,weights=weights,alpha=.5,label='1JJS',color='blue')
weights = np.ones_like(r24)/len(r24)
plt.hist(r24, 75,weights=weights,alpha=.5,label='2KKJ',color='gray')
weights = np.ones_like(r34)/len(r34)
plt.hist(r34, 75,weights=weights,alpha=.5,label='1ZOQ',color='orange')
plt.legend(loc=0)

=======
plt.hist(r12, 75,weights=weights,alpha=.5,label='1JJS')
weights = np.ones_like(r22)/len(r22)
plt.hist(r22, 75,weights=weights,alpha=.5,label='2KKJ')
weights = np.ones_like(r32)/len(r32)
plt.hist(r32, 75,weights=weights,alpha=.5,label='1ZOQ')

plt.legend(loc=0)
plt.subplot(3,2,3)

weights = np.ones_like(r13)/len(r13)
plt.hist(r13, 75,weights=weights,alpha=.5,label='1JJS')
weights = np.ones_like(r23)/len(r23)
plt.hist(r23, 75,weights=weights,alpha=.5,label='2KKJ')
weights = np.ones_like(r33)/len(r33)
plt.hist(r33, 75,weights=weights,alpha=.5,label='1ZOQ')

plt.legend(loc=0)
plt.subplot(3,2,4)

weights = np.ones_like(r14)/len(r14)
plt.hist(r14, 75,weights=weights,alpha=.5,label='1JJS')
weights = np.ones_like(r24)/len(r24)
plt.hist(r24, 75,weights=weights,alpha=.5,label='2KKJ')
weights = np.ones_like(r34)/len(r34)
plt.hist(r34, 75,weights=weights,alpha=.5,label='1ZOQ')

plt.legend(loc=0)
>>>>>>> 086d1d83b02725d861f5eb966fcc8dc37d7612c1
plt.subplot(3,2,5)

weights = np.ones_like(r15)/len(r15)
plt.hist(r11, 75,weights=weights,alpha=.5,label='1JJS',color='blue')
weights = np.ones_like(r25)/len(r25)
plt.hist(r25, 75,weights=weights,alpha=.5,label='2KKJ',color='gray')
weights = np.ones_like(r35)/len(r35)
plt.hist(r35, 75,weights=weights,alpha=.5,label='1ZOQ',color='orange')
plt.legend(loc=0)

plt.subplot(3,2,6)

weights = np.ones_like(r16)/len(r16)
<<<<<<< HEAD
plt.hist(r16, 75,weights=weights,alpha=.5,label='1JJS',color='blue')
weights = np.ones_like(r26)/len(r26)
plt.hist(r26, 75,weights=weights,alpha=.5,label='2KKJ',color='gray')
weights = np.ones_like(r36)/len(r36)
plt.hist(r36, 75,weights=weights,alpha=.5,label='1ZOQ',color='orange')
=======
plt.hist(r16, 75,weights=weights,alpha=.5,label='1JJS')
weights = np.ones_like(r26)/len(r26)
plt.hist(r26, 75,weights=weights,alpha=.5,label='2KKJ')
weights = np.ones_like(r36)/len(r36)
plt.hist(r36, 75,weights=weights,alpha=.5,label='1ZOQ')
>>>>>>> 086d1d83b02725d861f5eb966fcc8dc37d7612c1
plt.legend(loc=0)

fig.tight_layout()
plt.savefig('Hydro_compare_distance.png',dpi=150,bbox_inches='tight')
#plt.show()

def plot_3d_scatter(x1,y1,z1,x2,y2,z2,x3,y3,z3,label1,label2,label3,number):
    fig = plt.figure(figsize=(12,12),dpi=150);
    ax1=fig.add_subplot(221,projection='3d')
    ax1.scatter(x1,y1,z1,alpha=.5,c='blue',label='1JJS',rasterized=True)
    ax1.scatter(x2,y2,z2,alpha=.5,c='gray',label='2KKJ',rasterized=True)
    ax1.scatter(x3,y3,z3,alpha=.5,c='orange',label='1ZOQ',rasterized=True)    
    ax1.set_xlabel(str(label1))
    ax1.set_ylabel(str(label2))
    ax1.set_zlabel(str(label3))
    ax1.legend(loc=0)
    ax2=fig.add_subplot(222)
    ax2.scatter(x1,y1,alpha=.5,label='1JJS',c='blue',rasterized=True)
    ax2.scatter(x2,y2,alpha=.5,label='2KKJ',c='gray',rasterized=True)
    ax2.scatter(x3,y3,alpha=.5,label='1ZOQ',c='orange',rasterized=True)
    ax2.set_xlabel(str(label1))
    ax2.set_ylabel(str(label2))
    ax2.legend(loc=0)
    ax3=fig.add_subplot(223)
    ax3.scatter(y1,z1,alpha=.5,label='1JJS',c='blue',rasterized=True)
    ax3.scatter(y2,z2,alpha=.5,label='2KKJ',c='gray',rasterized=True)
    ax3.scatter(y3,z3,alpha=.5,label='1ZOQ',c='orange',rasterized=True)    
    ax3.set_xlabel(str(label2))
    ax3.set_ylabel(str(label3))
    ax3.legend(loc=0)
    ax4=fig.add_subplot(224)
    ax4.scatter(x1,z1,alpha=.5,label='1JJS',c='blue',rasterized=True)
    ax4.scatter(x2,z2,alpha=.5,label='2KKJ',c='gray',rasterized=True)
    ax4.scatter(x3,z3,alpha=.5,label='1ZOQ',c='orange',rasterized=True)
    ax4.set_xlabel(str(label1))
    ax4.set_ylabel(str(label3))
    ax4.legend(loc=0)
    plt.savefig("Correlation-compare-distance-"+str(number)+".png",dpi=150,bbox_inches='tight')
    plt.clf()
plot_3d_scatter(r11,r12,r13,r21,r22,r23,r31,r32,r33,'L13-L17','L13-L33','L13-F43',1)
plot_3d_scatter(r11,r13,r14,r21,r23,r24,r31,r33,r34,'L13-L17','L13-F43','L17-L33',2)
plot_3d_scatter(r11,r14,r15,r21,r24,r25,r31,r34,r35,'L13-L17','L17-L33','L17-F43',3)
plot_3d_scatter(r11,r15,r16,r21,r25,r26,r31,r35,r36,'L13-L17','L17-F43','L17-F43',4)
<<<<<<< HEAD
plot_3d_scatter(r12,r13,r14,r22,r23,r24,r32,r33,r34,'L13-L33','L13-F43','L14-L33',5)
plot_3d_scatter(r12,r14,r15,r22,r24,r25,r32,r34,r35,'L13-L33','L17-L33','L17-F43',6)
plot_3d_scatter(r12,r15,r16,r22,r25,r26,r32,r35,r36,'L13-L33','L17-F43','L33-F43',7)
plot_3d_scatter(r13,r14,r15,r23,r24,r25,r33,r34,r35,'L13-F43','L14-L33','L17-F43',8)
plot_3d_scatter(r13,r15,r16,r23,r25,r26,r33,r35,r36,'L13-F43','L17-F43','L33-F43',9)
plot_3d_scatter(r14,r15,r16,r24,r25,r26,r34,r35,r36,'L14-L33','L17-F43','L33-F43',10)
=======
plot_3d_scatter(r12,r13,r14,r22,r23,r24,r32,r33,r34,'L13-L33','L13-F43','L17-L33',5)
plot_3d_scatter(r12,r14,r15,r22,r24,r25,r32,r34,r35,'L13-L33','L17-L33','L17-F43',6)
plot_3d_scatter(r12,r15,r16,r22,r25,r26,r32,r35,r36,'L13-L33','L17-F43','L33-F43',7)
plot_3d_scatter(r13,r14,r15,r23,r24,r25,r33,r34,r35,'L13-F43','L17-L33','L17-F43',8)
plot_3d_scatter(r13,r15,r16,r23,r25,r26,r33,r35,r36,'L13-F43','L17-F43','L33-F43',9)
plot_3d_scatter(r14,r15,r16,r24,r25,r26,r34,r35,r36,'L17-L33','L17-F43','L33-F43',10)
>>>>>>> 086d1d83b02725d861f5eb966fcc8dc37d7612c1
