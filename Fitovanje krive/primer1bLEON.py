import numpy as np
import matplotlib.pyplot as plt

F = np.array([1,2,3,4,5])
x = np.array([3,6.5,9,11,15])

p = np.polyfit(F,x,1)
f = np.polyval(p,F) #odredjujemo vrednost p u tackama F
N7 = np.polyval(p,7)
print(N7    )

abs_gr = np.abs(f-x)
print(abs_gr)
rel_gr =  abs_gr/x * 100
print(rel_gr)
plt.plot(F,f)
plt.plot(F,x,"or")
plt.show()