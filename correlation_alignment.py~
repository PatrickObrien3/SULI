# -*- coding: utf-8 -*-
"""
Created on 

@author:JamesPino
"""

import numpy as np
import os 

EXP_HA = np.loadtxt('/home/jms/1KBH/BOTH/Chem_Shift/COMPLEX_HA.txt')
EXP_CA = np.loadtxt('/home/jms/1KBH/BOTH/Chem_Shift/COMPLEX_CA.txt')
EXP_C = np.loadtxt('/home/jms/1KBH/BOTH/Chem_Shift/COMPLEX_C.txt')

HA=np.loadtxt('HA_xyz')
CA=np.loadtxt('CA_xyz')
C=np.loadtxt('C_xyz')
ha='ha'
ca='ca'
c='c'

def align(exp,md,name):
	
	diff=np.zeros((1,5))
	Diff=[]
	s=0
	for i in range(0,len(exp)):
	    for j in range(0,len(md)):
	        if CA[j,0]== exp[i,0]:
	            Diff=np.column_stack((exp[i,0],exp[i,1],md[j,0],md[j,1],md[j,2]))   
	            diff=np.append(diff,Diff,axis=0)
	            Diff=[]
	np.savetxt(name+'_aligned.txt',diff)

align(EXP_HA,HA,ha)
align(EXP_CA,CA,ca)
align(EXP_C,C,c)        
