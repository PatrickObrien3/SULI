# -*- coding: utf-8 -*-
"""
Created on 

@author:JamesPino
"""

import os

directories=['/Users/ronaldholt/Desktop/ORNL/NCBD/Trajectory/ACTR/models']#, '~!......']

def renumber_for_EOM(working_directory,count_start):
    os.chdir(str(working_directory))
    for k in range(1,11):
        j=count_start
        os.system('mkdir Models_'+str(k) )
        for i in range(k,50001,5):
           # os.system('cp '+str(i)+'y.pdb  /Models_'+str(k)+'/'+str(j)+'x.pdb')
            os.system('cp  '+str(i)+'x00.int  Models_'+str(k)+'/'+str(j)+'x00.int')
            os.system('cp  '+str(i)+'x00.log  Models_'+str(k)+'/'+str(j)+'x00.log')
            j+=1
    return j
        
start=1
for x in directories:
    start+=renumber_for_EOM(x,start)
    
