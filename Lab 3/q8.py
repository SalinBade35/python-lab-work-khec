#  Write a Python program that accepts a string and calculates the number of digits and letters. 
# Sample Data : Python 3.2 
# Expected Output : 
# Letters 6 
# Digits 2 
# Note: Use isdigit, isalpha and pass functions. 

n = input("entre word or sentence: ")

alphabets = 0


for i in n :
	if (i.isalpha()):
		alpha+=1
print("Number of Digit is", len(n)-alphabets)
print("Number of Alphabets is", alphabets)


