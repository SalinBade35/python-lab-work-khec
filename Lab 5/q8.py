#  Write a Python program to calculate the average value of the numbers in a given tuple of 
# tuples. 
# Original Tuple: 
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) 
# Average value of the numbers of the said tuple of tuples: 
# [30.5, 34.25, 27.0, 23.25] 
# Original Tuple: 
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)) 
# Average value of the numbers of the said tuple of tuples: 
# [25.5, -18.0, 3.75] 


# t1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) 

# for i in t1:
#     print(i)


# Original Tuple
tuple1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

# Initialize a list to store the averages
averages = []

# Loop through the index positions of the inner tuples
for i in range(len(tuple1[0])):
    # Variable to store the sum of elements at the same index across all tuples
    total = 0
    # Loop through each tuple and sum up the elements at the same index
    for t in tuple1:
        total += t[i]
    # Calculate the average and add it to the averages list
    avg = total / len(tuple1)
    averages.append(avg)

# Print the result
print("Average value of the numbers of the said tuple of tuples:", averages)
