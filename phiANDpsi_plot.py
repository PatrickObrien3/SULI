import numpy as np
import os
import matplotlib.pyplot as plt

for i in range(2,60):
	x,y=np.loadtxt("1JJS1phi"+str(i)+".dat",unpack=True)
	r,t=np.loadtxt("1JJS1psi"+str(i)+".dat",unpack=True)
	plt.plot(x,y,color='b',legend="phi")
	plt.plot(r,t,color='r',legend="psi")
	plt.show()
