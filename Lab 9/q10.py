# Add a method to the Car class that allows you to update the car's fuel_level. Then, create an
# instance of Car, update its fuel_level to 50, and call check_fuel_level() to verify the change.


class Car:
    fuel_level = 100
    
    def check_fuel_level(self, fuel_level):
        self.fuel_level = fuel_level
        print(self.fuel_level)
    
c1 = Car()
c1.check_fuel_level(50)