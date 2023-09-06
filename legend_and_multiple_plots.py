# ===============================================================
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

# ==================================================================

# PIE CHARTS

coding = ['C++', 'C#', 'Python', 'Java', 'Golang', 'kotlin']
score = [45, 69, 90, 60, 100, 120]

plt.pie(score, labels=None)
plt.legend(coding)
plt.show()

# The purpose of the program above is to remove the original label from the data that
#  is obtained and replace it with a custom label from outside or a list, and the index
#  between the list and the data you want to name must be the same
