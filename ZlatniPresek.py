import numpy as np
import matplotlib.pyplot as plt
import math

def zlatniPresek(a,b,tol):
    c = (3 - math.sqrt(5)) / 2
    #korak 2 x1 x2
    x1 = a + c * (b-a)    
    x2 = a + b - x1
    n = 1
    #korak 3 iterativni postupak
    while (b - a) > tol:
        n = n+1
        if func(x1) <= func(x2):
            b = x2
            x1 = a + c * (b-a)
            x2 = a + b - x1
        else:
            a = x1
            x1 = a + c * (b-a)
            x2 = a + b - x1
    if func(x1) < func(x2):
        xopt = x1
        fopt = func(xopt)
    else:
        xopt = x2
        fopt = func(x2)
    return xopt, fopt ,n


def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f
###################
print("a")
a = 0
b = 3
tol = 0.0001
[xopt,fopt,tol] = zlatniPresek(a,b,tol)
print(xopt,fopt,tol)

x = np.linspace(0,4,1000)
f = np.linspace(0,0,len(x))
for i in range(0,len(x)):
    f[i] = func(x[i])

p = plt.plot(x,f, 'b--')
p = plt.plot(xopt,fopt,"*r",label = "min",markersize = 15, markeredgewidth = 1)
plt.show()