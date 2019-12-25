"""
Created on Wed Dec 20 00:56:24 2019

@author: Arfaoui Mehdi
"""



import matplotlib.pyplot as plt
import numpy as np
h=1.05457e-34 #(js)
m=9.1094e-31 #(kg)
k_label=[r"$-\pi/a$",r"$0$", r"$\pi/a$"]
#k=np.arange(-2*np.pi,2*np.pi,np.pi/10)
k=np.arange(-30,30,0.1)
fig, ax = plt.subplots()
#ax.set_xticklabels(k_label)
#plt.xlim(-2*np.pi,2*np.pi)
plt.plot(k,(h**2)*(k**2)/(2*m))
plt.axvline(0,linestyle='--',color='g')
plt.ylim(0,6.e-36)
plt.show()
