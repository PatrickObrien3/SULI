# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os
os.chdir("/Users/ronaldholt/Desktop/Ramplot/")
for i in range(2,60):
    fig=Figure(figsize=(10,10))
    canvas=FigureCanvas(fig)
    ax=fig.add_subplot(111)
   # x, y =np.loadtxt('2KKJpsi'+str(i)+'.dat',usecols =(0, 1), unpack=True )
  #  r,t =np.loadtxt( '2KKJphi'+str(i)+'.dat',usecols=(0,1),unpack=True)
    x,y=np.loadtxt ('1JJS1phi'+ str(i) + '.dat', usecols=(0,1), unpack=True)
    r,t=np.loadtxt('1JJS1psi'+str(i)+'.dat', usecols=(0,1), unpack=True)
    ax.set_title('Res'+str(i))
    #ax.set_xlim( (-190,190) )
    #ax.set_ylim( (-190,190) )
    ax.set_ylabel("phi",fontsize=12)
    ax.set_xlabel("psi",fontsize=12)
    ax.plot(x,y,color='r',alpha=.3)
    ax.plot(r,t,color='b',alpha=.3)
    ax.legend(('phi','psi'))
    ax.grid(True,linestyle='-',color='0.75')
    canvas.print_figure('phi_psi'+str(i)+'.png',dpi=100)
    print 'saved image',str(i) 