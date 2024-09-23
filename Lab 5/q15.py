# Write a Python program to find the two numbers whose product is maximum among all the 
# pairs in a given list of numbers. Use the Python set. 

# Original list of numbers
list1 = [12, 4543, 65, 0, 1, 3]

# Convert the list to a set to remove duplicates
set1 = set(list1)

# Convert the set back to a list and sort it
list1 = sorted(set1)

print(f"{list1[-1]} and {list1[-2]} make the maximum product.")
print(f"Product: {list1[-1] * list1[-2]}")



