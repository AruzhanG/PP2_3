def my_generator(n):
    value = 0
    while value <= n:
        yield n
        n -= 1
        
        
for num in my_generator(6):
    print(num)