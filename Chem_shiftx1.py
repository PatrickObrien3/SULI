import sys, os

for i in range(1,50001,100):
    os.system('/home/jms/Install/shiftx/./shiftx 1 '+str(i)+'x.pdb', str(i)+'.out')
