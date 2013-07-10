# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:54:24 2013

@author: jms
"""

import numpy as np
import os 

#MD_CA = np.loadtxt( '/home/jms/2KKJ/Chemical_shift/CA_xyz_all_2KKJ.txt' )
#MD_C = np.loadtxt( '/home/jms/2KKJ/Chemical_shift/C_xyz_all_2KKJ.txt' )
#MD_HA = np.loadtxt( '/home/jms/2KKJ/Chemical_shift/HA_xyz_all_2KKJ.txt' )

MD_CA = np.loadtxt( '/home/jms/1ZOQ/1ZOQ/1/ANAL/Chemical_Shift/CA_xyz' )
MD_C = np.loadtxt( '/home/jms/1ZOQ/1ZOQ/1/ANAL/Chemical_Shift/C_xyz' )
MD_HA = np.loadtxt( '/home/jms/1ZOQ/1ZOQ/1/ANAL/Chemical_Shift/HA_xyz' )

#MD_CA = np.loadtxt( '/home/jms/1JJS/1JJS_SAMMY/Chem_shift/CA_xyz_all_1JJS.txt' )
#MD_C = np.loadtxt( '/home/jms/1JJS/1JJS_SAMMY/Chem_shift/C_xyz_all_1JJS.txt' )
#MD_HA = np.loadtxt( '/home/jms/1JJS/1JJS_SAMMY/Chem_shift/HA_xyz_all_1JJS.txt' )

JJS_CA=np.loadtxt('/home/jms/NMR_Chemical_shift/15398_unbound_NCBD/CA.txt',skiprows=1)
JJS_C=np.loadtxt('/home/jms/NMR_Chemical_shift/15398_unbound_NCBD/C.txt',skiprows=1)
JJS_HA=np.loadtxt('/home/jms/NMR_Chemical_shift/15398_unbound_NCBD/HA.txt',skiprows=1)

KBH_CA=np.loadtxt('/home/jms/NMR_Chemical_shift/5228_ACTR_NCBD/NCBD/CA.txt',skiprows=1)
KBH_HA=np.loadtxt('/home/jms/NMR_Chemical_shift/5228_ACTR_NCBD/NCBD/HA.txt',skiprows=1)
KBH_C=np.loadtxt('/home/jms/NMR_Chemical_shift/5228_ACTR_NCBD/NCBD/C.txt',skiprows=1)

KKJ_CA=np.loadtxt('/home/jms/NMR_Chemical_shift/16363_unbound_2KKJ/CA.txt',skiprows=1)
KKJ_HA=np.loadtxt('/home/jms/NMR_Chemical_shift/16363_unbound_2KKJ/HA.txt',skiprows=1)
KKJ_C=np.loadtxt('/home/jms/NMR_Chemical_shift/16363_unbound_2KKJ/C.txt',skiprows=1)

L14_CA=np.loadtxt('/home/jms/NMR_Chemical_shift/17073_NCBD_TAD_2L14/NCBD/CA.txt',skiprows=1)
L14_HA=np.loadtxt('/home/jms/NMR_Chemical_shift/17073_NCBD_TAD_2L14/NCBD/HA.txt',skiprows=1)
L14_C=np.loadtxt('/home/jms/NMR_Chemical_shift/17073_NCBD_TAD_2L14/NCBD/C.txt',skiprows=1)

#HA=np.loadtxt('Complex_HA_xyz')
#CA=np.loadtxt('Complex_CA_xyz')
#C=np.loadtxt('Complex_C_xyz')



def align(exp,md,name):
    diff=np.zeros((1,5))
    Diff=[]
    for i in range(0,len(exp)):
        for j in range(0,len(md)):
            if md[j,0]== exp[i,0]:
                Diff=np.column_stack((exp[i,0],exp[i,1],md[j,0],md[j,1],md[j,2]))   
                diff=np.append(diff,Diff,axis=0)
                Diff=[]

    np.savetxt(name+'_aligned.txt',diff)

align(JJS_CA,MD_CA,'JJS_CA')
align(KBH_CA,MD_CA,'KBH_CA')
align(KKJ_CA,MD_CA,'KKJ_CA') 
align(L14_CA,MD_CA,'L14_CA') 
     
align(JJS_C,MD_C,'JJS_C')
align(KBH_C,MD_C,'KBH_C')
align(KKJ_C,MD_C,'KKJ_C') 
align(L14_C,MD_C,'L14_C') 

align(JJS_HA,MD_HA,'JJS_HA')
align(KBH_HA,MD_HA,'KBH_HA')
align(KKJ_HA,MD_HA,'KKJ_HA') 
align(L14_HA,MD_HA,'L14_HA')      
