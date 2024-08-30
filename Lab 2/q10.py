# #wap name and age and tell in which year will they turn 100 years

# name = input("entre name: ")
# age = int(input("entre age: "))

# x = 100 - age
# y = 2024 + x

# print(f"{name.capitalize()} you will turn 100 in {y} AD.")

from datetime import datetime

name = input("Enter name: ")
age = int(input("Enter age: "))

current_year = datetime.now().year
x = 100 - age
y = current_year + x

print(f"{name.capitalize()}, you will turn 100 in {y} AD.")
