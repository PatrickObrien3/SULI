def Extract(filename):
	f=open('out.txt','w')
	for line in open(filename):
		for i in range(100,5000,100):
			if str(i) in line:
				print>>f,  line[:]
if name == "__main__":
	import sys
	Extract((sys.argv[1]))
