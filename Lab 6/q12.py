#  Write a Python program to sort a dictionary by its keys. 

dict1 = {
    1 : 6,
    2 : 5,
    3 : 4,
}

l = []
for i in dict1:
    l.append(i)
    
l.sort()
# print(l)

dict2 = {}
for i in l:
    dict2[i] = dict1[i]
    
print(dict2)
    