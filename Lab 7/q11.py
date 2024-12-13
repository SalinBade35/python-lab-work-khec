# wap that takes a list of numbers and print each number doubled



def list_double(list):
    list1 = []
    for i in list:
        list1.append(i*2)
       
    return list1

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list_double(list))