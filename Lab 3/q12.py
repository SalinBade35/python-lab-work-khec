# 12. Write a Python program to construct the following pattern, using a nested for loop. 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

#for upper increasing triangle
for  i in range(5):
    for j in range(i+1):
        print("*", end = " ")
    print()
    
#for lower decreasing triangle
for i in range(4):    
    for j in range(i,4):
        print("*", end = " ")
    print()
    
    