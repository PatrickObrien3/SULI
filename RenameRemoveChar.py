
import os
for filename in os.listdir("."):
	if filename.startswith("2KKJ."):
		os.rename(filename, filename[5:])


exit()


#for filename in *.pdb ; do mv "$filename" "remd_$filename"; done;

