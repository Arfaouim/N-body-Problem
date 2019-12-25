"""
Created on Wed Dec 25 00:56:24 2019

@author: Arfaoui Mehdi
"""



import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jn
n=1.0e22 
x=np.arange(0,1000.01,0.01)
def delta(n):
    listofzeros = [0] * n+[1.0e308]+[0] * n
    return listofzeros
def ppar(x):
    return (n*delta(50000))/2+n**2*(1-jn(0, x)**2)/4
def ppar1(x):
    return n**2*(1-jn(0, x)**2)/4+n/2
plt.xlim(0,20)
plt.ylim(0,(n**2)/3)
plt.plot(x,ppar1(x),label='parallel')
plt.axhline((n**2)/4, color='r', lw=1)
plt.yticks([(n**2)/4], [r'$\frac{n^{2}}{4}$'],label='antip')
plt.xticks([2.4], [r'$\frac{3\pi}{2k_f}$'],label='antip')
plt.axvline(2.4, color='r', lw=1,linestyle='--')
plt.legend()
plt.grid()
plt.show()
