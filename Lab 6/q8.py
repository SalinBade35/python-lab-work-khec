# #  Write a Python script to merge two Python dictionaries. 
# # dict1 = {‘a’: 1, ‘b’: 2} and dict2 = {‘b’: 3, ‘c’:4} merge them into a single dictionary. What happens to the value of the key ‘b’?

# dict1 = {
#     'a': 1,
#     'b': 2
#     }


# dict2 = {
#     'b': 3,
#     'c': 4
#     }

# # dict2.update(dict1)
# dict1.update(dict2)

# print(dict1)

# # one sent explicitly gets the priority

dict1 = {
    'a': 1,
    'b': 2
    }


dict2 = {
    'b': 3,
    'c': 4
    }

# for i in dict2:
#     print(dict2[i]) # gives values
#     print(i)  # gives just key
    
for  i in dict2:
    dict1[i]  = dict2[i]
    
    # i gives the keys of dict2 one at a time,
    # dict1[i] meaning if i not in dict1 then i becomes new key
    # dict2[i] meaning dict2's key will be place in i and it give value 
    
print(dict1)

