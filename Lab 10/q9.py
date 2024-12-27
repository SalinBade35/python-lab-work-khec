# create a histogram of a numrical column using Numpy and Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

data= np.random.randn(1000)
hist, edges = np.histogram(data, bins=10)
plt.hist(data, bins=edges, edgecolor='black', alpha=0.7)

plt.title('Histogram of a NumPy array')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()