import numpy as np
import matplotlib.pyplot as plt

years = [2005 + x for x in range(10)]
weight = [24, 25, 26, 36, 47, 57, 68, 68, 58, 40]

plt.plot(years, weight, c='b', lw=2, linestyle='--')
# parameter c to change the color
# lw parameter to change the line size
# linestyle to change the line style

plt.show()
