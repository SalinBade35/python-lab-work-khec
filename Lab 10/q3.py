# select rows from a DataFram based on a multiple conditions

import pandas as pd

data = {'Name': ['Tom', 'Nick', 'John', 'Tom', 'Nick', 'John', 'Tom', 'Nick', 'John'],
    'Age': [20, 21, 22, 20, 21, 22, 20, 21, 22],
    'Salary': [1000, 2000, 3000, 1000, 2000, 3000, 1000, 2000, 3000]}

df = pd.DataFrame(data)

selected_rows = df[ (df['Age'] == 20) & df['Salary'] < 1000]

print(selected_rows)
