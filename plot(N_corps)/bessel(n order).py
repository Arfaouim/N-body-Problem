"""
Created on Wed Dec 23 00:56:24 2019

@author: Arfaoui Mehdi
"""


# jn : Bessel de premier type
# yn : Bessel de deuxième type
import numpy as np
import pylab as pl
from scipy.special import jn, yn
# Bessel de premier type
#print "J_%d(%f) = %f" % (n, x, jn(n, x))

x = np.linspace(0, 10, 100)

for n in range(4):
    pl.plot(x, jn(n, x), label=r"$J_%d(x)$" % n)
pl.xlim(0,10)    
pl.legend()
pl.show()
