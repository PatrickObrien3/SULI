import os,sys
import numpy as np
import pylab as plt


distances = (13, 17, 33, 43) #interesting ones from arvinf

n=0
fig=plt.figure(figsize=(12,9))
root='/home/jms/1JJS/ANAL/All/'

x,r12=np.loadtxt(str(root)+'13_17.out',unpack=True)
x,r13=np.loadtxt(str(root)+'13_33.out',unpack=True)
x,r14=np.loadtxt(str(root)+'13_43.out',unpack=True)
x,r23=np.loadtxt(str(root)+'17_33.out',unpack=True)
x,r24=np.loadtxt(str(root)+'17_43.out',unpack=True)
x,r34=np.loadtxt(str(root)+'33_43.out',unpack=True)


def calc_angle(a,b,c):
    A=np.degrees(np.arccos(((b)**2+(c)**2-(a)**2)/(2*(b)*(c))))
    B=np.degrees(np.arccos(((c)**2+(a)**2-(b)**2)/(2*(c)*(a))))
    C=180-A-B
    return A, B,C

A1,B1,C1=calc_angle(r14,r12,r24)
A2,B2,C2=calc_angle(r13,r12,r23)
A3,B3,C3=calc_angle(r34,r13,r14)
A4,B4,C4=calc_angle(r34,r23,r24)

rB1=90-B1
rB2=90-B2
angle1=180-rB1-rB2
