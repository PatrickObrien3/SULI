for i in range(1,60):
    print 'dihedral', str(i)+'psi', ':'+str(i)+'@N', ':'+str(i)+'@CA', ':'+str(i)+'@C', ':'+str(i+1)+'@N', 'out', 'psi'+str(i)+'.dat'
    print 'dihedral', str(i)+'phi', ':'+str(i-1)+'@C', ':'+str(i)+'@N', ':'+str(i)+'@CA', ':'+str(i)+'@C', 'out', 'phi'+str(i)+'.dat'
