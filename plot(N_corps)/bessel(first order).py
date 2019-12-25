"""
Created on Wed Dec 24 00:56:24 2019

@author: Arfaoui Mehdi
"""



import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,100,0.1)
def g(x):
    return (3*(np.sin(x)-x*np.cos(x))/(x**3))
plt.xlim(0,20)
plt.plot(x,g(x))
plt.axhline(0, color='r', lw=1)
plt.show()
