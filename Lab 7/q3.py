#wap to calculate the factorial of a number (a non-negative integer) with and without using recursion. the function accepts the number as an argument.

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter a number: "))
print("Factorial of",n,"is",fact(n))

def fact_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact_rec(n-1)

n=int(input("Enter a number: "))
print("Factorial of",n,"is",fact_rec(n))    
