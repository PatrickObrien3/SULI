# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:47:11 2013

@author: ronaldholt
"""

#!/bin/bash -f
i=1
run=( 'min1', 'min2', 'min3','min4', 'md1','md2', 'min11', 'md11' ,'min12', 'md12', 'min13', 'md13', 'min14', 'md14', 'min15', 'md15', 'md16')

for name in list( run):
    f=open('setup.'+name,'w')
    print>>f, '#!/bin/bash -f'
    print>>f, 'if [ -f groupfile ];'
    print>>f, 'then'
    print>>f,'  rm groupfile'
    print>>f, 'fi'

    print>>f, "nrep=`wc temperatures.dat | awk '{print $1}'`"
    print>>f,'echo $nrep'
    print>>f, 'count=0'
    print>>f,'for TEMP in `cat temperatures.dat`'
    print>>f,'do'
    print>>f,'  let COUNT+=1'
    print>>f,'  REP=`printf "%03d" $COUNT`'
    print>>f,'  echo "TEMPERATURE: $TEMP K ==> FILE: equilibrate.mdin.$REP"'
    print>>f,'  sed "s/XXXXX/$TEMP/g" ',name+'.in > temp '
    print>>f,'  sed "s/RANDOM_NUMBER/$RANDOM/g" temp > ',name+'.in.$REP'
    if name=='md16':
        print>>f,'  echo "-O -rem 0 -i ',name+'.in.$REP -o equilibrate.mdout.$REP -c ',name+'.rst.$REP -r remd.rst.$REP -ref',name+'.rst.$REP -x equilibrate.mdcrd.$REP -inf equilibrate.mdinfo.$REP -p 1JJS1.top" >> equilibrate.groupfile'
    else:
        print>>f,'  echo "-O -rem 0 -i ',name+'.in.$REP -o equilibrate.mdout.$REP -c ',name+'.rst.$REP -r ',run[i]+'.rst.$REP -ref' ,name+'.rst.$REP -x equilibrate.mdcrd.$REP -inf equilibrate.mdinfo.$REP -p 1JJS1.top" >> equilibrate.groupfile'
    i=1+i
    print>>f,'  rm -f temp'
    print>>f,'done'
    print>>f,'echo "#" >> groupfile'
    

    print>>f,'echo "N REPLICAS  = $nrep"'
    print>>f,'echo " Done."'
    f.close()