from functools import reduce
from operator import mul

my_list = [2, 3, 4, 5]

result = reduce(mul, my_list)

print(result)
