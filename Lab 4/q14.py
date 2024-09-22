#wap to sort a given list of string numerically 

l1 = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500'] 

l1.sort(key = int, reverse = False)
# print(l1) still items are in string type cause the sort just changes the position not the tpe

l2 = []
for i in l1:
    l2.append(int(i))
    
print(l2)




# l2 = sorted(map(int, l1))
# print(l2)


    

