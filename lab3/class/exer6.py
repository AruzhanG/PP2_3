def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers_str = input()
numbers_list = [int(x) for x in numbers_str.split()]

prime_numbers = list(filter(lambda x: is_prime(x), numbers_list))

print(prime_numbers)

        
        