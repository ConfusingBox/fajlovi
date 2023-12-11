import numpy as np
import matplotlib.pyplot as plt
def zadatak2(x,y):
    if len(x) != len(y):
        raise Exception("GRESKAICACAS")
    p3 = np.polyfit(x,y,3)
    p4 = np.polyfit(x,y,4)
    px3 = np.polyval(p3,x)
    px4 = np.polyval(p4,x)
    abs3 = np.abs(y-px3)
    abs4 =np.abs(y-px4)

    mid3 = np.sum(abs3) / len(abs3)
    mid4 = np.sum(abs4) / len(abs4)
    if mid3<mid4:
        return mid3
    else:
        return mid4
    pass

x = np.array([1,2,3,4,5])
y = np.array([3,6,9,12,15])

px = zadatak2(x,y)
# plt.plot(x,px)
plt.show()