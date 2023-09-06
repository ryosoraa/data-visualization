import matplotlib.pyplot as plt
import numpy as np

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
income = [55, 56, 78, 79, 83, 84, 90, 94]

income_ticks = list(range(50, 100, 2))

plt.plot(years, income)
plt.title('income in year', fontsize=20, fontname='verdana')
# fontsize is used to set the font size
# fontname is used to set the type of font used

plt.xlabel('years')
plt.ylabel('income')
plt.yticks(income_ticks, [f'Rp {x}k' for x in income_ticks])

# yticks are used to assign values ​​to the left of the data table

plt.show()
