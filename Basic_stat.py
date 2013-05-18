import numpy as np
import pylab as plt

x,y=np.loadtxt("out.txt", usecols=(0,1), unpack=True)
print 'max is', y.max()
print 'min is', y.min()
print 'std is', y.std()
print 'mean is',y.mean()
print 'cmedian is', cmedian(y, numbins = 1000)
print 'mode is',mode(y)
#print 'size of the data = %6.4f, (min %6.4f , max %6.4f ), arithmetic mean %6.4f , unbiased variance %6.4f , biased skewness %6.4f , biased kurtosis %6.4f  ' %stats.describe(y,axis=0)
#print '(size of the data,(min, max), arithmetic mean, unbiased variance, biased skewness, biased kurtosis) ', stats.descrive(y=axis=0)

freq=itemfreq(y)



n, bins, patches = plt.hist(y, 100, normed=False, facecolor='green', alpha=0.75)



plt.xlabel('Rg')
plt.ylabel('Count')
plt.title(r'Histogram of Rg')

plt.grid(True)

plt.show()
