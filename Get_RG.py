

f=open('outfile.txt','w')
for line in open("Rg.txt"):
	if "Rg" in line:
		print>>f, line[-8:]
         
