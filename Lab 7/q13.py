# Write a Python function that checks whether a passed string is a palindrome or not. 

def checker(string1):
    if string1 == string1[::-1]:
        print("the string is palindrome")
    else:
        print("the string is not a palindrome")
        
checker("malayalam")