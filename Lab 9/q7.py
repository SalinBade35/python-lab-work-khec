# Create two instances from the Dog class. For the first instance, set the name to 'Bruno' and 
# age to 2. For the second instance, set the name to 'Sher' and age to 3. Print out the information 
# for both dogs. 

class Dog:
    name = None
    age = None
    
    def display(x):
        print(f"name: {x.name}")
        print(f"age: {x.age}")
    
d1 = Dog()
d2 = Dog()
d1.name = "Bruno"
d2.name = "Sher"
d1.age = 2
d2.age = 3

d1.display()
d2.display()