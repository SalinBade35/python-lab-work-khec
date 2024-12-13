# Define a class named Car with attributes make, model, and year. Add a method 
# describe_car() that prints a neatly formatted descriptive name of the car. Then, create an 
# instance of Car and call this method. 

class Car:
    make = None
    model = None
    year = None
    
    def describe_car(self):
        print(f"{self.make}  {self.model}  {self.year}")

c1 = Car()
c1.make = "Porche GT3"
c1.model = 2023
c1.year = 2024

c1.describe_car()
        
        