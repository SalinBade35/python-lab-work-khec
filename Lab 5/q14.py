# 14.Write a Python program to find the longest common prefix of all strings. Use the Python set

# Initialize an empty list to hold the strings
l1 = []

# Get the number of strings from the user
n = int(input("How many strings would you like to enter? "))

# Collect the strings from the user
for i in range(n):
    a = input("Enter string {}: ".format(i + 1))  # Prompt for each string
    l1.append(a)  # Add the string to the list

# Check if the list is empty
if not l1:
    print("Longest common prefix: ")
else:
    # Initialize the prefix as the first string
    prefix = l1[0]

    # Use a set to store prefixes and compare them
    for string in l1[1:]:
        # Reduce the prefix until it matches the start of the current string
        while prefix and not string.startswith(prefix):
            prefix = prefix[:-1]  # Remove the last character from the prefix

    # Output the longest common prefix
    print("Longest common prefix:", prefix)


