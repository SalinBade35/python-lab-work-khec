#  Write a Python function that takes a sentence as a parameter and print the words in ascending order. 

def sort_words(sentence):   
    words = sentence.split()   # The split() method splits the sentence into a list of words by spaces.
    sorted_words = sorted(words)   
    return sorted_words

sentence = input("Enter a sentence: ")   
sorted_words = sort_words(sentence)   
print("Sorted words:", sorted_words)