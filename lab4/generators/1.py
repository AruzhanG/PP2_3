def my_generator(n):
    value = 1
    while value <= n:
        yield value ** 2
        value += 1
        
        

for square in  my_generator(6):
    
    print(square, end= ' ')
  