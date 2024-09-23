# 3.Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value

l1 = [1,2,3,4,5,6,7,8,9,0]


n = int(input("Enter a value, and we will find the pairs that sum to it: "))

pairs = []
seen = set()  # Set to keep track of numbers we've seen

# Iterate through the list
for num in l1:
    complement = n - num  # Calculate the complement
    if complement in seen:
        pairs.append((complement, num))  # Store the pair
    seen.add(num)  # Add the current number to the set

# Output the result
if pairs:
    print(f"Pairs in the list that sum to {n}: {pairs}")
else:
    print(f"No pairs found that sum to {n}")

