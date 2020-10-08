import time
import numpy as np
import matplotlib.pyplot as plt
voltage= np.array([0,3,4,5,6,7.2])
current = np.array([0,110,120,130,140,150])
plt.figure(1)
plt.plot(voltage,current)
plt.title('voltage-current curve:320011041')
plt.xlabel('voltage(V)')
plt.ylabel('current(mA)')
plt.grid(axis='both')
plt.show(1)