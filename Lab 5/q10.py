# Write a Python program to compute the element-wise sum of given tuples. 
# Original lists: 
# (1, 2, 3, 4) 
# (3, 5, 2, 1) 
# (2, 2, 3, 1) 
# Element-wise sum of the said tuples: 
# (6, 9, 8, 6) 


t1 =(1, 2, 3, 4) 
t2 =(3, 5, 2, 1) 
t3 =(2, 2, 3, 1)
t4 = []
sum = 0

for i in range(len(t1)):
    sum = t1[i]+ t2[i] + t3[i]
    t4.append(sum)
    
print(list(t4))