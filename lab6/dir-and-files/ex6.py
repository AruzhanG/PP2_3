import string
for letter in string.ascii_letters:
    fd = open(letter + ".txt","w")
    fd.close()
    