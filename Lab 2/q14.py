#wap that takes a number and prints whether it is even, odd or zero or invalid for non integer inputs. this program should first check if the input is a valid integer and then check for the other conditions

n = input("entre value: ")  #as string

if(n.isdigit() == True):
    n = int(n)
    if(n == 0):
        print(f"{n} is zero")
        
    elif(n % 2 == 0 and n != 0):
        print(f"{n}, is even number")
        
    else:
        print(f"{n} is odd number")
        
else:
    print(type(n))
        
        
