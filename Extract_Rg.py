a=1
f=open('out.txt','w')
for line in open("cryson_summary.txt"):
	if "Rg" in line:
		print>>f, a, line[-8:]
		a=a+1
		
	

