import numpy as np
import math

def zad4(x,y):
    if len(x) != len(y):
        raise Exception("GIGA GRESKA")
    p=[]
    red = 0
    greska = math.inf
    while greska>0.1:
        red = red + 1
        p = np.polyfit(x,y,red)
        px = np.polyval(p,x) #izracunaj p u tacki x
        greska = max(abs((y-px) / y) * 100)
    return p,greska,red
    pass

x = np.array([1,2,3,4,5])
y = np.array([3,6,9,12,15])
p = zad4(x,y)
print(p)