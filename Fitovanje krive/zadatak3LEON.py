import numpy as np
def zadatak3(x,y):
    if len(x) != len(y):
        raise Exception("hdahgdias")
    p5 = np.polyfit(x,y,5)
    p6 = np.polyfit(x,y,6)
    px3 = np.polyval(p5,x) #izracunaj p3 u tacki x
    px4 = np.polyval(p6,x)
    return p5,p6