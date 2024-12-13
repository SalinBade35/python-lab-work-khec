# Write a Python class named Student with two attributes student_id, student_name. Add a 
# new attribute student_class and display the entire attribute and the values of the class. Now 
# remove the student_name attribute and display the entire attribute with values. 

class Student:
    student_id: None
    student_name: None
    
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        
s1 = Student(790335, "Salin")
s1.student_class = "Computer Science"
print(s1.student_id)
print(s1.student_name)
print(s1.student_class)

del s1.student_name

print(s1.student_id)
print(s1.student_class)
        

        