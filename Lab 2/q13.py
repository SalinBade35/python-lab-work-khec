#wap script that takes a letter grade (A, B, C, D, E) as input and prints the corresponding grade point average (GPA). Include an else statement to handle invalid input.

grade = input("entre your grade: ")
grade = grade.upper()

dict1 = {
    "A" : 4.00,
    "B" : 3.00,
    "C" : 2.00,
    "D" : 1.00,
    "E" : "Fail"
}

if grade in dict1:
    print(dict1[grade])
    
if grade not in dict1:
    print("Invalid")

