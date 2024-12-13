#  Override the describe_car() method in the ElectricCar class to include information about 
# its battery size along with the car's make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_car(self):
        super().describe_car()
        print(f"Battery Size: {self.battery_size} kWh")

e_car = ElectricCar("Tesla", "Model S", 2023, 100)
e_car.describe_car()
super(ElectricCar, e_car).describe_car() # this calls the parent's method
