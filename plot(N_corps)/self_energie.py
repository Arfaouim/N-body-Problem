"""
Created on Lun Dec 15 00:56:24 2019

@author: Arfaoui Mehdi
"""


import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from sympy import*
#import playsound
#playsound.playsound('a.mp3',True)
init_printing()
x,y=symbols('x y')
X = np.arange(-1000,1000,0.001)
def f(x):
    print('f(x)=')
    print(pretty((1+(ln((1+x)/(1-x))*(1-x**2))/(2*x))))
    #return 1+(ln((1+x)/(1-x))*(1-x**2))/(2*x)
def  f1(x):
    return 1+(ln((1+x)/(1-x))*(1-x**2))/(2*x)
def g(x):
    return 1+((1-x**2)/2*x)*np.log(abs((1+x)/(1-x)))
def F(x):
    print(' /')
    print('|')
    print('| F(x) dx')
    print('|')
    print('/')
    print('=')
    print(pretty(Integral((x**2)*f1(x),x)))
    print('=')
    return  integrate((x**2)*f1(x),(x,0,1))
def plot():
    plt.xlabel('x')
    plt.ylabel('f(x)',rotation=0)
    plt.title(r'$f(x)=1+\dfrac{1-x^{2}}{x}\log\left(|\dfrac{1+x}{1-x}|\right)$ ',fontsize=16)
    #plt.semilogx(x,f(x),label='Inline label', linewidth=2)
    #plt.plot(x,f(x))
    plt.plot(X,g(X),label='x', linewidth=2)
    plt.xlim(0, 3)
    plt.ylim(0, 2) 
    plt.tick_params(labelcolor='b', labelsize='medium', width=3)
    plt.grid(True, linestyle='-.')
    plt.legend()
    plt.show()

