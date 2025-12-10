import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,6,0.2)

plt.plot([1,2,3,4],[1,2,4,4],".--b",t,t**2,".k")
plt.ylabel("afsoidjfoi")
plt.axis((0, 6, 0, 25))


plt.show()
