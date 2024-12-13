# wap that takes two arguments, name and age and returns a dictionary with these as keys and their respective values.


def dict(name,age):
    dict={"name":name,"age  ":age}
    return dict 

name=input("Enter name: ")
age=int(input("Enter age: "))

dict=dict(name,age)
print(dict)

# keys only
print(dict.keys())

# values only
print(dict.values())

