# 1. Write a python program to find the sum of n natural numbers 

n = int(input("n: "))

for i in range(1,n+1):
    n = n+1
    
print(n)

#we could have also used the direct formula:
#sum = n(n+1)/2