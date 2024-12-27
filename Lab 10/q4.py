# Select the first and last 7 rows of a Pandas DataFrame.

import pandas as pd

data = {'Name': ['Serij', 'Ram', 'Rabin', 'Santosh', 'Milan', 'Alina', 'Bijay', 'Chandra', 'Dinesh', 
'Suman'], 
'Age': [26, 32, 25, 31, 28, 22, 35, 30, 40, 28], 
'Salary': [50000, 60000, 45000, 70000, 55000, 60000, 70000, 55000, 75000, 65000]} 
df = pd.DataFrame(data) 
selected_rows = pd.concat([df.head(7)]) 
print("First 7 rows:") 
print(selected_rows) 
selected_rows = pd.concat([df.tail(7)]) 
print("\nLast 7 rows:") 
print(selected_rows) 