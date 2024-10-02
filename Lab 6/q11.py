#  Write a Python program to find all keys in a dictionary that have the given value. 
dict1 = {
    'name' : 'Hari',
    'age': 29,
    'city': 'Bhaktapur',
    
}

print(dict1.keys())
a = "Hari"
for x,y in dict1.items():
    if a == y:
        print(x,y)
        