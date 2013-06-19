import os

#for i in xrange(1,5):
#	os.system('grep LEU   '+str(i)+ '.pdb'');
os.chdir('/home/jms/REX-MD')
for i in range(1,5):
        filename= str(i)+'.pdb'
        output= 'Leu_' +str(i)+ '.pdb'
        os.system('grep LEU filename > output');
        print filename,output
