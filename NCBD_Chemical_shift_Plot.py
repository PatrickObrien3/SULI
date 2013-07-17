import matplotlib.pyplot as plt
import numpy as np

JJS='/home/jms/NMR_Chemical_shift/15398_unbound_NCBD/'
CA_JJS=np.loadtxt(str(JJS)+'CA.txt',skiprows=1)
C_JJS=np.loadtxt(str(JJS)+'C.txt',skiprows=1)
HA_JJS=np.loadtxt(str(JJS)+'HA.txt',skiprows=1)

KKJ='/home/jms/NMR_Chemical_shift/16363_unbound_2KKJ/'
CA_KKJ=np.loadtxt(str(JJS)+'CA.txt',skiprows=1)
C_KKJ=np.loadtxt(str(JJS)+'C.txt',skiprows=1)
HA_KKJ=np.loadtxt(str(JJS)+'HA.txt',skiprows=1)

JJS='/home/jms/NMR_Chemical_shift/5228_ACTR_NCBD/NCBD/'
CA_JJS=np.loadtxt(str(JJS)+'CA.txt',skiprows=1)
C_JJS=np.loadtxt(str(JJS)+'C.txt',skiprows=1)
HA_JJS=np.loadtxt(str(JJS)+'HA.txt',skiprows=1)

JJS='/home/jms/NMR_Chemical_shift/15398_unbound_NCBD/'
CA_JJS=np.loadtxt(str(JJS)+'CA.txt',skiprows=1)
C_JJS=np.loadtxt(str(JJS)+'C.txt',skiprows=1)
HA_JJS=np.loadtxt(str(JJS)+'HA.txt',skiprows=1)



CA=np.loadtxt('ca_aligned.txt',skiprows=1)
cc_CA=np.corrcoef(CA[:,1],CA[:,3])

HA=np.loadtxt('ha_aligned.txt',skiprows=1)
cc_HA=np.corrcoef(HA[:,1],HA[:,3])

C=np.loadtxt('c_aligned.txt',skiprows=1)
cc_C=np.corrcoef(C[:,1],C[:,3])

fig = plt.figure(figsize=(10,6),dpi=300)



ax1=fig.add_subplot(311)
ax1.errorbar(HA[:,2],HA[:,3],yerr=HA[:,4],label='HA')
ax1.plot(HA[:,0],HA[:,1],'ro',alpha=.5,label='exp HA ACTR/NCBD')
ax1.text(21, 4.25, 'H'+r'$\alpha$', color='k',fontsize=18)
ax1.text(80, 5.25, 'Cor.Coef.='+str(cc_HA[0,1]), color='k',fontsize=18)
#plt.title('HA')
plt.ylim(3.0,6.0)
col_labels=['col1','col2','col3']
row_labels=['row1','row2','row3']
table_vals=[11,12,13,21,22,23,31,32,33]
table = r'''\begin{tabular}{ c | c | c | c } & col1 & col2 & col3 \\\hline row1 & 11 & 12 & 13 \\\hline row2 & 21 & 22 & 23 \\\hline  row3 & 31 & 32 & 33 \end{tabular}'''
plt.text(9,3.4,table,size=12)

ax2=fig.add_subplot(312)
A=ax2.errorbar(CA[:,0],CA[:,3],yerr=CA[:,4],label='MD CA')
B=ax2.plot(CA[:,0],CA[:,1],'ro',alpha=.5,label='exp CA ACTR/NCDB')
ax2.text(21, 55,'C'+ r'$\alpha$', color='k',fontsize=18)
ax2.text(80,42.5,'Corr.Coef ='+ str(cc_CA[0,1]), color='k',fontsize=18)
#plt.title('CA')
plt.ylim(40,70)
col_labels=['col1','col2','col3']
row_labels=['row1','row2','row3']
table_vals=[11,12,13,21,22,23,31,32,33]
table = r'''\begin{tabular}{ c | c | c | c } & col1 & col2 & col3 \\\hline row1 & 11 & 12 & 13 \\\hline row2 & 21 & 22 & 23 \\\hline  row3 & 31 & 32 & 33 \end{tabular}'''
plt.text(9,3.4,table,size=12)

ax3=fig.add_subplot(313)
ax3.errorbar(C[:,2],C[:,3],yerr=C[:,4],label='C')
ax3.plot(C[:,0],C[:,1],'ro',alpha=.5,label='exp C ACTR/NCBD')
#plt.title('C')
ax3.text(21, 176, r'C', color='k',fontsize=18)
ax3.text(80, 170, r'Corr.Coeff='+str(cc_C[0,1]), color='k',fontsize=18)
plt.ylim(168,182)

col_labels=['col1','col2','col3']
row_labels=['row1','row2','row3']
table_vals=[11,12,13,21,22,23,31,32,33]
table = r'''\begin{tabular}{ c | c | c | c } & col1 & col2 & col3 \\\hline row1 & 11 & 12 & 13 \\\hline row2 & 21 & 22 & 23 \\\hline  row3 & 31 & 32 & 33 \end{tabular}'''
plt.text(9,3.4,table,size=12)



fig.tight_layout()

fig.legend((A),('MD' ), 'upper left')
fig.legend((B),('Experimental ACTR/NCBD'), 'upper right')
fig.savefig('Chem_shift.png',dpi=300)

#plt.show()