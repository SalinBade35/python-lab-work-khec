# modify above function so that it has default values of 2 for both length and width

def area(length=2,width=2):
    area=length*width
    return area 

def perimeter(length=2,width=2):    
    perimeter=2*(length+width)
    return perimeter


print("Area is:",area())
print("Perimeter is:",perimeter())