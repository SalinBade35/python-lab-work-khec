#wap to find the second smallest and second largest numbers in  a list
l = [1,2,3,4,5,6,7,8,9,10]

l.sort()

print(f"second largest : {l[-2]}\nsmallest: {l[1]}")

# for i in range(0, len(l)):
#     largest = l[0]
#     smallest = l[0]
    
#     if largest < l[i]:
#         largest = l[i]
        
#     if smallest > l[i]:
#         smallest = l[i]
# second_largest = l[l.index(largest)-1]  
# second_smallest = l[l.index(smallest)+1]
# print(f"second largest : {second_largest}\nsmallest: {second_smallest}")