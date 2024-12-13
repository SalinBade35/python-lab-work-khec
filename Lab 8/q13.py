""" 
Write a Python function that takes a name (string) as argument and capitalizes the first and fourth letters 
of the input name.
"""

def name(str):
    list1 = list(str)
    str1 = ""
    list2 = []
    for i in list1:
        if i == list1[0] or i == list1[3]:
            a = i.capitalize()
            list2.append(a)
        else:
            list2.append(i)
    
    for i in list2:
        a = i
        str1 = str1 + a
    return str1
        
print(name('sampada'))
    