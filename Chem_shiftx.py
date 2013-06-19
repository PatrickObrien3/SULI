f=open('shift_x','w')
for i in range(1,50001):
    print>>f, '/home/rarvind/Install/shiftx/./shiftx','1', str(i)+'.pdb', str(i)+'.out'
