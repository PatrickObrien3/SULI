

MDIR='/global/scratch/sd/arvind/1JJS/neu/Equil'

x='ln -s ../$PREV/$PREV.rst.* .'
#PREV=srt
#DPRE=srt
x=0
PMEMD='mpirun -np 480 $AMBERHOME/exe/sander.MPI -ng 48 -groupfile equilibrate.groupfile '
run=( 'min1', 'min2', 'min3','min4', 'md1','md2', 'min11', 'md11' ,'min12', 'md12', 'min13', 'md13', 'min14', 'md14', 'min15', 'md15', 'md16')
for name in list( run):
    print 'cd', MDIR
    
    print 'mkdir', name
    print 'cp files/'+name+'.in', name 
    print 'cd', name
    print 'ln -s ../1JJS.top .'
    print 'cp ../temperature.dat .'
    print 'cp ../setup'+name ,'.'
    if name=='min1':
        print 'ln -s ../min.rst .'
    else:
        print 'ln -s ../'+run[(x)]+'/'+run[(x)]+'.rst* .'
        x=1+x
    print './setup'
    print PMEMD

      
