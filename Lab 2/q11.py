#create a python script that converts temp from fahrenhiet to celcius and vice versa, based on user input

n = float(input("option: \n1. C to F\n2.F to C \n"))
value = float(input("value: "))
if n == 1:
    f = (value * ((9/5))+32)
    print(f"{value}C = {f}F")
    
else:
    c = (value-32)*(5/9)
    print(f"{value}C= {c}C")
    
    