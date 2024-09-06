#. Write a Python program to guess a number between 1 and 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again 
# until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the 
# program will exit. Import random

from random import randint

a = randint(0, 10)

n = int(input("Guess a number from 1 to 9: "))

a = randint(1,9)

print(a)

if(a == n):
    print(" You guess right")
    
else:
    print("You guess incorrect")