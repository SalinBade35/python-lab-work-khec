#  Create a child class called ElectricCar that inherits from the Car class. Add an attribute 
# battery_size to the child class with a default value. Also, add a method describe_battery() 
# that prints information about the battery size. 

class Car:
    pass

class ElectricCar(Car):
    battery_size  = 10
    
    def describe_battery(self):
        print(self.battery_size)
        

e1 = ElectricCar()
e1.describe_battery()