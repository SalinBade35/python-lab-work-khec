# define a function called calculate_average that takes a list of numbers as input and calculate the average of list. finally. the fucntion returns the average of that list

def calculate_average(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum/len(list)
list1 = [1,2,3,4,5,6,7,8,9,10]
print(calculate_average(list1))
