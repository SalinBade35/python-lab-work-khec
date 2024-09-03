# Write a Python program to get the Fibonacci series up to n terms. 
n = int(input("n:  "))

a, b = 0, 1
for i in range(0,n+1,1):
    print(a, end="   ")
    a, b = b, a + b
     