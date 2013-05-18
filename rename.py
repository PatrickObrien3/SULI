
import os
for filename in os.listdir("."):
	if filename.startswith("2KKJ."):
		os.mv(filename, filename.pdb)
		os.rename(filename, filename[5:])



ls


#for filename in *.pdb ; do mv "$filename" "remd_$filename"; done;

