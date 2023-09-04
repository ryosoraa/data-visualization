import matplotlib.pyplot as plt
import numpy as np

ages = np.random.normal(20, 1.5, 1000)

plt.hist(ages, bins=20, cumulative=True)
# cumulative to sort the data from the smallest
# bins in hist can like = plt.hist(ages, bins=[ages.min(), ages.max()])
plt.show()
