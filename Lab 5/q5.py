# wap to sort a tuple by its float element:
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')] 
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 

l = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
a = [] # empty list


for i in l:
    b = list(i)
    c = float(b[-1])
    a.append(c)
    a.append(b)
print(a)

 






