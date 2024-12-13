#  Write a Python a function that takes a string as argument and print the most common character in that string

def most_common_char(string):
    char_count = {}   # this is a empty dictionary
    for i in string:
        if i in char_count:
            char_count[i] += 1
           
        else:
            char_count[i] = 1
            
    max_count = max(char_count.values())
    for i, count in char_count.items():
        if count == max_count:
            return i

print(most_common_char("aabc"))


# empty stuffs: 
# set1 = set()
# dict1 = {}
# tuple = ()
# list = []