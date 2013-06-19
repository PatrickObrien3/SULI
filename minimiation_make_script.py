import os
x=open('MD18','w')
for i in range(1,7):
        print'/home/software/bin/sander -O -i  md18.in -o',str(i)+'md18.out',' -c,'str(i)+' min18.rst',' -p 1KBH_ww.top -r'str(i)+'restrt18',' -x'str(i)+' mdcrd'

