# Write a Python class named Student with two attributes student_name, marks. Modify the 
# attribute values of the said class and print the original and modified values of the said 
# attributes.

class Student:
    student_name = "Salin"
    marks = 90
    
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks
        
    def student_data(self):
        print(f"Student Name: {self.student_name} \nMarks: {self.marks}")   
        
s1 = Student("xenium", 100 )
s1.student_data()