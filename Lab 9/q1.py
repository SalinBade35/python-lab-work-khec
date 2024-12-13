# Define a Python function student(). Using function attributes display the names of all 
# arguments. 

# def student(*args):
#     print(kwargs)

# student_name = ['Salin', 'Sampada', 'Khan']
# student(student_name)
    
class Student:
    def __init__(self, student_name, student_class):
        self.student_name = student_name
        self.student_class = student_class
        
s1 = Student("Salin", "Computer Science")
print(s1.student_name)
print(s1.student_class)

