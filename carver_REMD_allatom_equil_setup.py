

MDIR='$SCRATCH/1KBH/Equil'

x='ln -s ../$PREV/$PREV.rst.* .'
#PREV=srt
#DPRE=srt
x=0
PMEMD='mpirun -np 480 $AMBERHOME/exe/sander.MPI -ng 48 -groupfile equilibrate.groupfile '
run=( 'min1', 'min2', 'min3','min4', 'md1','md2', 'min11', 'md11' ,'min12', 'md12', 'min13', 'md13', 'min14', 'md14', 'min15', 'md15', 'md16')

f=open('remd.pbs','w')
print>>f,"#PBS -q regular \n#PBS -A m1503 \n#PBS -l nodes=64:ppn=8 \n#PBS -l walltime=4:00:00 \n#PBS -N remd.1KBH_all_48 \n#PBS -e remd.1KBH_all_48.$PBS_JOBID.err \n#PBS -o remd.1KBH_all_48.$PBS_JOBID.out \n#PBS -V"
for name in list( run):
    print>>f, 'cd', MDIR
    
    print>>f, 'mkdir', name
    print>>f, 'cp files/'+name+'.in', name 
    print>>f, 'cd', name
    print>>f, 'ln -s ../1KBH_ACTR.prmtop .'
    print>>f, 'cp ../temperatures.dat .'
    print>>f, 'cp ../files/setup.'+name ,'.'
    if name=='min1':
        print>>f, 'ln -s ../min.rst .'
    else:
        print>>f, 'ln -s ../'+run[(x)]+'/'+run[(x+1)]+'.rst* .'
        x=1+x
    print>>f,'chmod +x setup.'+name
    print>>f, './setup.'+name
#    print'cd $PBS_O_WORKDIR'
    print>>f, 'module load amber'
    print>>f, PMEMD
f.close()
      
