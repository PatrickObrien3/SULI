import os



filePREFIX = 'adk_dims1'; 
for i in range(0,98):
	os.system('cryson ' + filePREFIX + '_' + str(i) + '.pdb  -sm 0.3 -ns 100 '); 
	os.system('rm -rf *.alm *.log ');
	os.system('mkdir IvsQ')
	os.system('mv *.int IvsQ/'); 
os.system( 'rm *.pdb' )


#os.system('cryson *.pdb exp.dat -cst')
#os.system('cryson adk_dims1_0.pdb')
#os.system('rm -rf *.alm *.log')
#os.system('mkdir IvsQ')
#os.system('mv *.int')

