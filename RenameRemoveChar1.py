import sys
import os
j=1
for filename in os.listdir("."):
	if filename.startswith(sys.argv[1]):
		os.rename(filename, filename[int(sys.argv[2]):] + 'x.pdb')


exit()


#for filename in *.pdb ; do mv "$filename" "remd_$filename"; done;

