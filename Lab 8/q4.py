# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
 
n = int(input("entre how many element will you list contain? "))
list1 = []
for i in range(n):
    value = input("value: ")
    list1.append(value)
    
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
        
print(list2)

