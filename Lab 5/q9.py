# Write a Python program to convert a given tuple of positive integers into an integer. 
# Original tuple: 
# (1, 2, 3) 
# Convert the said tuple of positive integers into an integer: 
# 123 
# Original tuple: 
# (10, 20, 40, 5, 70) 
# Convert the said tuple of positive integers into an integer: 
# 102040570



t1 = (1, 2, 3)
var = ''

for i in t1:
    var += str(i)

var1 = int(var)
print(var1)










