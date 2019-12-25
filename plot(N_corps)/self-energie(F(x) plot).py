"""

@author: Arfaoui Mehdi
"""


import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,1000.01,0.01)
def g(x):
    return 1+((1-x**2)/2*x)*np.log(abs((1+x)/(1-x)))
plt.xlim(0,2)
plt.ylim(0,3)
plt.plot(x,g(x))
plt.axvline(1, color='r', lw=1,linestyle='--')
plt.show()
