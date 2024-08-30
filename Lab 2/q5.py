#Write a Python program to check whether a variable is an integer, or string, or a list, or tuple, or set.

a=["list","items"]
if isinstance(a,int):
    print("It is an integer")
elif isinstance(a,str):
    print("It is a string")
elif isinstance(a,list):
    print("It is a list")
elif isinstance(a,tuple):
    print("It is a tuple")
elif isinstance(a,set):
    print("It is a set")
else:
    print("Invalid input")