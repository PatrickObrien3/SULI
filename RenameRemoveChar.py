import sys
import os
for filename in os.listdir("."):
	if filename.startswith(sys.argv[1]):
<<<<<<< HEAD
		os.rename(filename, filename[int(sys.argv[2]):] + '.pdb')
=======
		os.rename(filename, filename[int(sys.argv[2]):] + 'x.pdb')
>>>>>>> 086d1d83b02725d861f5eb966fcc8dc37d7612c1


exit()


#for filename in *.pdb ; do mv "$filename" "remd_$filename"; done;

