# . Write a Python program to input n numbers from user; count the number of even and odd numbers 
# from the input numbers and exit until the user input ‘0’. 
# Input numbers = (7, 4, 3, 8, 5, 6, 1, 2, 9) 
# Expected Output : 
# Number of even numbers : 4 
sum = 0
odd_count = 0
even_count = 0
n = int(input("n: "))
while(n!=0):
    if(n % 2 == 0):
        even_count += 1
    else:
        odd_count += 1
    sum = sum + n
    n = int(input("n: "))
    
print(f"total sum of number: {sum}")
print(f"number of even number: {even_count}\n number of odd number: {odd_count}")