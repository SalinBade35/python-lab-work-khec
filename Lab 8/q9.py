# Write a Python program to find the power of a number using recursion function. 

def power(x, y):    
    if y == 0:  
        return 1    
    else:  
        return (x * power(x, y-1))
    
print(power(5,2))