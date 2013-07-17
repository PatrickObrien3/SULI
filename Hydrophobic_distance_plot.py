import os,sys
import numpy as np
import pylab as plt


distances = (13, 17, 33, 43) #interesting ones from arvinf
#distances = (9,12,16,29,32 ,38 ) # leucine
#distances=(5, 10, 13, 14, 17, 29, 30, 32, 33, 44, 55, 58) 
#distances = (5, 32,  44) # Isoleucine

"""
F=open('trajin_hydrophobic_distance','w')
print>>F, 'trajin  '+str(sys.argv[1])+'.dcd'
print>>F,' '

os.system('rm *out')


for i in distances:
        for j in distances:
            if i<j:
                print>>F, 'distance','distance'+str(i)+'_'+str(j),':'+str(i)+'@CA', ':'+str(j)+'@CA', 'out', str(i)+'_'+str(j)+'.out'
            else:
                continue
                
F.close()
os.system('ptraj  '+str(sys.argv[1])+'.prmtop   trajin_hydrophobic_distance')


"""
n=0
fig=plt.figure(figsize=(12,9))
for i in distances:
    for j in distances:
        if i<j:
            #n=1+n
            #plt.subplot(3,2,n)
            x,y=np.loadtxt(str(i)+'_'+str(j)+'.out',unpack=True)
            #plt.plot(x,y,label=str(i)+'_'+str(j))
            #plt.legend(loc=0)
            n=n+1
            plt.subplot(3,2,n)
            plt.hist(y,100,label=str(i)+'_'+str(j))#, orientation='horizontal')
            plt.legend(loc=0)
        else:
            continue
plt.legend(loc=0)
fig.tight_layout()
plt.savefig('Hydro_distance.png',dpi=150,bbox_inches='tight')
plt.show()
