import matplotlib.pyplot as plt
import numpy


coding = ['C++', 'C#', 'Python', 'Java', 'Golang']
score = [45, 69, 90, 60, 100]

plt.bar(coding, score, color='purple',
        align='edge', width=0.8, edgecolor='blue')
plt.show()
