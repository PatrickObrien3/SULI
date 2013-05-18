import numpy
import math
import scipy.stats
import sys
from KabschAlign import *
from IterativeMeansAlign import *
from matplotlib import cm
from MDAnalysis import *

from jade import *




#TOP=sys.argv[1]
#DCD=sys.argv[2]
#FILE=sys.argv[3]

PROTEIN='1JJS2'
#u = MDAnalysis.Universe(TOP,DCD, permissive=False)

#u = MDAnalysis.Universe('../data/ubq_1111.pdb', '../data/UBQ_500ns.dcd', permissive=False);
#u = MDAnalysis.Universe("/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS1/1JJS1ww.pdb","/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS1/1JJS1_2us.dcd", permissive=False);
u = MDAnalysis.Universe("/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS2/1JJS2ww.pdb","/Users/ronaldholt/Google_Drive/ORNL_Research/1JJS/1JJS2/1JJS2_1us.dcd", permissive=False);
#u = MDAnalysis.Universe("/Users/ronaldholt/NCBD/From_Arvind/1JJS/1JJS3/1JJS3ww.pdb","/Users/ronaldholt/NCBD/From_Arvind/1JJS/1JJS3/1JJS3_600ns.dcd", permissive=False);

FRame,ENERGY=numpy.loadtxt(PROTEIN+'/Norm_Energy.txt',usecols=(0,1),delimiter=" ",unpack=True)
#u = MDAnalysis.Universe('../../tmp/2V93_1.pdb', '../../tmp/2V93.dcd', permissive=False);
ca = u.selectAtoms('name CA');
#ca = u.selectAtoms('not (type H)');
cacoords = []; frames = [];

colormap=cm.gist_rainbow

for ts in u.trajectory:
	f = ca.coordinates();
	cacoords.append(f.T);
	frames.append(ts.frame);

print "shape of cacoords is ", numpy.shape(cacoords);

dim = 3; Na = 59; #num_frame=50000;
num_frame=numpy.shape(cacoords)[0]

print num_frame
iterAlign = IterativeMeansAlign();
[itr, avgCoords, eRMSD, newCoords] = iterAlign.iterativeMeans(cacoords, 0.001, 10);



print "shape of eRMSD is",numpy.shape(eRMSD);

coords = numpy.reshape(newCoords, (len(newCoords), dim*Na)).T; 
print 'coords: ', numpy.shape(coords); 
avgCoords = numpy.mean(coords, 1); print avgCoords;
print 'avgCoords: ', numpy.shape(avgCoords);
tmp = numpy.reshape(numpy.tile(avgCoords, num_frame), (num_frame,dim*Na)).T; 
caDevsMD = coords - tmp;
#print numpy.shape(caDevsMD); print caDevsMD[0];

D = caDevsMD.flatten(); print numpy.shape(D);
gm = numpy.mean(D); 
gs = numpy.std(D);
gK = scipy.stats.kurtosis(D,0,fisher=False);

[n,s] = numpy.histogram(D, bins=51,normed=1);

gp = numpy.exp(-(s-gm)**2/(2*gs*gs));
gp = gp/numpy.sum(gp); print numpy.shape(gp);

lo = 0; hi = len(s);

fig = plt.figure();
ax = fig.add_subplot(111);
x = 0.5*(s[1:] + s[:-1]);
#ax.semilogy(s[lo:hi], gp[lo:hi],'c-',linewidth=2);
ax.hold(True); 
ax.semilogy(x, n, 'k-', linewidth=2.0); ax.axis('tight');
#plt.show();


print 'Mean: ', gm;
print 'Std. dev: ', gs;
print 'Kurtosis: ', gK;

cc = coords[:,0]; print numpy.shape(cc);
cc = numpy.reshape(cc, (dim,Na));
print numpy.shape(coords[0:-1:3,0]), numpy.shape(coords[1:-1:3,0]), numpy.shape(coords[2:-1:3,0]);

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
ax.plot(cc[0,:], cc[1,:], cc[2,:]);
plt.show();

print "shape of numpy.cov is ",numpy.shape(numpy.cov(coords));
[pcas,pcab] = numpy.linalg.eig(numpy.cov(coords));
si = numpy.argsort(-pcas.ravel()); print si;
pcaTmp = pcas;
pcas = numpy.diag(pcas);
pcab = pcab[:,si];

fig = plt.figure();
ax = fig.add_subplot(111);
#cs = ax.contourf(numpy.cov(coords));
#ax.colorbar(cs); 
#plt.show();

#fig = plt.figure();
#ax = fig.add_subplot(111);
#y = numpy.cumsum(pcaTmp.ravel()/numpy.sum(pcaTmp.ravel()));
#ax.plot(y);
#plt.show();

#fig = plt.figure(figsize=(10,10),dpi=300);
#ax = fig.add_subplot(111, projection='3d');
pcacoffs = numpy.dot(pcab.conj().T, caDevsMD);
pcacoffs =numpy.real(pcacoffs)
print "shap of pcaoffs is", numpy.shape(pcacoffs);
i=1
#P=ax.scatter(pcacoffs[0,:], pcacoffs[1,:], pcacoffs[2,:], marker='o', c=ENERGY,cmap=colormap );
fig = plt.figure(figsize=(12,12),dpi=300);
for j in range(40,361,40):
    #fig = plt.figure(figsize=(10,10),dpi=100);
    ax = fig.add_subplot(3,3,i, projection='3d');
    P=ax.scatter(pcacoffs[0,:], pcacoffs[1,:], pcacoffs[2,:], marker='o', c=ENERGY,cmap=colormap );
    cbar = fig.colorbar(P,ticks=[-3,0,3])
    cbar.ax.set_yticklabels(['<-3','0','>3'])
        #plt.savefig("Image1.png",dpi=300)
    ax.view_init(0,j)
    #plt.savefig(str(PROTEIN)+"/PCA_"+str(j)+".png",dpi=100)
    #fig.clf()
    i=i+1
plt.savefig(FILE+"_PCA.png",dpi=300,bbox_inches='tight')
#plt.show();

# some set up for running JADE
Ncyc  = 1;
subspace = 30;
lastEig = subspace; # number of eigen-modes to be considered
numOfIC = subspace; # number of independent components to be resolved

icajade = jadeR(coords, lastEig); 
print numpy.shape(icajade);
icacoffs = numpy.dot(icajade, caDevsMD);
icacoffs = numpy.asarray(icacoffs); 
print 'icacoffs: ', numpy.shape(icacoffs);

i=1
fig = plt.figure(figsize=(12,12),dpi=300);
for j in range(40,361,40):
    #fig = plt.figure(figsize=(10,10),dpi=300);
    ax = fig.add_subplot(3,3,str(i), projection='3d');
    P=ax.scatter(icacoffs[0,:], icacoffs[1,:], icacoffs[2,:], marker='o', c=ENERGY,cmap=colormap); 
    cbar = fig.colorbar(P,ticks=[-3,0,3])
    cbar.ax.set_yticklabels(['<-3','0','>3'])
    ax.view_init(0,j)
    #plt.savefig(str(PROTEIN)+"/QAA_"+str(j)+".png",dpi=100)
    #fig.clf()
    i=i+1
plt.savefig(FILE+"_QAA.png",dpi=300,bbox_inches='tight')
#plt.show();
