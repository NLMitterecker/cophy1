import numpy as np
import matplotlib.pyplot as plt

string_dimension = 100
x = np.linspace(1/string_dimension, 1, num=string_dimension)
xscale = np.linspace(1, 100, num=100)
ynext = np.zeros(string_dimension) #string_dimension/(1/string_dimension)
k = 1000
x0 = 0.3
initial_position = np.exp(-1*k*(x - x0)**2)
ycurrent = initial_position
yprevious = initial_position

def propagate(ycurrent, yprevious):
    r = 1
    ynext=np.zeros(string_dimension)
    for steps in range(2, 99):
        ynext[steps] = 2*(1-r**2)*ycurrent[steps] - yprevious[steps] + (r**2)*(ycurrent[steps+1]+ycurrent[steps-1])
    return ynext

for steps in range(1,2000):
    ynext = propagate(ycurrent, yprevious)
    yprevious = ycurrent
    ycurrent = ynext
    plt.plot(xscale/string_dimension, ycurrent)
    plt.show()