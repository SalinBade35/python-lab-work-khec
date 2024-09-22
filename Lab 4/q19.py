# write a program to insert a given string at the beginning of all items in a list.

# Sample list : [1,2,3,4], string : emp 
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

l = [1,2,3,4]

l1 = ["emp" + str(i)  for i in l]
    
    
print(l1)