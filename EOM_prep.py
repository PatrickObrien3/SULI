# -*- coding: utf-8 -*-
"""
Created on 

@author:James Pino and Jordan Angel

This script is to prepare files from molecular dynamic simulations to be run 
using EOM from ATSAS. It takes the results of Cryson and evenly separates the
results while renumbering the files so the EOM can function properly.


"""

import os

#directories=['/home/jms/1KBH/BOTH/p_actr1/', '/home/jms/1KBH/BOTH/p_actr2/']
#directories=['/home/jms/Best_1KBH/3/ANAL/']
#directories=['/home/jms/1JJS/1/ANAL/','/home/jms/1JJS/2/ANAL/','/home/jms/1JJS/3/ANAL/']
directories=['/home/jms/1JJS/3/ANAL/','/home/jms/1JJS/2/ANAL/']
#savedir='/home/jms/1KBH/ANAL/EOM_Complex/Models_'
#savedir='/home/jms/Best_1KBH/EOM/'
savedir='/home/jms/1JJS/EOM/'
def renumber_for_EOM(working_directory,count_start):
    os.chdir(str(working_directory))
    for k in range(1,11):
        print 'Model', str(k) ,' of 10'
        j=count_start
        if j==1:
            os.system('mkdir '+str(savedir)+str(k))
        if j==5002:
            j=5001
        for i in range(k,50001,10):
            #print j
            os.system('ln -s    '+working_directory+str(i)+'x.pdb  '+savedir+str(k)+'/'+str(j)+'x.pdb')
            os.system('ln -s    '+working_directory+str(i)+'x00.int  '+savedir+str(k)+'/'+str(j)+'x00.int')
            os.system('ln -s    '+working_directory+str(i)+'x00.log  '+savedir+str(k)+'/'+str(j)+'x00.log')
            os.system('ln -s    '+working_directory+str(i)+'.txt  '+savedir+str(k)+'/'+str(j)+'.txt')
            j+=1
        print 'Completed function run'
    print j
    return j

start=1
for x in directories:
    start+=renumber_for_EOM(x,start)
