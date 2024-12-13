# create a function that takes a list and a number, return a list after adding the number to the list preventing it from changing the original list.

def list_add(list,n):
    list_new=list.copy()
    for i in range(len(list)):
        list_new[i]=list[i]+n
    return list_new

list = [1,2,3,4]
n = 10

print(list_add(list,n))
