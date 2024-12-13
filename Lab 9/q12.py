# Modify the ElectricCar class to include an __init__() method that properly initializes the 
# parent class's attributes as well as its own attribute battery_size.

class Car:
    def __init__(self, fuel_level):
        self.fuel_level = fuel_level
        print(f"Fuel Level: {self.fuel_level}")

class ElectricCar(Car):
    def __init__(self, fuel_level, battery_size=10):
        super().__init__(fuel_level)
        self.battery_size = battery_size 
    
    def describe_battery(self):
        print(f"Battery Size: {self.battery_size}")

ecar = ElectricCar(50, 15)
ecar.describe_battery()

ecar2 = ElectricCar(70)
ecar2.describe_battery()
