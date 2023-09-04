import matplotlib.pyplot as plt
import numpy


coding = ['C++', 'C#', 'Python', 'Java', 'Golang', 'kotlin']
score = [45, 69, 90, 60, 100, 120]
explodes = [0.2, 0, 0, 0, 0, 0]

plt.pie(score, labels=coding, explode=explodes,
        autopct='%.2f%%', pctdistance=0.7, startangle=90)

# labels use to name the part of each piece of pie
# explode is used to cut the desired part of the pie
# autopct is used to provide a percent value (%) for each slice of the pie
# pctdistance is used to provide the distance between autopct and the center of the pie
# startangle is used to tidy up the displayed data so that the line starts from the top
plt.show()
