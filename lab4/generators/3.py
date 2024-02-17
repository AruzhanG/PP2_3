def my_generator(N):
    value = 0
    while value < N:
        if value % 3 == 0 and value % 4 == 0:
            yield value
        value += 1
    
for even in my_generator(100):
    print(even, end=', ')