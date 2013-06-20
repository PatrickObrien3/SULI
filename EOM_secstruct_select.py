# -*- coding: utf-8 -*-
"""
Created on 

@author:JamesPino
"""
import numpy as np


f=open('trajin_select_models','w')
pdb,freq=np.loadtxt('//Users/ronaldholt/Google_Drive/Data_for_Chris/ACTR/GA001/best_curve001.txt',skiprows=2,unpack=True)


for i in pdb:
    print>>f,'trajin '+str(int(i))+'x.pdb'+' pdb' 
    print 'trajin '+str(int(i))+'x.pdb'+' pdb'
print>>f,'secstruct out SS_select.out'
f.close()