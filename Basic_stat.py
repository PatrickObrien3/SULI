import numpy as np
import pylab as plt
import sys


x,y,z=np.loadtxt(sys.argv[1], usecols=(0,1,2), unpack=True)
print 'Rg max is', y.max()
print 'Rg min is', y.min()
print 'Rg std is', y.std()
print 'Rg mean is',np.average(y)
#print 'Rg mode is',mode(y)
#print 'size of the data = %6.4f, (min %6.4f , max %6.4f ), arithmetic mean %6.4f , unbiased variance %6.4f , biased skewness %6.4f , biased kurtosis %6.4f  ' %stats.describe(y,axis=0)
#print '(size of the data,(min, max), arithmetic mean, unbiased variance, biased skewness, biased kurtosis) ', stats.descrive(y=axis=0)

print 'Dmax max is', z.max()
print 'Dmax min is', z.min()
print 'Dmax std is', z.std()
print 'Dmax mean is',np.average(z)
#print 'Dmax mode is',mode(z)


