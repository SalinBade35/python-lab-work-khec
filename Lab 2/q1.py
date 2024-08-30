#wap to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

n = int(input("entre number: "))

if(n>17):
    x = n - 17
    print(2*x)

else:
    print(n, "is less than 17")