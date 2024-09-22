#wap to get largest and smallest number in a list without using builtin functions

l = [1,2,3,4,5]

l.sort()

print(f"largest : {l[-1]}\nsmallest: {l[0]}")

# for i in range(0, len(l)):
#     largest = l[0]
#     smallest = l[0]
    
#     if largest < l[i]:
#         largest = l[i]
#     if smallest > l[i]:
#         smallest = l[i]
# print(f"largest : {largest}\nsmallest: {smallest}")