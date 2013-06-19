make new directory for the run

move to the directory

export CUDA_VISIBLE_DEVICES= '0'

source ~/.bashrc

link the restrt file from the last run to the new directory as the 1JJS1.crd

cp the topology file to the folder as 1JJS1.top

cp the mdweb.in file to the folder as itself 

nohup /home/software/bin/pmemd.cuda_SPFP -O -i mdweb.in -o mdweb.out -p 1JJS1.prmtop -c 1JJS1.inpcrd -r restrt -x mdcrd &





import os
TOP=1JJS1.top
restart=1JJS1.crd.md16

os.mkdir( 'Equil')
os.system('mv * Equil')
os.mkdir( 'Prod')
os.chdir('Prod')
os.system( 'ln -s ../Equil/Struct/'TOP'')
os.mkdir('Prod-0-200ns')
os.chdir('Prod-0-200ns')
os.system( 'ln -s ../'top'')
os.system( 'ln -s ../../Equil/md16/'Restart'')
os.system( 'mv 'restart' RST')
os.system( 'nohup /home/software/bin/pmemd.cuda.V12_gnu -0 -p 'top' -c 'RST' -i mdwed.in -o mdweb.out -r resrt -x mdcrd &')


