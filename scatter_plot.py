import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

# print(x_data)

plt.scatter(x_data, y_data, marker='*')
# The marker parameter is used to change the desired point image
plt.show()
