import numpy as np
import matplotlib.pyplot as plt
import math

#(pocetna_tacka, kriterijum_zaustavljanja tj tolerancija)
def newtonRhapson(x0,tol):
    x_novo = x0
    x_pre = math.inf
    iteracije = 0
    while(abs(x_pre - x_novo) > tol):
        iteracije = iteracije + 1
        x_pre = x_novo
        x_novo = x_pre - dfunc(x_pre) / ddfunc(x_pre)
    x_opt = x_novo
    f_opt = func(x_opt)
    return x_opt,f_opt,iteracije


def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f

def dfunc(x):
    f = -(4*x**3 - 15*x**2 - 4*x + 24)
    return f

def ddfunc(x):
    f = -(12*x**2 - 30*x - 4)
    return f

####
tol = 0.0001
init_guess = 1
[x_opt,f_opt,iteracije] = newtonRhapson(init_guess,tol)
print(x_opt,f_opt,iteracije)

x = np.linspace(0,4,1000)
f = np.linspace(0,0,len(x))
for i in range(0,len(x)):
    f[i] = func(x[i])

p = plt.plot(x,f, 'b--')
p = plt.plot(x_opt,f_opt,"or",label = "min",markersize = 15, markeredgewidth = 1)
plt.show()