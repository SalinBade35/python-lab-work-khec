#. Write a Python script to check whether a given key already exists in a dictionary

dict1 = {
    1: 6,
    2: 5,
    3: 4,
}

n = input("entre the key to check if it exist or not in a dictionary: ")

if int(n) not  in dict1:
    print(f"{n} does not exist")
else:
    print(f"{str(n)} exists")
    



