# wap that accepts radius and returns the area and circumference of a circle. import pi from math

import math

def area(radius):
    area=math.pi*radius*radius
    return area

def circumference(radius):
    circumference=2*math.pi*radius
    return circumference    

radius=int(input("Enter radius: "))
print("Area is:",area(radius))
print("Circumference is:",circumference(radius))