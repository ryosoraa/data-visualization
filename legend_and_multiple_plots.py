# plot charts

import matplotlib.pyplot as plt
import numpy as np

stock_a = [100, 102, 97, 95, 91, 103, 120]
stock_b = [80, 102, 90, 92, 106, 110, 85]
stock_c = [68, 92, 49, 85, 92, 94, 100, 102]

plt.plot(stock_a, label='company 1')
plt.plot(stock_b, label='company 2')
plt.plot(stock_c, label='company 3')

# label is used to label or name each data line

plt.legend(loc='lower right')
# legend is used to display all the name lists for each line
# loc in legends is used to set the location of the list of line names

plt.show()
