#  Write a Python program to develop a rock paper scissors game, restart the game until the user 
# press ‘n’ when the game ends

import random

while True:
    user = int(input("\n1. Rock\n2. Paper\n3. Scissors\n4. Exit\n"))
    if user == 4: 
        break
    if user not in [1, 2, 3]: #10
        continue
    
    options = ["rock", "paper", "scissors"]
    user = options[user-1]
    computer = random.choice(options)
    print(f"Computer chose {computer}.", end=" ")
    print(f"You choose {user}")

    if user == computer:
        print("It's a draw!")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
