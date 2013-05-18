# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(JamesPino)s
"""

import numpy as np
import os
import matplotlib.pylab as plt

MD_Run=np.loadtxt('/Users/ronaldholt/Desktop/ORNL/NCBD/AMBER/1JJS1/All_IvsQ.csv',delimiter=',')
os.chdir('/Users/ronaldholt/Desktop/Csub_Files')
lis_files= os.listdir(".")
J=MD_Run[10:,0]
ran_lis=np.random.random_integers(1,100000,size=2)
for filename in lis_files:
    if filename.startswith("50mM"):
        plt.subplot(411)  
        for i in ran_lis:
            md=MD_Run[10:,str(i)]
            md_norm=md/np.max(md)
            plt.semilogy(J,md_norm,'+',label=str(MD_Run[0,str(i)]))
            ran_lis=np.random.random_integers(1,100000,size=2)
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.semilogy(I,q,label=filename)
#        plt.legend(loc=0)
        plt.title("I(Q) vs. Q")
        plt.xlim([.1,.3])
        plt.ylim([0,1])
    if filename.startswith("150mM"):
        plt.subplot(412)
        for i in ran_lis:
            md=MD_Run[10:,str(i)]
            md_norm=md/np.max(md)
            plt.semilogy(J,md_norm,'+',label=str(MD_Run[0,str(i)]))
            ran_lis=np.random.random_integers(1,100000,size=2)
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.semilogy(I,q,label=filename)
#        plt.legend(loc=0)
        plt.xlim([.1,.3])
        plt.ylim([0,1])
    if filename.startswith("500mM"):
        plt.subplot(413)        
        for i in ran_lis:
            md=MD_Run[10:,str(i)]
            md_norm=md/np.max(md)
            plt.semilogy(J,md_norm,'+',label=str(MD_Run[0,str(i)]))
            ran_lis=np.random.random_integers(1,100000,size=2)
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.xlim([.1,.3])
        plt.ylim([0,1])
        plt.semilogy(I,q,label=filename)
    if filename.startswith("dEG" or "0per"):
        plt.subplot(414)
        for i in ran_lis:
            md=MD_Run[10:,str(i)]
            md_norm=md/np.max(md)
            plt.semilogy(J,md_norm,'+',label=str(MD_Run[0,str(i)]))
            ran_lis=np.random.random_integers(1,100000,size=2)
        x,y=np.loadtxt(filename, skiprows=1, usecols=(0,1), delimiter=",", unpack=True)
        I=x[6:84]
        q=y[6:84]/np.max(y[6:84])
        plt.semilogy(I,q,label=filename)
#        plt.legend(loc=0)
        plt.xlabel("Q")
        plt.xlim([.1,.3])
        plt.ylim([0,1])
        plt.ylabel("I(Q)")
plt.show()