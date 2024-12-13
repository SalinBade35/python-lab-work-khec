#  Write a Python function that takes a date in string format DD/MM/YYYY and checks if it is a valid date and in the correct format. 

def check_date(dd,mm,yy):
    if dd > 30 or dd < 1 or mm > 30 or mm < 1 or yy > 2024 or yy < 1:
        print("date is invalid")
    else:
        print(yy,mm,dd , "is valid" )
    
    

dd = int(input("dd: "))
mm = int(input("mm: "))
yy = int(input("yr: "))

check_date(dd,mm,yy)