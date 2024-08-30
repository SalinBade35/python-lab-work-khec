#Create a program that asks for an age and prints the category like child, teen, adult, old

# age = int(input("entre your age: "))

# agelist = {
#     range(0, 13) : "child" ,
#     range(13, 20) :  "teen" , 
#     range(20, 60) : "adult",
#     range(60,1000 ) : "oldage"
# }
        
    
# if age in agelist:
#     print(agelist[age])
    
# else:
#     print("Invalid")

age = int(input("Enter your age: "))

agelist = {
    range(0, 13): "child",
    range(13, 20): "teen",
    range(20, 60): "adult",
    range(60, 1000): "oldage"
}

category = None

# Check which range the age falls into
for age_range123, label123 in agelist.items():
    if age in age_range123:
        category = label123
        break

if category:
    print(f"You are a {category}.")
else:
    print("Invalid age")

    

