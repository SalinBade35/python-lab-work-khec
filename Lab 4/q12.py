#wap to merge two list and remove all duplicates from the combined list.

l1 = [1,2,3,4]
l2 = [1,2,6,7,8,9,4,4,4,3]
l3 = []
for i in l1+l2:
    if i not in l3:
        l3.append(i)
print(l3)