# Write a Python function that takes a sentence, and return a sentence with the words reversed.



def reverse_str(sentence):
    str1 = ""
    words_list = sentence.split()  # Split the sentence into words
    reversed_words = []  # List to store reversed words
    
    for word in words_list:
        reversed_words.append(word[::-1])  # Reverse each word
    
    for i in reversed_words:
        a = i
        str1 = str1 + a + " "
    return str1
   

print(reverse_str("my name is salin"))