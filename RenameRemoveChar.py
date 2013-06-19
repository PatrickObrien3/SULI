
import os
import sys


for filename in os.listdir("."):
	if filename.startswith(str(sys.argv[1])):
		os.rename(filename, filename[int(sys.argv[2]):]+'.pdb')


exit()


#for filename in *.pdb ; do mv "$filename" "remd_$filename"; done;

