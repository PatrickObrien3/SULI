# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(JamesPino)s
"""
import numpy as np
import matplotlib.pyplot as plt


EXP_data='/Users/ronaldholt/Desktop/ORNL/NCBD/1KBH-ACTR/icnorm_ncbd_actr_bsub.txt'
THEOR_data='/Users/ronaldholt/Google_Drive/ORNL_Research/1KBH/All_IvsQ.csv'



Complex=np.loadtxt(EXP_data,skiprows=2)
q=Complex[:,0]
Iq=Complex[:,1]#/np.max(Complex[:,1])
yerr=Complex[:,2]#/np.max(Complex[:,1])


MD_Run=np.loadtxt(THEOR_data,delimiter=',')  

I=MD_Run[10:,0]
#ran_lis=np.random.random_integers(1,20000,size=20000)
for i in range(1,20000,100):
    md=MD_Run[10:,str(i)]
    md_norm=md#/np.max(md)
    plt.semilogy(I,md_norm,'.',alpha=.5)
avg=np.average(MD_Run,axis=1)
avg_norm=avg#/np.max(avg)    
plt.semilogy(I,avg_norm[10:,],'o',label='MD avg')
plt.semilogy(q,Iq,'o',label='SANS')
plt.errorbar(q, Iq, yerr=yerr)    
plt.legend(loc=0)
plt.show()
