#wap to remove duplicates from  a list.
l = [1,2,3,4,4,5,6,6,67,6,6]
m = []

for i in l:
    if i not in m:
        m.append(i)
        
print(m)


