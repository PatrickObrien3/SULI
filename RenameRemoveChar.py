
import os
for filename in os.listdir("."):
	if filename.startswith("1KHB2."):
		os.rename(filename, filename[6:]+'.pdb')


exit()


#for filename in *.pdb ; do mv "$filename" "remd_$filename"; done;

