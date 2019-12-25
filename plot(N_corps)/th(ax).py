"""

@author: Arfaoui Mehdi
"""



import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy 
a_min = -3000  
a_max =3000  
ai = 1
def f(x):
     return numpy.tanh(ai*x)
    #(1-np.exp(-2*x))/ (1+np.exp(-2*x))
fig = plt.figure()
x = numpy.arange(-10, 10,0.01)

# plt.axes((left, bottom, width, height), facecolor='w')
sin_ax = plt.axes([0.10, 0.2, 0.8, 0.65])
plt.axes(sin_ax)
plt.suptitle('f(x)=th(ax)')
plt.title('f(x)= th(ax)')
plt.xlabel('x')
plt.ylabel('f(E)',rotation=0)
fd,=plt.plot(x, f(x),'r')


# here we create the slider
a_slider = Slider(plt.axes([0.2, 0.05, 0.65, 0.05])
          ,      # the axes object containing the slider
      'Varie a',            # the name of the slider parameter
      a_min,          # minimal value of the parameter
      a_max,          # maximal value of the parameter
      valinit=ai  # initial value of the parameter
     )
def update(T):
    fd.set_ydata(numpy.tanh(a_slider.val*x)) 
    fig.canvas.draw_idle()


a_slider.on_changed(update)
plt.show()
