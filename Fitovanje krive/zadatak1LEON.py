import numpy as np
import matplotlib.pyplot as plt

def zadatak1(x,y):
    if len(x) != len(y):
        raise ValueError('Vektori nisu istih duzina')
    plt.plot(x,y,'red')
    p = np.polyfit(x,y,1)
    px = np.polyval(p,x)
    plt.plot(x,px,"or")
    plt.show()
    

x = np.array([1,2,3,4,5])
y = np.array([3,6,9,12,15])
zadatak1(x,y)