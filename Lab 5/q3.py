#wap to find repeated items in a tuple
t1 = (1,2,3,3,3,4,5,5,6,7)
l1 = []
repeated_items = []

for item in t1:
    if t1.count(item)>1 and item not in repeated_items:
        repeated_items.append(item)
        
print(repeated_items)



































for item in t1:
    if t1.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print(repeated_items)



           
    
    

