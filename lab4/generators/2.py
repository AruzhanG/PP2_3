def my_generator(N):
    value = 0
    while value < N:
        if value % 2 == 0:
            yield value
        value += 1
    
for even in my_generator(20):
    print(even, end=', ')
  