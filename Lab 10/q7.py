# Perform element-wise addition of a NumPy array and a Pandas DataFrame column. 

import pandas as pd 
import numpy as np 
data = {'Name': ['Serij', 'Ram', 'Rabin', 'Santosh', 'Milan'], 
'Age': [25, 30, 22, 35, 28], 
'Salary': [50000, 60000, 45000, 70000, 55000]} 
df = pd.DataFrame(data) 
numpy_array = np.array([1000, 2000, 3000, 4000, 5000]) 
df['Updated_Salary'] = np.add(df['Salary'], numpy_array) 
print(df) 