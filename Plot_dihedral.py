import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os
os.chdir("/Users/ronaldholt/Desktop/Ramplot/")
for i in range(2,30):
    fig=Figure(figsize=(10,10))
    canvas=FigureCanvas(fig)
    ax=fig.add_subplot(111)
    s, y =np.loadtxt('2KKJpsi'+str(i)+'.dat',usecols =(0, 1), unpack=True )
    r,x =np.loadtxt( '2KKJphi'+str(i)+'.dat',usecols=(0,1),unpack=True)
    t,v=np.loadtxt ('1JJS1phi'+ str(i) + '.dat', usecols=(0,1), unpack=True)
    q,w=np.loadtxt('1JJS1psi'+str(i)+'.dat', usecols=(0,1), unpack=True)
    ax.set_title('Res'+str(i))
    ax.set_xlim( (-190,190) )
    ax.set_ylim( (-190,190) )
    ax.set_ylabel("phi",fontsize=12)
    ax.set_xlabel("psi",fontsize=12)
    ax.scatter(x,y,color='r',s=10,marker='.',alpha=.3)
    ax.scatter(v,w,color='b',s=10,marker='.',alpha=.3)
    ax.legend(('2KKJ','1JJS'))
    ax.grid(True,linestyle='-',color='0.75')
    canvas.print_figure('res'+str(i)+'.png',dpi=100)
#    os.system("open res*")


