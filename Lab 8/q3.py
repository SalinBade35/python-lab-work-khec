#Write a Python function that accepts a string and counts the number of vowel and consonant letters. 

def check(value):
    v = 0
    c = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in value:
        if i in vowels:
            v+=1
        else:
            c+=1
    return f"{value} has {v} vowel and {c} consonants"

value = input("entre the string: ")
print(check(value)) 