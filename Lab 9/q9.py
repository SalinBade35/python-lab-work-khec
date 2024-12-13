# Modify the Car class so that it has a default value for an attribute called fuel_level, with a 
# default value of 100. Add a method check_fuel_level() that prints the car's current fuel level. 

class Car:
    fuel_level = 100
    def check_fuel_level(self):
        print(self.fuel_level)
        


c1 = Car()
# c1.fuel_level = 220
c1.check_fuel_level()