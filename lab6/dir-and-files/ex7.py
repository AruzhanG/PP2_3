with open('a.txt', 'r') as fisrtfile, open('b.txt','a') as secondfile:
    for line in fisrtfile:
        
        secondfile.write(line)

