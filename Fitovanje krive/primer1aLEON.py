import numpy as np
import matplotlib.pyplot as plt

F = np.array([1,2,3,4,5])
x = np.array([3,6,9,12,15])

p = np.polyfit(F,x,1) #nezavisna zavisna prvi red       x = aF + b
f = np.polyval(p,F) #odredjujemo vrednost polinoma p u tackama F
print(p)
N7 = np.polyval(p,7)
print(N7)
plt.plot(F,f)
plt.plot(F,x,"or")
plt.show()

