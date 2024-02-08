def reverse_words(sentence):
    words = sentence.split()
    reverse_words = ' '.join(reversed(words))
    return reverse_words
user_input = input("Given sentence:") 
result = reverse_words(user_input)         
print("Reversed sentence",result)       