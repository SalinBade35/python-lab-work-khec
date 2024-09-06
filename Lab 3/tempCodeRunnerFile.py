n = input("entre word or sentence: ")

alpha = 0


for i in n :
	if (i.isalpha()):
		alpha+=1
print("Number of Digit is", len(n)-alpha)
print("Number of Alphabets is", alpha)