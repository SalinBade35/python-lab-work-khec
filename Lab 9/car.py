class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year                        

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

    def update_year(self, new_year):
        self.year = new_year