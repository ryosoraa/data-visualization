import matplotlib.pyplot as plt
import numpy


coding = ['C++', 'C#', 'Python', 'Java', 'Golang']
score = [45, 69, 90, 60, 100]

plt.bar(coding, score, color='purple',
        align='edge', width=0.8, edgecolor='blue')
# The color parameter is used to change the color
# align parameter to adjust the position of the text below the plot
# width to set the thickness of the bar
# edgecolor is used to color the outside of the bar

plt.show()
