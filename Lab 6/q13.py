# lambda agrument can be more than one: expression can only be one
# map : map( function, iterable)
# filter : map( function, iterable)
# reduce : map( function, iterable)

# l = [1,2,3,4,5,6,7,8,9]

# var = map(lambda x: x*2, l)

# print(list(var))

# var1 = filter(lambda x : x%2 ==0 , l)
# print(list(var1))

# from functools import reduce
# var3 = reduce(lambda x,y : x+y, l)
# print(var3)

# Write a Python program to sort a dictionary by values instead of keys

# Write a Python program to sort a dictionary by values instead of keys

dict1 = {
    1: 6,
    2: 5,
    3: 4,
}

items = list(dict1.items())


# Sort the list of tuples based on the second element (value)
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][0] > items[j][0]:  # Change '<' to '>' for ascending order
            items[i], items[j] = items[j], items[i]

# Convert back to a dictionary
sorted_dict = dict(items)

print(sorted_dict)
