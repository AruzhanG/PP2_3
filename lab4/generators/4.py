def squares(a,b):
    while a <= b:
        yield  a ** 2
        a += 1
        
for square in squares(1,20):
    print(square,end = ', ')