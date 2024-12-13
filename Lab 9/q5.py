# Write a Python class named Student with two attributes: student_id, student_name. Add a 
# new attribute: student_class. Create a function to display all attributes and their values in the 
# Student class. 

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        # Check if the className attribute exists before accessing it
        if hasattr(self, 'className'):
            print(f"Class Name: {self.className}")
        else:
            print("Class Name: Not assigned")

s1 = Student(790335, "Salin Bade")
s1.className = "BCE"  # Adding the attribute dynamically
s1.display()
