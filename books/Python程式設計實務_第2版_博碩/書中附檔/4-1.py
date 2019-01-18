import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(0,360)
y = np.sin(x*np.pi/180)
plt.plot(x, y)
plt.xlim(0,360)
plt.ylim(-1.2, 1.2)
plt.title("SIN Function")
plt.show()
