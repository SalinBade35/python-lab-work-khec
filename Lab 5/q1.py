# wap to convert tuple to a string

# my_tuple = ('H', 'e', 'l', 'l', 'o')
my_tuple = (1,2,3)

result = "" # empty string

for element in my_tuple: # Iterate through tuple and concatenate elements
    result += str(element)

print(result)
print(type(result))
