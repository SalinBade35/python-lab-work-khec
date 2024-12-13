#Write a Python function to check whether a number falls within a given range. 

n = 10

def range_checker(value):
    if value >= n:
        print(f"{value} doesn't fall under the range {n}")
    else:
        print(f"{value} does fall under the range {n}")
value = int(input("entre the number: "))
range_checker(value)

