# wap function to find the maximum and minimum values, sum and multiplication of all the numbers in a list.

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def max_min(list):
    list.sort()
    return list[-1], list[0]

def sum(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum  

def multiplication(list):   
    mul=1
    for i in range(len(list)):
        mul=mul*list[i]
    return mul

print(max_min(list))
print(sum(list))
print(multiplication(list))