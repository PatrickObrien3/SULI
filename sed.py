import sys, os 
if str(sys.argv[1])=='1JJS':
    for i in range(1,50001):
        os.system(" sed '62,122d' "+str(i)+'.out >>  '+str(i)+'.txt' )
if str(sys.argv[1])=='1KBH':
    for i in range(1,50001):
        os.system("sed '134,1805d' "+str(i)+'.out >>  '+str(i)+'.txt')
if str(sys.argv[1])=='ACTR':
    for i in range(1,50001):
        os.system("sed '75,151d' "+str(i)+'.out >>  '+str(i)+'.txt')

#for i in range(1,50001):
    #for ACTR
    #print>>f, "sed '75,151d' ",str(i)+'.out', '>>', str(i)+'.txt'
   #for 1JJS
   # print>>f, "sed '62,122d' ",str(i)+'.out', '>>', str(i)+'.txt'
    #for 1KBH
   # print>>f, "sed '134,1805d' ",str(i)+'.out', '>>', str(i)+'.txt'
