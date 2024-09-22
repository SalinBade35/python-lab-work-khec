#wap to copy a content of one list to another

l1 = [1, 'apple', 5.70]
l2 = l1  # no new list is created instead l2 becomes another reference to the same list object that l1 refers to
print(l2)


import copy

# Original list
original = [1, [2, 3], 4]

# Shallow copy
shallow_copy = original.copy()
shallow_copy[1][0] = 'changed'

# Results
print(original)      # Output: [1, ['changed', 3], 4]
print(shallow_copy)  # Output: [1, ['changed', 3], 4]

# Deep copy
deep_copy = copy.deepcopy(original)
deep_copy[1][0] = 'changed again'

# Results
print(original)      # Output: [1, ['changed', 3], 4]
print(deep_copy)     # Output: [1, ['changed again', 3], 4]

