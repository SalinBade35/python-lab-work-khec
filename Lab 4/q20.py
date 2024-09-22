#wap to insert n values in a list and find those values in a list that are greater than a specified number.

l1 = []

n = int(input("how many items do you like to entre: "))

for i in range(0, n):
    m = int(input("value: "))
    l1.append(m)
    
print(l1)

a = int(input("\nentre checking number: "))

l2 = [i for i in l1 if i>a]
print(l2)

    
