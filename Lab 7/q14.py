# Write a Python function that takes a string as input and counts the number of uppercase and lowercase 
# characters in the string.

def count_upper_lower(string):
    upper = 0
    lower =  0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("No. of Uppercase characters:",upper)
    print("No. of Lowercase characters:",lower)
    
string = input("Enter a string: ")
count_upper_lower(string)