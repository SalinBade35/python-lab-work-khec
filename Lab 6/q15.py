#  Write a Python program to sort a list alphabetically in a dictionary. 
# Sample: num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 
# Output: {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}




num1 = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 


# num1 = {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

for x, y in num1.items():
    y.sort()
    
print(num1.items())
        
    








