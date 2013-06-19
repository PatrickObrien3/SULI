import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

figure = Figure()
canvas = FigureCanvas(figure)
axes = figure.add_subplot(1, 1, 1, axisbg='black')
#canvas.print_figure('red-bg.png')

#y = np.loadtxt('outfile.txt')
x, y = np.loadtxt('out.txt', usecols=(0, 1), unpack=True)
print 'Range is ' ,  y.min(), y.max()
print 'Standard Dev is %8.4f' % y.std()
print 'Mean is %8.4f' %y.mean()



Y= plt.hist(y, 100, normed=False, facecolor='blue',alpha=0.75)

#n, bins, patches

plt.xlabel('Rg')
plt.ylabel('Count')
plt.title(r'Histogram of Rg')
#plt.xlim(9,35.0)
#plt.ylim(0,7000)
plt.grid(True)

plt.show(facecolor='black')
