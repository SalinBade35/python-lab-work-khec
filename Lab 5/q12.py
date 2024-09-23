# 2.Write a Python program to create an intersection, a union, set difference and a symmetric 
# difference of sets. Also find the length, maximum and minimum values in a set. 




# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Intersection
intersection = set1.intersection(set2)

# Union
union = set1.union(set2)

# Set difference
difference_set1_set2 = set1.difference(set2)
difference_set2_set1 = set2.difference(set1)

# Symmetric difference
symmetric_difference = set1.symmetric_difference(set2)

# Length, maximum, and minimum of a set
length_set1 = len(set1)
max_set1 = max(set1)
min_set1 = min(set1)

# Output results
print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", intersection)
print("Union:", union)
print("Set Difference (set1 - set2):", difference_set1_set2)
print("Set Difference (set2 - set1):", difference_set2_set1)
print("Symmetric Difference:", symmetric_difference)
print("Length of Set 1:", length_set1)
print("Maximum value in Set 1:", max_set1)
print("Minimum value in Set 1:", min_set1)
