# Write a Python class named Dog that has two attributes: name and age. Then, create an 
# instance of your Dog class and print out the name and age of the dog. 

class Dog:
    name = None
    age = None
    
    def display(self):
        print("name : ", self.name)
        print("age: ", self.age)

dog1 = Dog()
dog1.name = "Husky"
dog1.age = 3

dog1.display()