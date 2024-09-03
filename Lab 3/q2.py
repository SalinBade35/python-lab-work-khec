#2. Write a program to read an integer from user. For all non-negative integers i < n, print i2

n = int(input("n: "))

for i in range(0,n+1,1):
    print(i**2,end=" ")
    