import os

os.system('mkdir IvsQ')

for i in range(1,20001):

        os.system('cryson ''1KBH.'+str(i)+ '.pdb'' -sm 0.3 -ns 100 -dro 0.0');
os.system('rm -rf *.alm *.log ');
os.system('mv *.int IvsQ/');

