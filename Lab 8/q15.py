# Write a Python function takes a two-word strings and find if both words begin with same letter or not.

def check(x,y):
    if x[0].upper() == y[0].upper():
        print("both words starts with same letter")
    else:
        print("both words does not start with same letter")
        
check("Salin", "sampada")