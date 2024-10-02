# . Use the get() method to fetch the value of ‘age’ from the above dictionary. If the ‘age’ is not a key,  it should return ‘Key not available’. 


dict1 = {
    'name' : 'Hari',
    'age': 29,
    'city': 'Bhaktapur',
    
}

if 'age' in dict1:
    print(dict1.get('age'))
    
else:
    print("Key not available")