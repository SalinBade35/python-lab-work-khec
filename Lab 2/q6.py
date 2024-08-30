#wap script that takes two numbers as input and prints their sum, difference, product and quotient using match case.

a = float(input("a :"))
b = float(input("b :"))

operator = input("+-*/: ")
match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("invalid")
