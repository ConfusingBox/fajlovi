import numpy as np
import matplotlib.pyplot as plt
import math 
import numpy.linalg as lin

def parabola(x1,x3,tol):
    X = np.array([x1,(x1+x3)/2,x3]).transpose()
    pom = np.array([1,1,1]).transpose()
    Y = np.array([pom,X,X*X]).transpose()

    F =np.linspace(0,0,len(X))
    for i in range(0,len(x),1):
        F[i] = func(X[i])
    abc = lin.solve(Y,F)
    x = -abc[1]/2/abc[2]
    fx = func(x)
    n =0

    while np.abs(np.dot([1,x,x**2],abc)- fx) > tol:
        if (x > X[1]) and (x < X[2]):
            if (fx < F[1]) and (fx < F[2]):
                X = np.array([X[1],x,F[2]])
                F = np.array([F[1],fx,F[2]])
def func(x):
    f = -(x**4 - 5*x**3 - 2*x**2 + 24*x)
    return f