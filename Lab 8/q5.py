# Write a Python function to create and print a list where the values are the squares of numbers between 
# 1 and 20 (both included). 

def listGenerator():
    list1 = []
    for i in range(21):
        list1.append(i*i)
    return list1

print(listGenerator())
        