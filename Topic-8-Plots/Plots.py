#Richard Deegan
#This program will displays a plot of the functions
#f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes

#import required modules 
import matplotlib.pyplot as plt
import numpy as np 
# set range [0,4] using arange, increments of 0.1
x = np.arange(0,4,0.1)

# set y values as per question x,x2,x3 
y1= x
y2= x**2
y3= x**3
#plot points and title to include function 
plt.plot(y1, label = "$f(x)=x$")

plt.plot(y2, label = "$g(x)=x**2$")
    
plt.plot(y3, label = "$h(x)=x**3$")
    
#legend, x and y asis and graph of plot
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#References:
#https://matplotlib.org/tutorials/introductory/pyplot.html
#https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python
