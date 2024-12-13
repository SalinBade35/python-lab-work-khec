# Write a Python program using a function to count the even and odd numbers from a given list and also print them separately.

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def even_odd(list1):
    even = []
    odd = []
    for i in list1:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

even, odd = even_odd(list1)
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")