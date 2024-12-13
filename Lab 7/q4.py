# wap function that take two parameters length and width and return the area and permimeter of rectangle.

def area(length,width):
    area=length*width
    return area 

def perimeter(length,width):
    perimeter=2*(length+width)
    return perimeter

length=int(input("Enter length: "))
width=int(input("Enter width: "))
print("Area is:",area(length,width))
print("Perimeter is:",perimeter(length,width))