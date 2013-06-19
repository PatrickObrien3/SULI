import matplotlib.mlab as mlab
import os
import numpy as np
import matplotlib.pyplot as plt
from math import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

for i in range(2,60):
	fig=Figure(figsize=(10,10))
	canvas=FigureCanvas(fig)
	ax=fig.add_subplot(111)
	a, y =np.loadtxt('2KKJpsi'+str(i)+'.dat',usecols =(0, 1), unpack=True )
	b,x =np.loadtxt( '2KKJphi'+str(i)+'.dat',usecols=(0,1),unpack=True)
	c, r =np.loadtxt('1JJS1psi'+str(i)+'.dat',usecols =(0, 1), unpack=True )
	d,t =np.loadtxt( '1JJS1phi'+str(i)+'.dat',usecols=(0,1),unpack=True)
	ax.set_title('Res'+str(i))
	ax.set_ylabel("phi",fontsize=12)
	ax.set_xlabel("psi",fontsize=12)
	ax.scatter(x,y,s=20,color='tomato')
	ax.scatter(t,r,s=20,color='blue')
	ax.grid(True,linestyle='-',color='0.75')
	canvas.print_figure('res'+str(i)+'.png',dpi=500)

#for filename in os.listdir("."):
#	if filename.endswith(".txt"):
#		y = np.loadtxt(filename)
#		print 'Range is ' ,  y.min(), y.max()
#		print'Standard Dev is %8.4f' % y.std()
#		print'Mean is %8.4f' %y.mean()
#		n, bins,patches = plt.hist(y, 75, normed=False, facecolor='blue', alpha=0.75)
#		plt.xlabel('Distance')
#		plt.ylabel('Count')
#		plt.title(filename)
#		plt.xlim(9,35.0)
#		plt.ylim(0,7000)
#		plt.grid(True)
#		plt.show()



