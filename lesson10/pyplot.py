from matplotlib import pyplot as plt
import numpy as np
import math
x=np.arange(-2*math.pi,2*math.pi,0.01)
y=np.sin(x)/x
plt.plot(x,y)
plt.show()