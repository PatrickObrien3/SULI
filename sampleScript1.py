import os

os.system('mkdir IvsQ')
 
for i in range(1,50000):
	     
	os.system('cryson  ' +str(i)+ '.pdb'' -sm 0.3 -ns 100 -dro 0.0'); 
os.system('rm -rf *.alm *.log ');
os.system('mv *.int IvsQ/'); 



#os.system('cryson *.pdb exp.dat -cst')
#os.system('cryson adk_dims1_0.pdb')
#os.system('rm -rf *.alm *.log')
#os.system('mkdir IvsQ')
#os.system('mv *.int')

