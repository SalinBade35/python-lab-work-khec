#wap to print the numbers of a specified list after removing even numbers from it.

l = [1,2,3,4,5,6,7,8,9,10]

m = filter(lambda x: x % 2 != 0, l)
print(list(m))

for i in l:
    if i%2 ==0:
        l.remove(i)
        
        
print(l)

# for num in m:
#     print(num)  # This will print the odd numbers one by one.

# print(list(m))  # This will show the filtered list of odd numbers.
#  # note :Once consumed, the filter object cannot be used again.

