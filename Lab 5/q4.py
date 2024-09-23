# . Write a Python program to replace the last value of tuples in a list. 
list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list2 = []
str1 = ""

for i in list1:
    for j in i:
        list2.append(j)
        
print(list2)

for i in range(9):
    if i == 2  or i == 5 or i == 8:
        list2[i] = 100
        
print(list2)


   
        

    
        