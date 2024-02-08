def palindrome(word):
    reverse_word = ''.join(reversed(word))
    if word == reverse_word:
        print("Yes")
    else:
        print("No")
        
palindrome("mam")    