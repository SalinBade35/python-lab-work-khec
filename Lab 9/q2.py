#  Write a Python function student_data () that will print the ID of a student (student_id). If 
# the user passes an argument student_name or student_class the function will print the 
# student name and class.

class Student:
    def student_data(student_id, student_name=None, student_class=None):
        print(f"Student ID: {student_id}")
        if student_name:
            print(f"Student Name: {student_name}")
        if student_class:
            print(f"Student Class: {student_class}")

s1 = Student
s1.student_data(790335, "Salin", "Computer Science")
s1.student_data(790336, "Sampada")
