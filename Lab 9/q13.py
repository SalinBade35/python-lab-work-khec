# Add a new method to the ElectricCar class that calculates the range of the car based on the 
# battery size. The method should print a message indicating the range.

class ElectricCar:
    fuel = 10

    def check(self):
        if self.fuel > 0 and self.fuel <= 5:
            print("Range = 50km")
        elif self.fuel > 5 and self.fuel <= 10:
            print("Range = 100km")
        else:
            print("Invalid fuel level not available.")

e1 = ElectricCar()
e1.check()

e1.fuel = 3
e1.check()

e1.fuel = 15
e1.check()


            