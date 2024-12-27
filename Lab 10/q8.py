# Calculate the cumulative sum of a NumPy array and store the results in a new Pandas 
# DataFrame column. 

import pandas as pd
import numpy as np

data = {'Values': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

numpy_array = np.array([1, 2, 3, 4, 5])

df['Cumulative_Sum'] = numpy_array.cumsum()

print(df)