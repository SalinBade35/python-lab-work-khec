#wap to take input from users and store it in a variable spam then print hello if 1 is stored in spam, print HI if 2 stored in spam, adn print Greetings! if anyting else is the in spam


spam = int(input("entre number"))

if spam == 1:
    print("hello")

elif spam == 2:
    print("HI")
    
else:
    print("Greetings")